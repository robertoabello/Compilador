# -*- enconding: utf-8 -*-

# Referencia: http://www.juanjoconti.com.ar/2007/11/02/minilisp-un-ejemplo-de-ply/
import ply.yacc as yacc
from mini_c_lexer import tokens
import mini_c_lexer
import sys

VERBOSE = 1
mensaje = 0	


def p_program(p):
	'program : declaration_list'
	pass

def p_declaration_list_1(p):
	'declaration_list : declaration_list declaration'
	 #p[0] = p[1] + p[2]  
	pass

def p_declaration_list_2(p):
	'declaration_list : declaration'
	pass

def p_declaration(p):
	'''declaration : var_declaration
				  | fun_declaration'''
	pass

def p_var_declaration_1(p):
	'var_declaration : type_specifier ID SEMICOLON'
	pass

def p_var_declaration_2(p):
	'var_declaration : type_specifier ID LBRACKET NUMBER RBRACKET SEMICOLON'
	pass


def p_var_declaration_3(p):
	'var_declaration : type_specifier ID COMMA ID SEMICOLON'
	pass




#---------------------------------------- 
#       TIPOS DE DATOS

def p_type_specifier_1(p):
	'type_specifier : E'
	pass

def p_type_specifier_2(p):
	'type_specifier : S'
	pass

def p_type_specifier_3(p):
	'type_specifier : F'
	pass
#----------------------------------------






def p_fun_declaration(p):
	'fun_declaration : type_specifier ID LPAREN params RPAREN compount_stmt'
	pass


def p_params_1(p):
	'params : param_list'
	pass

def p_param_list_1(p):
	'param_list : param_list COMMA param'
	pass

def p_param_list_2(p):
	'param_list : param'
	pass

def p_param_list_3(p):
	'param_list : empty'
	pass

def p_param_1(p):
	'param : type_specifier ID'
	pass

def p_param_2(p):
	'param : type_specifier ID LBRACKET RBRACKET'
	pass

def p_compount_stmt(p):
	'compount_stmt : LBLOCK local_declarations statement_list RBLOCK'
	pass

def p_local_declarations_1(p):
	'local_declarations : local_declarations var_declaration'
	pass

def p_local_declarations_2(p):
	'local_declarations : empty'
	pass

def p_statement_list_1(p):
	'statement_list : statement_list statement'
	pass

def p_statement_list_2(p):
	'statement_list : empty'	
	pass

#-----------------------------------
#          CONDICIONALES

def p_selection_stmt_1(p):
	'selection_stmt : SI LPAREN expression RPAREN statement'
	pass

def p_selection_stmt_2(p):
	'selection_stmt : SI LPAREN expression RPAREN statement SINO statement'
	pass


#-----------------------------------
#          ITERADORES

def p_iteration_stmt_1(p):
	'iteration_stmt : MQ LPAREN expression RPAREN statement'
	pass

def p_iteration_stmt_2(p):
	'iteration_stmt : H  statement  MQ LPAREN expression RPAREN'
	pass


def p_iteration_stmt_3(p):
	'iteration_stmt : P LPAREN ID EQUAL NUMBER SEMICOLON ID relop NUMBER SEMICOLON ID addop addop RPAREN statement'
	pass

#-----------------------------------

def p_statement(p):
	'''statement : expression_stmt
				| compount_stmt
				| selection_stmt
				| iteration_stmt
				
	'''
	pass

def p_expression_stmt_1(p):
	'expression_stmt : expression SEMICOLON'
	pass

def p_expression_stmt_2(p):
	'expression_stmt : SEMICOLON'
	pass

def p_expression_1(p):
	'expression : var EQUAL expression'
	pass

def p_expression_2(p):
	'expression : simple_expression'
	pass

def p_var_1(p):
	'var : ID'
	pass

def p_var_2(p):
	'var : ID LBRACKET expression RBRACKET'
	pass

def p_simple_expression_1(p):
	'simple_expression : additive_expression relop additive_expression'
	pass

def p_simple_expression_2(p):
	'simple_expression : additive_expression'
	pass

def p_relop(p):
	'''relop : LESS 
			| LESSEQUAL
			| GREATER
			| GREATEREQUAL
			| DEQUAL
			| DISTINT
			| AND
			| OR
	'''
	pass

def p_additive_expression_1(p):
	'additive_expression : additive_expression addop term'
	pass

def p_additive_expression_2(p):
	'additive_expression : term'
	pass

def p_addop(p):
	'''addop : PLUS 
			| MINUS
	'''
	pass

def p_term_1(p):
	'term : term mulop factor'
	pass

def p_term_2(p):
	'term : factor'
	pass

def p_mulop(p):
	'''mulop : 	TIMES
				| DIVIDE
	            | POW
   	            | MODULO

	'''
	pass

def p_factor_1(p):
	'factor : LPAREN expression RPAREN'
	pass

def p_factor_2(p):
	'factor : var'
	pass

def p_factor_3(p):
	'factor : call'
	pass

def p_factor_4(p):
	'factor : NUMBER' 
	pass

def p_call(p):
	'call : ID LPAREN args RPAREN'
	pass

def p_args(p):
	'''args : args_list
			| empty
	'''
	pass

def p_args_list_1(p):
	'args_list : args_list COMMA expression'
	pass

def p_args_list_2(p):
	'args_list : expression'
	pass

def p_empty(p):
	'empty :'
	pass

def p_error(p):

	
	if VERBOSE:

		if p is not None:
			print("Error de sintaxi en la linea " + str(p.lexer.lineno) + ", Token inesperado  " + str(p.value))
			mensaje = 2
		else:
			print("Error de sintaxi en la linea: " + str(mini_c_lexer.lexer.lineno))
			mensaje = 4
	else:
		print('Error', 'de sintaxi')
		
		
		

parser = yacc.yacc()

if __name__ == '__main__':

	data = ''' 
	         /variables/ 
             E a,c; 


             /Mi Programa/
            
             E main(){
       
   



            }
               
	''' 



	parser.parse(data, tracking=True)
	

