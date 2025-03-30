# 🔍 Lexical Analyzer in Python

This project implements a **lexical analyzer** (lexer) in Python as part of a compiler front-end simulation. It reads a text file containing a stream of lexemes (identifiers, numbers, operators) and tokenizes them according to a set of predefined rules.

---

## 📌 Project Description

Lexical analysis is the first phase of a compiler, where raw input (text source code) is transformed into a stream of **tokens** that represent meaningful building blocks like keywords, variables, numbers, and symbols.

This lexer reads an input file, splits it into lexemes, and classifies each as:
- **INTEGER** → whole numbers (e.g., `354`, `-322`, `0`)
- **FLOAT** → decimal numbers (e.g., `3.243`, `0.003`, `-3.4`)
- **ID** → identifiers (e.g., `sum`, `big_size`, `x123`)
- **Operators**:
  - `&` → `BITWISE_AND`
  - `&&` → `LOGICAL_AND`
  - `|` → `BITWISE_OR`
  - `||` → `LOGICAL_OR`
- **ERROR** → invalid/unrecognized lexemes (e.g., `34RR`)

A **symbol table** is used to store identifiers and their indexes.

---

## 🧠 How It Works

Upon running the program:

1. The user is prompted to enter the name of the input file.
2. A menu is shown:
   - `1. Call lex()` → get the next token
   - `2. Show symbol table` → list all unique identifiers
   - `3. Exit` → quit the program
3. The `lex()` function returns a token and its associated value (number or symbol table index).
4. Tokens are printed one by one as the user continues to select `Call lex()`.

---

## 📁 Project Structure


