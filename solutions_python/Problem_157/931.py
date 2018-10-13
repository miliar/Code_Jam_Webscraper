def readline():
    return input().split(' ')
    
def to_num(l):
    return list(map(int, l))
    
def main():
    T = to_num(readline())[0]
    for t in range(T):
        print('Case #{}: {}'.format(t + 1, task()))

def task():
    global mem
    mem = {}
    l, x = to_num(readline())
    s = readline()[0] * x
    n = len(s)
    if test(s, 0, n) != ("1", -1):
        return "NO"
    for i in range(0, n):
        for j in range(i + 1, n):
            if (test(s, 0, i) == ("i", 1) and
                test(s, j, n) == ("k", 1) and
                test(s, i, j) == ("j", 1)):
                    return "YES"
    return "NO"

mem = {}

def test(s, st, ed):
    global mem
    if (st, ed) in mem:
        return mem[st, ed]
    lst = s[st:ed]
    val = "1"
    sign = 1
    for i, v in enumerate(lst):
        res = mult[val, v]
        val = res[0]
        sign *= res[1]
        mem[st, st + i + 1] = (val, sign)
    if (st, ed) in mem:
        return mem[st, ed]
    else:
        mem[st, ed] = (val, sign)
        return mem[st, ed]
    
mult = {}
mult["1", "1"] = ("1", 1)
mult["i", "1"] = ("i", 1)
mult["j", "1"] = ("j", 1)
mult["k", "1"] = ("k", 1)

mult["1", "i"] = ("i", 1)
mult["i", "i"] = ("1", -1)
mult["j", "i"] = ("k", -1)
mult["k", "i"] = ("j", 1)

mult["1", "j"] = ("j", 1)
mult["i", "j"] = ("k", 1)
mult["j", "j"] = ("1", -1)
mult["k", "j"] = ("i", -1)

mult["1", "k"] = ("k", 1)
mult["i", "k"] = ("j", -1)
mult["j", "k"] = ("i", 1)
mult["k", "k"] = ("1", -1)

main()