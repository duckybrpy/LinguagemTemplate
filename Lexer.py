import re, os

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []

    def lex(self):
        token_specification = [
            ('NUMBER', r'\d+'),
            ('STRING', r'"[^"]*"'),
            ('EQUALS', r'=='),
            ('ASSIGN', r'='),
            ('IF', r'if'),
            ('ELSE', r'else'),
            ('ELIF', r'elif'),
            ('PRINT', r'system.print'),
            ('WHILE', r'while'),
            ('FOR', r'for'),
            ('NAME', r'[A-Za-z_][A-Za-z_0-9]*'),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('LBRACE', r'\{'),
            ('RBRACE', r'\}'),
            ("PLUS", r'\+'),
            ('SKIP', r'[ \t]+'), e
            ('NEWLINE', r'\n'),  
            ('MISMATCH', r'.'),  
        ]

        master_pattern = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
        regex = re.compile(master_pattern)

        line_num = 1
        line_start = 0
        for mo in regex.finditer(self.code):
            kind = mo.lastgroup
            value = mo.group()
            if kind == 'NEWLINE':
                line_start = mo.end()
                line_num += 1

            elif kind == "STRING":
                value = value.strip('"')
            
     
            self.tokens.append((kind, value))
            
            

        return self.tokens
