import math

def findDigit(number, n):
    return number // 10**n % 10

def isTidy(n):
    if n < 10:
        return True

    i = 0

    for i in range(int(math.log10(n))):
        if (findDigit(n, i) < findDigit(n, i + 1)):
            return False
    return True


def findTidy(n):

    i = 0
    while not isTidy(n):
        n = n - (n%pow(10,i+1) + 1)
        i = i + 1
    return n


fin = open("B-large.in",'r')
fout = open("output_b.out",'w')

testcases_number = int(fin.readline())

for i in range(testcases_number):
    n = int(fin.readline())
    fout.write("Case #" + str(i+1) + ": " + str(findTidy(n)) + "\n")

fin.close()
fout.close()
