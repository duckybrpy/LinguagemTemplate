class Interprete:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

        self.variables = {}
        self.functions = {}
        pass

    def parser(self):
        while self.pos < len(self.tokens):
            token, value = self.tokens[self.pos]
            print(token, " -> ", value, self.pos)
            if token == 'NAME':
                self.handler_name()

            elif token == 'PRINT':
                self.handler_print()

            elif token == "IF":
                self.handler_if()

            else:
                self.pos += 1

    #PRINT
    def handler_print(self):
        token, value = self.next_token()
    
        if token == "LPAREN":
            token, value = self.next_token()
            result = self.evaluate()
            print(result)

            if token == "RPAREN":
                self.next_token()


        self.next_token()


    # CONFIGURAR VARIAVEIS
    def handler_name(self):
        token, value = self.tokens[self.pos]
        
        if token == "NAME":
            var_name = value
            token, value = self.next_token()
                
            if token == "ASSIGN":
                token, value = self.next_token()
                
                if token == "STRING":
                    self.variables[var_name] = value
                    


        self.next_token()


    #AVANÇAR O PROXIMO TOKEN
    def next_token(self, skip = True):
        if skip == True:
            while self.pos < len(self.tokens) - 1:
                self.pos += 1
                token, value = self.tokens[self.pos]
                #PULAR O TOKEN SKIP
                if token == "SKIP":
                    continue

                return token, value
        else:
            #SO AVANÇA MESMO
            self.pos += 1
            token, value = self.tokens[self.pos]

            return token, value
    
    def handler_if(self):
        condition = False
        while self.pos < len(self.tokens):
            token, value = self.tokens[self.pos]
    
            if token == "IF" or token == "ELIF":
                token, value = self.next_token()
                print(token, " ->", value, " IF", self.pos)
                if token == "LPAREN":
                    self.pos += 1
                    print(token, " ->", value, " IF", self.pos)
        
                    c = self.conditions()

                    if c and not condition:
                        condition = True
                        self.next_token(skip=True)
                        
                        self.exec_block()
                    else:
                        self.skip_block()
                
                self.next_token()
                    
            
            elif token == "ELSE":
                self.exec_block()
            
            else:
                self.skip_block


        pass


    # VERIFICAR AS CONDICOES
    def conditions(self):
        l = self.get_value()

        token, operator = self.next_token()
        print(token, "--> ", operator, "if", self.pos)
        self.next_token()

        v = self.get_value()
        

        if operator == "==":
            return l == v
        
        elif operator == "!=":
            return l != v
        
        elif operator == ">":
            return l > v
        
        elif operator == "<":
            return l < v
        
        elif operator == ">=":
            return l >= v
        
        elif operator == "=<":
            return l <= v
        
        
        return False


    # FAZER A EXECUCAO DO BLOCO
    def exec_block(self):
        while self.pos < len(self.tokens):
            token, value = self.tokens[self.pos]
            if token == "RBRACE":
                self.pos += 1
                break

            elif token == "NAME":
                self.handler_name()
            
            elif token == "PRINT":
                self.handler_print()
            
            self.next_token(skip=False)

    # PUKAR O BLOCK DE EXECUÇAO
    def skip_block(self):
        while self.pos < len(self.tokens):
            token, value = self.tokens[self.pos]

            if token == "RBRACE":
                self.pos += 1
                break

            self.pos += 1

    def get_value(self):
        token, value = self.tokens[self.pos]
        print(token, "-->", value, "GET", self.pos)
        if token == "NUMBER":
            return int(value)

        elif token == "STRING":
            return value
        
        elif token == "NAME":
            return self.variables.get(value, None)
        
        return False

    
    #CONCATENAR
    def evaluate(self):
        result = ""
        while self.pos < len(self.tokens):
            token, value = self.tokens[self.pos]
            if token == "STRING":
                result += value
                print(token, " -> PRINT")
                self.pos += 1
            elif token == "NAME":
                token, value = self.tokens[self.pos]
                print(token, " -> PRINT")
                result += self.variables[value]
                self.pos += 1

            elif token == "RPAREN":
                break

            elif token == "SKIP":
                self.pos += 1

            else:
                self.pos += 1

        return result


