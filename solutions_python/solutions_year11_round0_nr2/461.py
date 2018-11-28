# Google Code Jam : Qualification Round 2011 : Problem B. Magicka
# https://code.google.com/codejam/contest/dashboard?c=975485#s=p1
# Python 2.6.5

def format_list(l):
    s = "["
    for e in l:
        s += str(e) + ", "
    if (len(s) > 1):
        s = s[:-2]
    s += "]"
    return s


def simulate_invoke(combine, destroy, invoke):
    l = ""
    for e in invoke:
        l += e
        if len(l) < 2:
            continue
        
        for c in combine:
            if (l[-2] == c[0] and l[-1] == c[1]) or (l[-2] == c[1] and l[-1] == c[0]):
                l = l[:-2]
                l += c[2]
                break

        for d in destroy:
            if l.find(d[0]) != -1 and l.find(d[1]) != -1:
                l = ""
                break

    return l


def solve_case(t, case_str):
    combine = []
    destroy = []
    invoke = ""
    
    splitted_str = case_str.split()

    c = int(splitted_str[0])
    for i in range(0 + 1, c + 1):
        combine.append(splitted_str[i])

    d = int(splitted_str[1 + c])
    for i in range(1 + c + 1, 1 + c + d + 1):
        destroy.append(splitted_str[i])

    invoke = splitted_str[-1]

    result = simulate_invoke(combine, destroy, invoke)
    print "Case #" + str(t) + ": " + format_list(result)


def solve():
    T = int(raw_input())
    for t in range(1, T + 1):
        solve_case(t, raw_input())

solve()
