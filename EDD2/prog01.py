from prog02 import build_expression 
from prog02 import calculate_result

variables = {}

def is_number(s):
    try:
        float(s)
        return True
    
    except ValueError:
        return False

def is_variable(var):
    return var in variables

def is_operator(op):
    return op in ['+', '-', '*', '/']

def valid_expression(input_expr):
    correct = []
    parentheses_count = 0

    elements = input_expr.split()
    
    for element in elements:
        
        if element:
            
            if is_number(element) or is_operator(element):
                correct.append(element)
            
            elif is_variable(element):
                correct.append(variables[element])
            
            elif element == '(':
                parentheses_count += 1
                correct.append(element)
           
            elif element == ')':
                
                if parentheses_count > 0:
                    parentheses_count -= 1
                    correct.append(element)
                
                else:
                    return "ERRO1"
            
            else:
                return "ERRO1"

    if parentheses_count != 0:
        return "ERRO2"

    return ' '.join(correct)

def evaluation_variable(input_expr):
    pos = input_expr.find("=")
    var = input_expr[:pos].strip()
    value = input_expr[pos + 1:].lstrip()

    if any(c in "+-*/()" for c in value):
        test = valid_expression(value)
        
        if test == "ERRO1":
            print("Erro: Valor inválido encontrado.")
       
        elif test == "ERRO2":
            print("ERRO: Parênteses desbalanceados.")
        
        else:
            raiz = build_expression(test)
            result = calculate_result(raiz)
            variables[var] = str(result)
    
    else:
        variables[var] = value

def evaluation(input_expr):
    
    if '=' in input_expr:
        evaluation_variable(input_expr)
   
    elif input_expr in variables:
        print(variables[input_expr])
    
    else:
        test = valid_expression(input_expr)
        
        if test == "ERRO1":
            print("Erro: Valor inválido encontrado.")
        
        elif test == "ERRO2":
            print("ERRO: Parênteses desbalanceados.")
        
        else:
            raiz = build_expression(test)
            print(calculate_result(raiz))

evaluation("x = 3 + 4 * (2 - 1)")
evaluation("y = x + 2")
evaluation("y")
