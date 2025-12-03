# Calculator App (Python)

This is a simple and clean GUI-based calculator built using **Python** and **Tkinter**. It supports basic arithmetic operations along with parentheses, exponent (`^`), modulo (`%`), and decimal calculations.

## Features

* User-friendly graphical interface
* Basic operations: `+`, `-`, `*`, `/`
* Additional operations: parentheses `()`, exponent `^`, modulo `%`
* Safe expression evaluation (AST-based)
* Clear button and backspace support
* Keyboard support for Enter and Backspace

## How It Works

* The UI is created using **Tkinter**.
* The input expression is parsed using Python's **AST** module to ensure safe evaluation.
* The `^` operator is converted to Python's `**` operator internally.

## How to Run

1. Make sure Python is installed on your system.
2. Save the main file as `calculator.py`.
3. Run the script:

   ```bash
   python calculator.py
   ```
4. The calculator window will open.

## File Structure

* `calculator.py` — Main application file containing GUI and logic.
* `README.md` — Documentation for understanding and running the project.

## Requirements

* Python 3.x (recommended)
* Tkinter (comes pre-installed with Python)

## Screenshot (Optional)

Add a screenshot of the app UI here if needed.

## License

This project is free to use and modify.
