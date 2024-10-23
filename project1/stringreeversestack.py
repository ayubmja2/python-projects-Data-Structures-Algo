# Reverse a string using a stack.

string = "Hello, People of earth"
stack = []

#Addes elements in the stack

for i in range(len(string)):
    stack.append(string[i])
    
#if the stack is not null pop and print each letterrr
while stack:
    element = stack.pop()
    print(element, end= '')
