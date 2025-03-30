import re

class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        return f"<{self.token_type}, {self.value}>"

class Lexer:
    def __init__(self, text):
        self.tokens = self.tokenize(text)
        self.index = 0
        self.symbol_table = []

    def tokenize(self, text):
        # Split based on spaces for simplicity
        return text.split()

    def lex(self):
        if self.index >= len(self.tokens):
            return None  # No more tokens

        lexeme = self.tokens[self.index]
        self.index += 1

        # Patterns
        float_pattern = re.compile(r"^-?\d+\.\d+$")
        int_pattern = re.compile(r"^-?\d+$")
        id_pattern = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
        logical_and = "&&"
        logical_or = "||"
        bitwise_and = "&"
        bitwise_or = "|"

        if lexeme == logical_and:
            return Token("LOGICAL_AND", "nothing")
        elif lexeme == logical_or:
            return Token("LOGICAL_OR", "nothing")
        elif lexeme == bitwise_and:
            return Token("BITWISE_AND", "nothing")
        elif lexeme == bitwise_or:
            return Token("BITWISE_OR", "nothing")
        elif float_pattern.match(lexeme):
            return Token("FLOAT", float(lexeme))
        elif int_pattern.match(lexeme):
            return Token("INTEGER", int(lexeme))
        elif id_pattern.match(lexeme):
            if lexeme not in self.symbol_table:
                self.symbol_table.append(lexeme)
            return Token("ID", self.symbol_table.index(lexeme))
        else:
            return Token("ERROR", lexeme)

    def show_symbol_table(self):
        for i, ident in enumerate(self.symbol_table):
            print(f"{i}: {ident}")

def main():
    filename = input("Enter input filename: ")
    try:
        with open(filename, "r") as file:
            data = file.read()
    except FileNotFoundError:
        print("File not found!")
        return

    lexer = Lexer(data)

    while True:
        print("\n--- MENU ---")
        print("1. Call lex()")
        print("2. Show symbol table")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            token = lexer.lex()
            if token is not None:
                print(token)
            else:
                print("No more tokens.")
        elif choice == "2":
            lexer.show_symbol_table()
        elif choice == "3":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
