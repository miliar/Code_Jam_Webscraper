inp = "A-large"
inpin = inp+".in"
inpout = inp+".out"

txt = open(inpin).readlines()
txt = [x.strip() for x in txt]

txt.pop(0)

cases = []
while txt:
    txt.pop(0)
    x = [int(i) for i in txt.pop(0).split()]
    y = [int(i) for i in txt.pop(0).split()]
    cases.append( (x,y) )

f = open(inpout, "w")
for num, (x, y) in enumerate(cases):
    x = sorted(x)
    y = sorted(y)
    y.reverse()

    f.write( "Case #"+str(num+1)+": "+str(sum([x[i]*y[i] for i in xrange(len(x))])) + "\n")
f.close()
