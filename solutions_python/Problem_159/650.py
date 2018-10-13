f = open("a.in", "rU")
def ri():#int
    return int(f.readline().strip())
def rl(sep=False):#list of string
    if not sep:
        return f.readline().split()
    return f.readline().split(sep)
def rli(sep=False):#list of int
    return [int(i) for i in rl(sep)]

cases = ri()####
out = ""####
for case in range(cases):####
    n = ri()
    m = rli()
    one_eaten = 0
    two_rate = 0
    for i in range(1,n):
        if m[i] < m[i-1]:
            one_eaten += m[i-1] - m[i]
            if m[i-1] - m[i] > two_rate:
                two_rate = m[i-1] - m[i]
    two_current = m[0]
    two_eaten = 0
    for i in range(1,n):
        two_eaten += min(two_current, two_rate)
        two_current = m[i]
    out += "Case #{}: {} {}\n".format(case+1, one_eaten, two_eaten)####
f.close()####
out = out.strip()####
o = open("a.out", "w")####
o.write(out)####
o.close()####