from stack2 import Stack2


def is_balanced(text):
    stack = Stack2()
    for char in text:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()


print(is_balanced("(())()"))  # true
print(is_balanced("())("))  # false