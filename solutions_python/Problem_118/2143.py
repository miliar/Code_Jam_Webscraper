fsq = [1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004]

f = open("C-small-attempt0.in","r")
s = open("outout.in","w")
t = int (f.readline())
for i in range(1,t+1):
    c = 0
    a = [int(x) for x in f.readline().split()]
    for j in fsq:
        if j>=a[0] and j<=a[1]:
            c = c+1
    s.write("Case #%d: %d" % (i,c))
    if i<t:
        s.write("\n")
    
f.close()
s.close()
