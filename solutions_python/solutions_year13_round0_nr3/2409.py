def check(i):
    if checkSqrt(i) and checkPalin(i) and checkPalin(int(i**(0.5))):
        return True
    else:
        return False

def checkPalin(i):
    if str(i) == (str(i))[::-1]:
        return True
    else:
        return False

def checkSqrt(i):
    if ((i**(0.5))%1) > 0:
        return False
    else:
        return True
def main():
    f = open("C-small-attempt0.in",'r')
    f2 = open("output.txt",'w')

    n = int(f.readline())
    for i in range(n):
        count = 0
        limits = map(int, f.readline().split(' '))
        for j in range(limits[0], limits[1]+1):
            if check(j):
                count = count+1
        f2.write("Case #" + str(i+1) + ": " + str(count) + "\n")

    f.close()
    f2.close()

if __name__ == "__main__":
    main()
