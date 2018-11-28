import time
start = time.time()
f = open('B-large.in','r')
n = int(f.readline())
i=0
while i<n:
    ln = f.readline()
    d = ln.split()
    c = {}
    cp = []
    opp = {}
    j=0
    cimax = int(d[j])
    j+=1
    ci = 0
    while ci<cimax:
        ci+=1
        key = d[j][:2]
        if d[j][0]>d[j][1]:
            key = d[j][1]+d[j][0]
        c[key] = d[j][2]
        j+=1
    opimax = int(d[j])
    j+=1
    opi = 0
    while opi<opimax:
        opi+=1
        x = d[j][0]
        y = d[j][1]
        if not opp.has_key(x):
            opp[x] = []
        if not opp.has_key(y):
            opp[y] = []
        opp[x] += [y]
        opp[y] += [x]
        j+=1

    cno = d[j]
    j+=1
    m = d[j]
    sol = 'Case #'+str(i+1)+': ['
    elements = []
    for char in m:
        ell = len(elements)
        if ell==0:
            elements+=char
        else:
            test = char + elements[-1]
            if char>elements[-1]:
                test = elements[-1] + char
            if c.has_key(test):
                elements[-1] = c[test]
            else:

                if opp.has_key(char):
                    destro = False
                    for de in opp[char]:
                        if de in elements:
                            destro = True
                    if destro:
                        elements = []
                    else:
                        elements+= char
                
                else:
                    elements+=char
                    
   
    ccc = 0
    for c in elements:
        if ccc>0:
            sol += ", "
        sol += c
        ccc = 1
    sol += ']'
    print sol
    i+=1
f.close()
