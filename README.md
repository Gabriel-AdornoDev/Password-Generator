# 🔐 Password Generator

A simple yet powerful command-line tool to **generate secure passwords** and **evaluate the strength** of existing ones — built with Python.

## ✨ Features

- **Generate secure passwords** with custom length
- **Evaluate password strength** — Weak, Medium or Strong
- Uses Python's secrets module for cryptographically secure randomness
- Clean and interactive terminal menu

## 🚀 How to Run

Make sure you have Python 3 installed.

```bash
python main.py
```

## 🛠️ Technologies

- Python 3
- secrets — cryptographically secure random generation
- string — character set handling

## 🔒 Why secrets instead of andom?

The andom module is not suitable for security purposes. The secrets module uses the operating system's randomness source, making it safe for generating passwords and tokens.

## 👤 Author

**Gabriel Adorno** — [GitHub](https://github.com/Gabriel-AdornoDev)
