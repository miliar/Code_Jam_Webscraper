import math
def main():
    scanner = open('C-small-attempt0.in','r')
    writer = open('C-small-attempt0.out','w')
    X = 1
    T = int(scanner.readline())
    while T > 0:
        count = 0
        line = scanner.readline()
        A = int(line.split(' ')[0])
        B = int(line.split(' ')[1])
        while A <= B:
            if pal(A) and square(A):
                if pal(int(math.sqrt(A))):
                    count += 1
            A += 1
        writer.write('Case #%d: %d\n' % (X, count))
        X += 1
        T -= 1

def pal(num):
    strNum = str(num)
    i = 0
    length = len(strNum) - 1
    while i < length:
        if strNum[i] != strNum[length]:
            break
        i += 1
        length -= 1
    return i >= length

def square(num):
    return int(math.sqrt(num)) == math.sqrt(num)

if __name__ == '__main__':
    main()