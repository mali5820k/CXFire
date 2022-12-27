from tokens import TokenType

class Parser():
    def __init__(self, tokens=[]):
        self.tokens = tokens
        # If a specific token type doesn't have a parsing rule, then throw an error or ignore it if appropriate by handling it with other means
        # Also, define a power of binding for specific operator to auto-determine precedence.
        self.parsing_rules = {  TokenType.PLUS: self.infix_expression,
                                TokenType.MINUS: self.prefix_expression,
                                TokenType.MULTIPLY: self.infix_expression,
                                TokenType.DIVIDE: self.infix_expression,
                                TokenType.MODULO: self.infix_expression,
                                
                                TokenType.PLUS_PLUS: self.mixfix_expression,
                                TokenType.MINUS_MINUS: self.mixfix_expression,
                                TokenType.MULTIPLY_MULTIPLY: self.mixfix_expression,
                                TokenType.DIVIDE_DIVIDE: self.mixfix_expression,
                            }
        self.class_table = {}
        #self.functions_table = {"sample_function": [name="", declared=false, parameters_list=[TokenType.UINT8, TokenType.INT64]]}
        #self.variables_table = {"sample": [value=20, declared=false]}

    def prefix_expression(self):
        
        pass

    def infix_expression(self):
        pass

    def postfix_expression(self):
        pass

    def mixfix_expression(self):
        pass
