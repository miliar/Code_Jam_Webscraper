def isTidy(num):
    numStr = str(num)
    for n in range(0, len(numStr)-1):
        if int(numStr[n]) > int(numStr[n+1]):
            return False
    return True

def findTidy(num):
    for n in range(num, 0, -1):
        if isTidy(n):
            return str(n)

def main():
    f1 = open('in.txt', 'r')
    f2 = open('out.txt', 'w')
    t = int(f1.readline())
    for n in range(0, t):
        header = 'Case #' + str(n+1) + ': '
        f2.write(header + findTidy(int(f1.readline())) + '\n')
main()