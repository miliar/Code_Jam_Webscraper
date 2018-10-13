k = 4
i = 2
j = 3
d = {"k": k, "i": i, "j": j}
def mult(a, b):
    global k, i, j
    sign = 1 if a*b > 0 else -1
    a = abs(a)
    b = abs(b)
    if a == 1:
        return sign*b
    if b == 1:
        return sign*a
    if a == b:
        return sign*-1
    if a == i:
        if b == j:
            return sign*k
        return sign*-j
    if a == j:
        if b == i:
            return sign*-k
        return sign*i
    if b == i:
        return sign*j
    return sign*-i

def check(s):
    global k, i, j
    #print("check starts", s)
    cur = 1
    start = 0
    while cur != i:
        if start >= len(s):
            #print("start outside")
            return False
        cur = mult(cur, s[start])
        start += 1
    end = len(s) - 1
    cur = 1
    while cur != k:
        if end < 0:
            #print("stop outside")
            return False
        cur = mult(s[end], cur)
        end -= 1
    #print(start, end)
    cur = 1
    for pos in range(start, end + 1):
        cur = mult(cur, s[pos])
    return cur == j

if __name__ == "__main__":
    t = int(input())
    for c in range(t):
        l, x = map(int, input().split())
        s = [d[el] for el in input()]
        s *= x
        print("Case #{}: {}".format(c + 1, "YES" if check(s) else "NO"))
