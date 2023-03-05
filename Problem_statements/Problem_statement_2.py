def isValidParenthesis(expression):
    stack = []

    for ch in expression:
        if ch == '(' or ch == '[' or ch == '{':
            stack.append(ch)
        else:
            if stack:
                topElement = stack[-1]
                if (ch == ')' and topElement == '(' or
                        ch == ']' and topElement == '[' or
                        ch == '}' and topElement == '{'):
                    stack.pop()
                else:
                    return False
            else:
                return False

    if not stack:
        return True
    else:
        return False


if __name__ == "__main__":

    expression = input("Enter an expression: ")
    if isValidParenthesis(expression):
        print("true")
    else:
        print("false")
