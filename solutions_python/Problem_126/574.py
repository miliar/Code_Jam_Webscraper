

def valid(string, n):
    ch = ['a', 'e', 'i', 'o', 'u']
    count = 0
    if len(string) < n:
        return False
    for c in string:
        if c not in ch:
            count += 1
            if count >= n:
                return 1
        else:
            count = 0
    return 0

inf= open("A-small-attempt0.in", "r")
outf = open("A.out", "w")

T = int(inf.readline())
for i in range(T):
    line = inf.readline().split(" ")
    string = str(line[0])
    n = int(line[1])
    count = 0
    data = []
    for ch in string:
        data.append(ch)
    for j in range(len(data)):
        l = len(data[j:])
        for k in range(l):
            t = l-k+j
         #   print valid(str(data[j:-k]), n)
            if valid(data[j:t], n) == 0:
                break
            else:
                count += 1
    outf.write("Case #%d: %d\n" %(i+1, count))
    
inf.close()
outf.close()
