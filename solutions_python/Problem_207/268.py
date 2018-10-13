import sys


fin = sys.stdin
fout = sys.stdout
ferr = sys.stderr

T = int(fin.readline())

for case in range(T):
    l = fin.readline()
    N, R, O, Y, G, B, V = list(map(int, l.split()))
    (T,TC), (S,SC), (F,FC) = sorted([(R,'R'),(Y,'Y'),(B,'B')]) 

    AC = F-S #tyle do uzupelnienia trzecim kolorem
    if AC>T:    
        fout.write("Case #%i: IMPOSSIBLE\n" % (case+1))
        continue
    W = T-AC #tyle zostanie trzeciego koloru do powstawiania wczesniej
    P = S*2 #a tyle jest pozycji gdzie mozna powstawiac trzeci kolor   
    if W>P:
        fout.write("Case #%i: IMPOSSIBLE\n" % (case+1))
        continue

    fout.write("Case #%i: " % (case+1))
    for i in range(F):
        fout.write(FC)
        if S>0:
            if W>0:
                fout.write(TC)
                W -= 1                
            fout.write(SC)
            S -= 1
            if W>0:
                fout.write(TC)
                W -= 1                
        else:
            fout.write(TC)
    fout.write("\n")
