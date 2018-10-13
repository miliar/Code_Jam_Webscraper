import sys

s1 = ["a zoo",
"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"]

t1 = ["y qee",
"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"]

def translate(m, s):
    o = []
    for l in s:
        o.append(m[l])
    return "".join(o)

def main():
    s = "".join(s1)
    t = "".join(t1)
    z = zip(t, s)
    z.sort()
    m = dict(z)
    vals = m.values()
    for l in 'qwertyuiopasdfghjklzxcvbnm':
        if not m.has_key(l):
            uk = l
        if vals.count(l) == 0:
            uv = l
    m[uk] = uv

    #print m
    m['\n'] = '\n'
    sys.stdin.readline()
    i = 0
    while True:
        line = sys.stdin.readline()
        #line = "y qee"
        if line == '':
            break
        i += 1
        sys.stdout.write("Case #%d: " % i + translate(m, line))

main()
