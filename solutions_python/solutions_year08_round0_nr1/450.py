
import sys

def doCase():
    search = int(lines.pop())
    s = []
    for j in xrange(search):
        s.append(lines.pop())
    q = int(lines.pop())
    currentSearches = s[:]
    curSearch = None
    count = 0
    i = 0    
    while (i < q) and (len(currentSearches) > 1):
        i += 1
        this = lines.pop()
        if this in currentSearches:
            currentSearches.remove(this)

    curSearch = currentSearches[0]
    currentSearches = s[:]
    while i < q:
        i += 1
        this = lines.pop()
        if (this == curSearch):
            currentSearches.remove(this)
            while (i < q) and (len(currentSearches) > 1):
                i += 1
                this = lines.pop()
                if this in currentSearches:
                    currentSearches.remove(this)
            curSearch =  currentSearches[0]
            count += 1
            currentSearches = s[:]

    f.write(str(count)+"\n")      

f = open(sys.argv[1])
lines = f.read().split("\n")
f.close()
f = open('G:\\google\\res.txt','w')
lines.reverse()
times = int(lines.pop())
for i in range(times):
    f.write("Case #"+str(i+1)+": ")
    doCase()
f.close()
