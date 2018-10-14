f = open("Out.txt", "w")

def substrings(string, n):
    for start in xrange(0,len(string)):
        for end in xrange(start,len(string)+1):
            x = string[start:end]
            if len(x) >= n:
                yield x
i = 0
for e in open("In.txt", "r"):
    if i != 0:
        s, n = e.split()
        n = int(n)
        lista = []
        for e in range(0, len(s)-n+1):
            sub = s[e:n+e]
            ok = 1
            for x in sub:
                if x in ('a', 'e', 'i', 'o', 'u'):
                    ok = 0
                    break
            if ok:
                lista.append(sub)
        count = 0
        
        for e in substrings(s, n):
            for c in lista:
                if c in e:
                    count += 1
                    break
        ans = ans = "Case #" + str(i) + ": " + str(count) + "\n"
        f.write(ans)
    i += 1
f.close()
