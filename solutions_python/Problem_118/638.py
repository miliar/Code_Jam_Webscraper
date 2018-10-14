def is_palindrome(s):
    length = len(s)
    return all(s[i] == s[length - i - 1] for i in range(length // 2))

def gen_square_pal(n):
    res = []
    for i in range(n + 1):
        if is_palindrome(str(i)) and is_palindrome(str(i * i)):
            res.append(i * i)
    return res

sq_pal = gen_square_pal(10000000)
print(sq_pal)

inf = open("c.in", "r")
ouf = open("c.out", "w")
T = int(inf.readline())
for t in range(T):
    print("Case #", (t + 1), ": ", sep="", end="", file=ouf)
    a, b = [int(i) for i in inf.readline().split()]
    res = 0
    for sp in sq_pal:
        if a <= sp <= b:
            res += 1
    print(res, file=ouf)


