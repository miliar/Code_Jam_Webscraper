pairs = {'Q':2,'W':3,'E':5,'R':7,'A':11,'S':13,'D':17,'F':19}

def run():
    f=open("other.in")
    g=open("out.txt",'w')
    num = int(f.readline())
    for i in range(num):
        g.write("Case #%d: " % (i+1))
        case = f.readline().split()
        combos={}
        opps = []
        base=1
        for j in range(int(case[0])):
            triple = case[j+base]
            combos[pairs[triple[0]]*pairs[triple[1]]]=triple[2]
        base=int(case[0])+2
        for j in range(int(case[base-1])):
            double = case[j+base]
            opps.append(pairs[double[0]]*pairs[double[1]])
        es = []
        last=1
        for c in case[-1]:
           es.append(c)
           if len(es)<2:
               continue
           if es[-2] in pairs:
               prod = pairs[es[-1]]*pairs[es[-2]]
               if prod in combos:
                   es = es[:-2]
                   es.append(combos[prod])
                   continue
           simple = [x for x in es if x in pairs]
           for k in opps:
               if k in [pairs[c]*pairs[d] for d in simple]:
                   es = []
                   break
        g.write("[")
        for h in range(len(es)):
            if (h!=0):
                g.write(", ")
            g.write(es[h])
        g.write("]\n")
    f.close()
    g.close()
    
