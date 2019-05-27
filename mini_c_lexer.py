# -*- encondig: utf-8 -*-

# --------------------------------------
# c minus lexer
# --------------------------------------

# NEW: 	comments in classic C
# 		comentario in C99 standard

import ply.lex as lex

# list of tokens
tokens = (

	# Reserverd words
	'SINO',
	'SI',
	'E',
	'S',
	'F',
	'AND',
	'OR',
	'MQ',
	'P',
	'H',
	
	# Symbols
	'PLUS',
	'MINUS',
	'TIMES',
	'DIVIDE',
	'POW',
	'MODULO',
	'LESS',
	'LESSEQUAL',
	'GREATER',
	'GREATEREQUAL',
	'EQUAL',
	'DEQUAL',
	'DISTINT',
	'SEMICOLON',
	'COMMA',
	'LPAREN',
	'RPAREN',
	'LBRACKET',
	'RBRACKET',
	'LBLOCK',
	'RBLOCK',

	# Others	
	'ID', 
	'NUMBER',
)

# Regular expressions rules for a simple tokens
t_PLUS    	 = r'\+'
t_MINUS	     = r'-'
t_TIMES    	 = r'\*'
t_DIVIDE 	 = r'/'
t_EQUAL      = r'='
t_POW        =r'\^'
t_MODULO     = r'\%'
t_LESS 	     = r'<'
t_GREATER    = r'>'
t_SEMICOLON  = ';'
t_COMMA	     = r','
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_LBRACKET   = r'\['
t_RBRACKET   = r'\]'
t_LBLOCK     = r'{'
t_RBLOCK     = r'}'
t_AND        = r'\&'
t_OR         = r'\|'

def t_SINO(t):
	r'SINO'
	return t

def t_SI(t):
	r'SI'
	return t

def t_E(t):
	r'E'
	return t
	
def t_S(t):
	r'S'
	return t

def t_F(t):
	r'F'
	return t
	
def t_MQ(t):
	r'MQ'
	return t
	
	
def t_P(t):
	r'P'
	return t

	
def t_H(t):
	r'H'
	return t
	
	

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_ID(t):
	r'\w+(_\d\w)*'
	return t

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_DEQUAL(t):
	r'=='
	return t

def t_DISTINT(t):
	r'!='
	return t


def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

t_ignore = ' \t'


def t_comments(t):
	r'/(.|\n)*?/'
	t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
	r'/(.)*?\n'
	t.lexer.lineno += 1

def t_error(t):
	print ("Error Lexico: " + str(t.value[0]))
	t.lexer.skip(1)



def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

# Test 
if __name__ == '__main__':

	# Test
	data = '''
		* comentario
   			de varias lineas
		*
		void main (int argc) {
			int a & 10
			a = 10;
			// Esto es otro comentario
			SINO
			SI
			F
			E
			DB
			S
            ^
           %  
			return 0;
		}
	'''

	# Build lexer and try on
	lexer.input(data)
	test(data, lexer)

