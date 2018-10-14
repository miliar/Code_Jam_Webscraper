import math

input = open("fas.in" , "r")
output = open("fas.out" , "w")
cases = int(input.readline())
fas = [1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002]
for i in range(1, cases + 1):
    result = 0
    [a, b] = [int(x) for x in input.readline().split()]
    a = pow(int(a), 0.5)
    b = pow(int(b), 0.5)
    a = int(math.ceil(a))
    if(math.ceil(b) == b):
        b = int(b) + 1
    else:
        b = int(math.ceil(b))
    for f in fas:
        if f >= a and f < b:
            result = result + 1
    print "Case #" + str(i) + ": " + str(result)
    output.write("Case #" + str(i) + ": " + str(result) + "\n")
input.close()
output.close()
