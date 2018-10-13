import sys
import math

def isFairAndSquare(n):
    if n < 10 and math.sqrt(n) - int(math.sqrt(n)) == 0:
        return True
    else:
        num = str(n)
        if num == num[::-1] and math.sqrt(n) - int(math.sqrt(n)) == 0:
            sqrt = str(int(math.sqrt(n)))
            if sqrt == sqrt[::-1]:
                return True
        else:
            return False

def countFairAndSquare(a, b, case):
    count = 0
    for i in range(a, b):
        if isFairAndSquare(i):
            count += 1
    return "Case #{0}: {1}".format(case, count)


if __name__ == "__main__":
    input = open("C-small-attempt0.in")
    output = open("ouput.txt", "w")
    t = input.readline()
    for i in range (1, int(t) + 1):
        line = input.readline()
        args = line.split(' ')
        output.write(countFairAndSquare(int(args[0]), int(args[1]) + 1, i) + "\n")
    input.close()
    output.close()



