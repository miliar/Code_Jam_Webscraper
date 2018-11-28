import os.path
import sys

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
filepath = os.path.abspath(os.path.join(__location__, "B-large.in"))
f = open(filepath, "r")
filepath = os.path.abspath(os.path.join(__location__, "out.txt"))
fo = open(filepath, 'w')

T=int(f.readline())

for Case in range(0,T):
    tmp=f.readline()
    tmp2=tmp.split()
    C=float(tmp2[0])
    F=float(tmp2[1])    
    X=float(tmp2[2])
    if (C >= X):
        fo.write ("Case #" + str(Case+1) + ": " + "{:.7f}".format(X/2) + "\n")
    else:      
        Crate=2;
        Ttime=0
        while True:
            Crate2=Crate + F
            Ftime1=X/Crate
            Ftime2=C/Crate + X/Crate2
            if (Ftime1<=Ftime2):
                fo.write ("Case #" + str(Case+1) + ": " + "{:.7f}".format(Ttime + Ftime1) + "\n")
                break
            Ttime = Ttime + C/Crate
            Crate=Crate2    
f.close()
fo.close()