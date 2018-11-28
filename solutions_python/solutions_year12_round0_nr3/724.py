def solve():
    A, B = map(int, raw_input().split(' '))
    total = set({})
    def getPair(n):
        ndigits = str(n)
        for i in range(1, len(ndigits)):
            num = int(ndigits[-i:] + ndigits[:-i])
            if num <= B and num >= A and num != n:
                if (n,num) not in total:
                    total.add((n,num))
                    total.add((num, n))
    for i in range(A, B):
        getPair(i)
    return len(total) / 2


if __name__ == '__main__':
    t = int(raw_input())
    for case in range(1, t+1):
        print("Case #{0}: {1}".format(case, solve()))


