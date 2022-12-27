from enum import Enum, auto
class TokenType(Enum):
    # UNIVERSAL OPERATORS
    EQUALS = auto()
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    DOT = auto()
    COMMA = auto()
    SEMICOLON = auto()
    COLON = auto()
    RIGHT_ARROW = auto()
    QUESTION_MARK = auto()

    # LOGICAL OPERATORS
    EQUALS_EQUALS = auto()
    NOT_EQUALS = auto()
    GREATERTHAN = auto()
    LESSTHAN = auto()
    GREATERTHAN_EQUALS = auto()
    LESSTHAN_EQUALS = auto()
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    MODULO = auto()
    PLUS_PLUS = auto()
    MINUS_MINUS = auto()
    DIVIDE_DIVIDE = auto()
    MULTIPLY_MULTIPLY = auto()
    BANG = auto()

    # BITWISE OPERATORS
    OR = auto()
    XOR = auto()
    NOR = auto()
    XNOR = auto()
    AND = auto()
    NAND = auto()
    NOT = auto()
    R_SHIFT = auto()
    L_SHIFT = auto()

    # KEYWORDS:
    UINT8 = auto()
    UINT16 = auto()
    UINT32 = auto()
    UINT64 = auto()
    INT8 = auto()
    INT16 = auto()
    INT32 = auto()
    INT64 = auto()
    FLOAT32 = auto()
    FLOAT64 = auto()
    STRING = auto()
    CHAR = auto()
    BOOL = auto()
    CLASS = auto()
    STRUCT = auto()
    NULL = auto()
    VAR = auto()

    # FOR NON-KEYWORDS
    IDENTIFIER = auto()
    LITERAL = auto()

    def __repr__(self):
        return "<%s.%s>" % (self.__class__.__name__, self._name_)

class Token():
    value = None
    type = TokenType.NULL
    
    def __init__(self, value=None, type=TokenType.NULL):
        self.value = value
        self.type = type

    def __repr__(self):
        return f"{self.type} : {self.value}"