import tokens
### Essentially the Scanner and Lexer of the compiler.

class Tokenizer():
    def __init__(self, file=None):
        self.currentLine = 0
        self.file = file
        self.tokens = []
    
    def tokenize(self):
        read_file = open(self.file, 'r')
        file_contents = read_file.readLines()
        read_file.close()
        for line in file_contents:
            # Need to read each character in for string-checks
            pass