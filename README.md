# Polygon Area Calculator 📐🟩

An Object-Oriented Python application to calculate geometric properties, evaluate spatial limits, and generate ASCII visualizations for Rectangles and Squares.

## 🛠️ Technologies Used
* **Python:** Core logic and calculations.
* **Object-Oriented Programming (OOP):** Utilizes class inheritance, method overriding, and magic methods (like `__str__` and `__init__`).

## 🗂️ Project Structure
* **`main.py`**: The main executable script containing the class definitions, methods, and testing data.

## 📊 Class Architecture
The logic is built on two related classes:
* **`Rectangle`**: The parent class. Manages `width` and `height` dimensions. Calculates area, perimeter, and diagonal length. Includes a `get_picture()` method for ASCII rendering and `get_amount_inside()` to determine how many times another shape fits inside it.
* **`Square`**: The child class. Inherits from `Rectangle` but strictly enforces equal sides through a unified `length` property, seamlessly updating all parent attributes when modified.

## 🚀 How to Run
1. Run the script in your terminal:
   ```bash
   python area.py
