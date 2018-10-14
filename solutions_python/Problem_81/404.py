import sys

def rpi(WP,OWP, OOWP):
    return 0.25 * WP + 0.50 * OWP + 0.25 * OOWP

def solve(l):
    wp = []
    for i in l:
        wp.append((len([j for j in i if j == '1'])*1.0)/len([j for j in i if j in ['1','0']]))

    owp = []
    c = 0
    for i in l:
        index = 0
        index_list = []
        for j in i:
            if j in ['1','0']:
                index_list.append(index)
            index += 1
        per = []
        for index in index_list:
            win = 0
            lost = 0
            opp_team = l[index]
            for k in range(len(opp_team)):
                if k != c and opp_team[k] == '1':
                    win += 1
                if k != c and opp_team[k] == '0':
                    lost += 1
            #print index, win, lost
            per.append(win*1.0/(win+lost))
        c += 1
        #print per
        owp.append((1.0/len(per))*(sum(per)))
        
        
    oowp = []
    for i in l:
        o = []
        for j in range(len(i)):
            if i[j] in ['1','0']:
                o.append(owp[j])
        oowp.append(float(sum(o)) / len(o))
        
    ret = []
    for i in range(len(wp)):
        r = round(rpi( wp[i], owp[i], oowp[i] ),12)
        print r
        ret.append( r )
    return ret
    
    
filename = sys.argv[1]
f = open(filename, 'r')
case = 1
count = 0
outputs = []
f.readline()
c = int(f.readline())
count = int(c)
while c:
	l = []
	for i in range(c):
		l.append(f.readline())
	print 'Case #'+str(case)+':'
	solve(l)
	case += 1
	c = int(f.readline())
	
