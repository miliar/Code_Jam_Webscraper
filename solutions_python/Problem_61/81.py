limit = 501
facs = [1, 1]
table = [[0 for j in range(limit)]
            for i in range(limit)]

def int_input():
    return int(raw_input())

def combination(n, k):
    return facs[n]/(facs[k]*facs[n-k])

def do_facs():
    for i in range(2, limit):
        facs.append(facs[-1]*i)

def do_table():
    for p in range(limit):
        table[p][1] = 1
    for p in range(2, limit):
        for l in range(1, p):
            for c in range(1, l):
                spaces = l-c-1
                digits = p-l-1
                if spaces <= digits:
                    table[p][l] += table[l][c] * combination(digits, spaces)

def answer(c):
    n = int_input()
    ans = 0
    for i in table[n]:
        ans += i
    ans %= 100003
    print "Case #%d: %d" % (c, ans)

def main():
    do_facs()
    do_table()
    for c in range(int_input()):
        answer(c+1)

main()
