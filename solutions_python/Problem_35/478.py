def getint(f):
    return int(f.readline().strip())

def getstr(f):
    return f.readline().strip()

def getarr(f):
    s=f.readline().strip().split()
    for i in range(len(s)):
        s[i]=int(s[i])
    return s

def convtime(t):
    (h, m) = t.split(":")
    return int(h) * 60 + int(m)