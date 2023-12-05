class Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def get_priority(op):
    
    if op in ('+', '-'):
        return 1
    
    elif op in ('*', '/'):
        return 2
    
    return 0


def build_expression(expression):
    stack_nodes = []
    operators = []

    elements = expression.split()

    for element in elements:
        
        if element.isdigit() or (len(element) > 1 and element[0] == '-' and element[1:].isdigit()):
            stack_nodes.append(Node(element))
       
        elif element == "(":
            operators.append('(')
        
        elif element == ")":
            
            while operators and operators[-1] != '(':
                right = stack_nodes.pop() if stack_nodes else None
                left = stack_nodes.pop() if stack_nodes else None

                operator = Node(operators.pop())
                operator.left = left
                operator.right = right

                stack_nodes.append(operator)
            
            if operators and operators[-1] == '(':
                operators.pop()  
        else:
           
            while operators and get_priority(operators[-1]) >= get_priority(element[0]):
                right = stack_nodes.pop() if stack_nodes else None
                left = stack_nodes.pop() if stack_nodes else None

                operator = Node(operators.pop())
                operator.left = left
                operator.right = right

                stack_nodes.append(operator)
            operators.append(element[0])

    while operators:
        right = stack_nodes.pop() if stack_nodes else None
        left = stack_nodes.pop() if stack_nodes else None

        operator = Node(operators.pop())
        operator.left = left
        operator.right = right

        stack_nodes.append(operator)

    return stack_nodes[0]


def calculate_result(root):
    if not root:
        return 0

    if root.value.isdigit():
        return float(root.value)

    left = calculate_result(root.left)
    right = calculate_result(root.right)

    if root.value == "+":
        return left + right
    
    elif root.value == "-":
        return left - right
    
    elif root.value == "*":
        return left * right
    
    elif root.value == "/":
        
        if right != 0:
            return left / right
       
        else:
            print("Erro: Divisao por zero.")
            return 0

    print("Erro: Operador invalido.")
    return 0


def tree_in_order(root):
    if not root:
        return

    tree_in_order(root.left)
    print(root.value, end=' ')
    tree_in_order(root.right)


# Exemplo de uso:
expression = "3 + 4 * (2 - 1)"
root = build_expression(expression)
result = calculate_result(root)

print("Resultado:", result)
print("Árvore em ordem:")
tree_in_order(root)
