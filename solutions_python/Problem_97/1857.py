from sys import exit


def sumDigits(n):
    sum = 0
    for i in range(len(str(n))):
        sum += int(str(n)[i])
    return sum

def findRecycled(a, b):
    count = 0
    for n in range(a, b):
        for m in range(n+1, b+1):
            if(sumDigits(n) == sumDigits(m)):
                for i in range(1, len(str(n)) + 1):
                    num = str(n)
                    num = num[i:] + num[:i]
                    if len(str(int(num))) == len(str(m)) and int(num) == m:
                        count+=1
    return count


def main():
    f = open('dancingoutput.txt', '+w')
    for i in range(int(input())):
        a,b = tuple(map(int, input().split()))
        f.write('Case #' + str(i + 1) + ': ' + str(findRecycled(a,b)) + '\n')
        

if __name__ == '__main__':
    exit(main())
    


