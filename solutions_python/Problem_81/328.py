'''
Created on May 21, 2011

@author: cihancimen
'''

def test_case(num):
    tnum = int(raw_input())
    wp = {}
    owpd = {}
    owp = {}
    mc = {}
    mb ={}
    oowp ={}
    rsi = {}
    for team in range(tnum):
        owpd[team] = {}
        owp[team] = 0
        scores = raw_input()
        sum = 0.0
        mc[team] = 0
        mb[team] = {}
        oowp[team] = 0
        for i in range(len(scores)):
            if(scores[i] == '1'):
                sum += 1
                mc[team] +=1
                mb[team][i] = True
            elif(scores[i] == '0'):
                mc[team] +=1
                mb[team][i] = True
#        print sum / (tnum -1)
        wp[team] = sum / (mc[team])
        for t2 in range(tnum):
            if(t2 != team):
#                print team, t2
                owpn = (sum - (1 if scores[t2] == '1' else 0))
                owpnc = mc[team] - (1 if t2 in mb[team] else 0 )
#                print team, t2, owpn
                owpd[team][t2] =  owpn / owpnc
#                owp[team][t2] = 'a'
#        print team, owpd[team]
#        for k in owpd[team].values():
#            owp[team] = owp[team] + k
#        owp[team] = owp[team] / len(owpd) 
#    print mc
    for team in range(tnum):
        c = 0
        for t2 in range(tnum):
            if(team != t2 and t2 in mb[team]):
                owp[team] += owpd[t2][team]
                c += 1
        owp[team] /= c
    for team in range(tnum):
        c = 0
        for t2 in range(tnum):
            if(team != t2 and t2 in mb[team]):
                oowp[team] += owp[t2]
                c += 1
        oowp[team] /= c
    for team in range(tnum):
        rsi[team] = 0.25 * wp[team] + 0.5 * owp[team] + 0.25 * oowp[team]
#    print wp
#    print owpd
#    print owpd
#    print owp
#    print oowp
    print "Case #%d:" % (num + 1) 
    for k in rsi.values():
        print k

if __name__ == '__main__':
    num_test = int(raw_input())
    for n in range(num_test):
        test_case(n)