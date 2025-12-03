import tkinter as tk
import ast
import operator as op

def safe_eval(expr):
    allowed_ops={ast.Add:op.add,ast.Sub:op.sub,ast.Mult:op.mul,ast.Div:op.truediv,ast.Pow:op.pow,ast.Mod:op.mod,ast.UAdd:op.pos,ast.USub:op.neg}
    def _eval(node):
        if isinstance(node,ast.Expression):
            return _eval(node.body)
        if isinstance(node,ast.Constant):
            return node.value
        if isinstance(node,ast.BinOp):
            left=_eval(node.left)
            right=_eval(node.right)
            oper=allowed_ops.get(type(node.op))
            if oper is None:
                raise ValueError('unsupported operator')
            return oper(left,right)
        if isinstance(node,ast.UnaryOp):
            oper=allowed_ops.get(type(node.op))
            if oper is None:
                raise ValueError('unsupported operator')
            return oper(_eval(node.operand))
        if isinstance(node,ast.Call):
            raise ValueError('calls not allowed')
        raise ValueError('unsupported expression')
    node=ast.parse(expr,mode='eval')
    return _eval(node)

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator By Manthan')
        self.resizable(False,False)
        self.expr=tk.StringVar()
        entry=tk.Entry(self,textvariable=self.expr,font=('Segoe UI',20),justify='right',bd=5,relief='sunken')
        entry.grid(row=0,column=0,columnspan=4,sticky='nsew',padx=5,pady=5)
        buttons=[
            ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
            ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
            ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
            ('0',4,0),('.',4,1),('%',4,2),('+',4,3),
            ('(',5,0),(')',5,1),('^',5,2),('=',5,3),
        ]
        for (txt,r,c) in buttons:
            btn=tk.Button(self,text=txt,font=('Segoe UI',16),width=4,height=2,command=lambda t=txt:self.on_click(t))
            btn.grid(row=r,column=c,sticky='nsew',padx=3,pady=3)
        clr=tk.Button(self,text='C',font=('Segoe UI',16),width=4,height=2,command=self.clear)
        clr.grid(row=6,column=0,columnspan=2,sticky='nsew',padx=3,pady=3)
        bdel=tk.Button(self,text='⌫',font=('Segoe UI',16),width=4,height=2,command=self.backspace)
        bdel.grid(row=6,column=2,sticky='nsew',padx=3,pady=3)
        exitb=tk.Button(self,text='Exit',font=('Segoe UI',16),width=4,height=2,command=self.destroy)
        exitb.grid(row=6,column=3,sticky='nsew',padx=3,pady=3)
        for i in range(7):
            self.grid_rowconfigure(i,weight=1)
        for j in range(4):
            self.grid_columnconfigure(j,weight=1)
        self.bind('<Return>',lambda e: self.on_click('='))
        self.bind('<BackSpace>',lambda e: self.backspace())

    def on_click(self,t):
        if t=='=':
            try:
                expr=self.expr.get().replace('^','**')
                result=safe_eval(expr)
                self.expr.set(str(result))
            except Exception:
                self.expr.set('Error')
        else:
            self.expr.set(self.expr.get()+t)

    def clear(self):
        self.expr.set('')

    def backspace(self):
        self.expr.set(self.expr.get()[:-1])

if __name__=='__main__':
    app=Calculator()
    app.mainloop()
