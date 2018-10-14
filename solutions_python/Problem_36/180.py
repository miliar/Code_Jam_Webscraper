import sys

def main():
    message = 'welcome to code jam'
    line = sys.stdin.readline().strip()
    values = line.split()
    for inputNum in range(int(values[0])):
        input = sys.stdin.readline().strip()
        found = find(input, message)
        print 'Case #%d: %04d' % (inputNum + 1, found % 10000)       

def find(input, message):
    m = len(input)
    n = len(message)
    s = {}
    for i in range(m + 1):
        for j in range(n + 1):
            if j == 0:
                s[i, j] = 1        
            else:
                s[i, j] = 0   
    for j in range(1, n + 1):
        sum = 0
        for i in range(1, m + 1):
            if input[i - 1] == message[j - 1]:
                sum += s[i, j - 1]
            s[i, j] = sum   
    return s[m, n]

if __name__ == "__main__":
    main()
