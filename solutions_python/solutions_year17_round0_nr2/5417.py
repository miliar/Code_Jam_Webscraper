import sys

name = "B"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

def isTidy(numero):
    digitos = str(numero)
    res = True
    for i in range(len(digitos)-1):
        if digitos[i] > digitos[i+1]:
            res = False
    return res

for testCase in range(1, testCases + 1):
    line = input().split()
    numero = int (line[0])
    
    while (not isTidy(numero)):
        numero = numero - 1
    
    res = numero

    print("Case #" + str(testCase) + ": " + str(res))
