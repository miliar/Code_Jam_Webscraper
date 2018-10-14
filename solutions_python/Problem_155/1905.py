fin = open("data.in", "r")
fout = open("data.out", "w")
data = fin.readlines()
for j, e in enumerate(data[1:]):
    s = 0
    m = 0
    for i, x in enumerate(e[2:-1]):
        x = int(x)
        if x:
            m = max(m, i-s) 
            s+=x
    fout.write("Case #%d: %d\n" %(j+1, m))
