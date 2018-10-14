# To change this template, choose Tools | Templates
# and open the template in the editor.
import os

fn = 'E:\dev\GoogleJam\src\InOut\A-large'
try: os.remove(fn+'.out')
except: pass
fout = open(fn+'.out','w')
case = 0

def average(v):
    return sum(v, 0.0) / len(v)

def main():
    f = open(fn+'.in', 'r')
    global case
    for case in range(int(f.readline())):
        team = []
        team_nb = int(f.readline())
        for l in range(team_nb):
            team.append([f.readline().strip()])
            team[-1].append( average( map(int,list(str(team[-1][0]).replace(".","")))) ) 

        for tn in range(len(team)):
            opp = []
            t = team[tn]
            for i in range(team_nb):
                if t[0][i] != ".":
                    opps = list(team[i][0])
                    opps.pop(tn)
                    opps = ''.join(opps)
                    opp.append( average( map(int,list(str(opps).replace(".","")))) )
            t.append(average(opp))

        res = []
        for t in team:
            oopp = []
            for i in range(team_nb):
                if t[0][i] != ".":
                    oopp.append(team[i][2])
            t.append(average(oopp))
            res.append( str(0.25 * t[1] + 0.50*t[2] + 0.25 * t[3]) )

        put("\n"+"\n".join(res))

def put(res):
    print res
    fout.write("Case #" + str(case+1) + ": " + str(res) + "\n")


__author__="Louis"
__date__ ="$16 avr. 2011 10:41:32$"

if __name__ == "__main__":
    main()
