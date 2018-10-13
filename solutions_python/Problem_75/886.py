# To change this template, choose Tools | Templates
# and open the template in the editor.
import os

fn = 'E:\dev\GoogleJam\src\InOut\B-large'
try: os.remove(fn+'.out')
except: pass
fout = open(fn+'.out','w')
case = 0

def main():
    f = open(fn+'.in', 'r')
    global case
    for case in range(int(f.readline())):
        seq = f.readline().strip().split(' ')
        c = int(seq.pop(0))
        comb = []
        for i in range(c):
            co = seq.pop(0)
            comb.append([co[0:2], co[2]])
            comb.append([co[1]+co[0], co[2]])
        c = int(seq.pop(0))
        opp = []
        for i in range(c):
            op = seq.pop(0)
            opp.append(op)
            opp.append(op[1]+op[0])
        l = int(seq.pop(0))
        invoke = seq.pop(0)
        res = invoke[0]

        #print comb, opp
        for i in range(l-1):
            #print res, invoke[i+1]
            if len(res) == 0:
                res = invoke[i+1]
                #print "res was empty", res
                continue
            #try to combine the last ones.
            for c in comb:
                if res[-1]+invoke[i+1] == c[0]:
                    res = res[0:-1] + c[1]
                    break
            else:
                #look for opposite sequences
                cop = [op for op in opp if op[0] == invoke[i+1]]
                for o in cop:
                    #print "opp?", o, res.find(o[1])
                    if res.find(o[1]) >= 0:
                        res= ""
                        break
                else:
                    res += invoke[i+1]
            #print "res", res


        put("["+', '.join(list(res))+"]")

def put(res):
    print res
    fout.write("Case #" + str(case+1) + ": " + str(res) + "\n")


__author__="Louis"
__date__ ="$16 avr. 2011 10:41:32$"

if __name__ == "__main__":
    main()
