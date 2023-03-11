a=""
operand1=""
operand2=""
operator1=""
operator2=""


while a != "=":
    a=input()
    if operator1 == "":
        if a == "*":
            operator1=a
        elif a == "/":
            operator1=a
        elif a == "+":
            operator1=a
        elif a == "-":
            operator1=a
        elif operand1=="":
            operand1=float(a)
    else:
        print(operator2)
        print(operator1)
        if operator2 == "" and a!="=":
            if a == "*":
                operator2=a
            elif a == "/":
                operator2=a
            elif a == "+":
                operator2=a
            elif a == "-":
                operator2=a
            elif operand2=="":
                operand2=float(a)
        else:
            if operator1 == "+" or operator1 =="-":
                if operator2 == "*":
                    operand2=operand2*float(a)
                    operator2=""
                elif operator2 =="/":
                    operand2=operand2/float(a)
                    operator2=""
                else:
                    if operator1 =="+":
                        operand1=operand1+operand2
                    elif operator1 =="-":
                        operand1=operand1-operand2
                        print(operand1)
                    operator1=operator2
                    operator2=""
            elif operator1 =="*":
                operand1=operand1*operand2
                operator1=operator2
                operator2=""
                operand2=float(a)
            elif operator1 =="/":
                operand1=operand1/operand2
                operator1=operator2
                operator2=""
                operand2=float(a)
print(operand1)
            
                

        