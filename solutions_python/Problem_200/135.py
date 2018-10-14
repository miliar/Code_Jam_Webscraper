#!/usr/bin/env python3

T = int(input().strip())

def isTidy(number):
    number = list(int(i) for i in str(number))
    for i in range(len(number) - 1):
        if number[i] > number[i + 1]: #found untidy
            return False
    return True

for t in range(T):
    print("Case #{}: ".format(t + 1), end="")
    
    line = input()
    number = list(int(i) for i in line) #oh, yeah, Python
    
    for i in range(len(number) - 1):
        if number[i] > number[i + 1]: #found untidy
            while i > 0 and number[i - 1] == number[i]:
                i -= 1
            number[i] -= 1
            for j in range(i + 1, len(number)):
                number[j] = 9
    if number[0] == 0 and len(number) != 1:
        number.pop(0)
    print(''.join(str(i) for i in number))
    #solution_dut = ''.join(str(i) for i in number)
    
    ##also solve naively
    #number = int(line)
    #while not isTidy(number):
    #    number -= 1
    #if str(number) != solution_dut:
    #    print("######## {} ({})".format(number, line))

