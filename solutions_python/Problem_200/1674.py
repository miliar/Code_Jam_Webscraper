import sys
import math

def main():
    total = int(sys.stdin.readline())
    for i in range(total):
        line = sys.stdin.readline()
        result = find_tidy(line.rstrip())
        print ('Case #{}: {}'.format(i + 1, result))

def find_tidy(string):
    length = len(string)
    asc = 0
    nondesc = 0
    for i in range(1, length):
        if int(string[i - 1]) < int(string[i]):
            asc = nondesc = i
        elif int(string[i - 1]) == int(string[i]):
            nondesc = i
        else:
            break
    
    if nondesc == length - 1:
        return int(string)
    else:
        base = string[:asc + 1]
        base = int(base) if (base != '') else 1
        n = base * int(math.pow(10, length - asc - 1))
        return n - 1
        
if __name__ == '__main__':
    main()