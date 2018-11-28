


def gogo(a,b):
    ret = 0
    store = []

    for c in range(a,b+1):
        t = []
        for k in range(1,len(str(c))):
            v = str(c)
            v = int(v[k:] + v[:k])
            if v not in t and len(str(v)) == len(str(c)) and v > c and v <= b:
                t.append(v)
                ret += 1

    return ret




s = open("c:/Users/Kevin Hulin/Downloads/C-small-attempt0.in")
#s = open("c:/Users/Kevin Hulin/Downloads/B-large.in")
#s = open("c:/Users/Kevin Hulin/Downloads/ctest.in")

s = s.readlines()

for i in range(0,len(s)):
    s[i] = s[i].replace("\n","")



t = int(s[0])


f = open("c:/Users/Kevin Hulin/Downloads/Csmall.out","w")


for i in range(1,t+1):
    v = s[i].split(" ")
    n = int(v[0])
    m = int(v[1])
    f.write("Case #" + str(i) + ": " + str(gogo(n,m)))
    if i < t:
        f.write("\n")

f.close()    
