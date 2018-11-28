import sys
from pprint import pprint
for i in range(0, int(sys.stdin.readline())):
    p=[float(s) for s in str.split(sys.stdin.readline())]
    if(p[0]>p[2]):
        a = p[2]/2
    else:
        C=p[0]
        F=p[1]
        X=p[2]
        mi=0
        ma=1000000
        while 1:
            mp=int((mi+ma)/2)
            pal = (X/(2+((mp-1)*F))) + (sum((C/(2+(ff*F))) for ff in range (0,mp-1)) if mp-1 > 0 else 0) if mp-1 >= 0 else 0
            pa = (X/(2+(mp*F))) + (sum((C/(2+(ff*F))) for ff in range (0,mp)) if mp > 0 else 0)
            par =(X/(2+((mp+1)*F))) + (sum((C/(2+(ff*F))) for ff in range (0,mp+1)) if mp+1 > 0 else 0)
            if((mi==ma) or (pal==pa or par == pa) or (par>pa and pal > pa) or (pal == 0 and par > pa)):
                a=pa
                break
            if(par<pa):
                mi=mp
                continue
            if(pal > 0 and pal<pa):
                ma = mp
                continue
            pprint(pal)
            pprint(pa)
            pprint(par)
            raise Exception('fuuuuu...')

    sys.stdout.write("Case #{:d}: {:.7f}\n".format(i+1, a))
