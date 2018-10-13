import string
import math

FILENAME = "C-small-attempt0.in"
inFile = open(FILENAME, 'r', 0)
fout = open("C_res.in", "w")
line = inFile.readline()
T = int(string.split(line)[0])

def is_palin(n):
    if len(n) <= 2:
        if n[0] == n[-1]:
            return True
        else:
            return False
    else:
        if n[0] == n[-1]:
            return is_palin(n[1:-1])
        else:
            return False

def check_n_check(n):
    if is_palin(str(n)) == True:
        if is_palin(str(n**2)) == True:
            return 1
    return 0

def sqrt_int(bound, ROUND):
    temp = math.sqrt(bound)
    if ROUND == 0:
        if int(temp) >= temp:
            temp = int(temp)
        else:
            temp = int(temp) + 1
    else:
        if int(temp) <= temp:
            temp = int(temp)
        else:
            temp = int(temp) - 1
    return temp

for t in range(T):
    res = 0
    L = []
    spec = inFile.readline()
    A = int(string.split(spec)[0])
    B = int(string.split(spec)[1])

    a = sqrt_int(A, 0)
    b = sqrt_int(B, 1)

    for i in range(a, b+1):
        res = res + check_n_check(i)

    fout.write ("Case #" + str(t+1) + ": " + str(res) + "\n")

fout.close()
