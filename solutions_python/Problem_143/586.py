import math

def foo(limit1, limit2, target):
    if max(limit1, limit2, target) == 0:
        return 1
    n = int(math.log(float(max(limit1, limit2, target)), 2)) + 1
    possible1 = []
    possible2 = []
    for i in range(limit1):
        possible1.append(decimalToVector(i, n))
    for i in range(limit2):
        possible2.append(decimalToVector(i, n))

    AND = []
    for item1 in possible1:
        for item2 in possible2:
            AND.append(vectorToDecimal(bitwiseAND(item1, item2)))
    
    counter = 0
    for item in AND:
        if item < target:
            counter += 1
    return counter
        


def bitwiseAND(item1, item2):
    output = []
    if len(item1) != len(item2):
        print("incorrect input AND")
    for i in range(len(item1)):
        if item1[i] == 1 and item2[i] == 1:
            output.append(1)
        else:
            output.append(0)
    return output




def decimalToVector(n, r):
    if n < 0 or n >= 2**(r):
        print("n is too large or less than zero.")
        return
    
    rtn = []
    for i in range(0, r):
        
        if n >= 2**(r-i-1):
            rtn.append(1)
            n -= 2**(r-i-1)
            
        else:
            rtn.append(0)
            
    return rtn


def vectorToDecimal(vector):
    rtn = 0
    for i in range(0, len(vector)):
        
        if vector[i] == 1:
            rtn += 2**(len(vector)-i-1)
            
    return rtn



file = open("B-small-attempt0.in.txt", "r")
output = open("B-small-attempt0.out.txt", "w")
T = int(file.readline())
for i in range(T):
    variables = file.readline().split(" ")
    output.write("Case #" + str(i+1) + ": " + str(foo(int(variables[0]), int(variables[1]), int(variables[2]))) + "\n")

file.close()
output.close()

