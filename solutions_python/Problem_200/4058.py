# str to list of int and reverse
def strToLint(s):
    result = []
    c = 0
    for d in s:
        c += 1
        result.insert(0, int(d))
    return [c, result]

def lintToStr(l, li):
    result = 0
    for i in range(l):
        result += li[i] * (10**i)
    return str(result)

def checkAndUpdate(l, n):
    for i in range(l-1):
        if n[i] < n[i+1]:
            n[i] = 9
    return n

def main():
    T = int(input())
    for t in range(0, T):
        l, n = strToLint(input())
        for i in range(0, l-1):
            while (n[i+1] > n[i]) or (n[i] == 0 and n[i+1] == 0):
                n[i] -= 1
                if n[i] < 0:
                    n[i+1] -= 1
                    n[i] = 9
        n = checkAndUpdate(l, n)
        # n.reverse()
        # print('n: ', n)
        x = lintToStr(l, n)
        # transform n to string
        print("Case #" + str(t+1) + ": " + x)

if __name__ == '__main__':
    main()
