import sys

lines = list(open("1.tst").readlines())
for line in lines:
    line = "".join(line.strip().split())
c = zip("".join(lines[:3]), "".join(lines[3:]))
c.append(('z','q'))
c.append(('q','z'))
c.sort()
code = dict(c)
#print sorted(code)


case = 1
sys.stdin.readline()
for line in sys.stdin:
    ans = ""
    for c in line.strip():
        if c in code:
            ans += code[c]
        else:
            ans += c
    print "Case #%d: %s" % (case, ans)
    case += 1


