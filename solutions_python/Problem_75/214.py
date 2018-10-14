
def doProb(fname, ofname):
    #do problem A given a file name
    f = open(fname, 'r');
    of = open(ofname, 'w');
    T = int(f.readline());

    output = ['Case #' + str(i) + ': '+ doStuff(f.readline().split()) + '\n' for i in xrange(1,T+1)]
    f.close();      

    of.writelines(output);
    of.close();

def doStuff(Line):    
    C = int(Line[0]);
    cmb = {};
    for i in xrange(1, C+1):
        cmb[Line[i][0:2]] = Line[i][2];
        cmb[Line[i][1]+Line[i][0]] = Line[i][2];
    D = int(Line[C+1]);
    opp = {};
    for i in xrange(C+2, C+D+2):
        if(Line[i][0] in opp):
            opp[Line[i][0]].add(Line[i][1]);
        else:
            opp[Line[i][0]] = set([Line[i][1]]);
        if(Line[i][1] in opp):
            opp[Line[i][1]].add(Line[i][0]);
        else:
            opp[Line[i][1]] = set([Line[i][0]]);

    N = int(Line[C+D+2]);
    s = Line[C+D+3];
    
    s2 = [s[0]];
    for i in xrange(1,N):
        if(len(s2)==0):
            s2 = [s[i]];
        elif((s2[-1]+s[i]) in cmb):
            s2[-1] = cmb[s2[-1]+s[i]];
        elif(s[i] in opp):
            forbidden = opp[s[i]];
            for letter in s2:
                if(letter in forbidden):
                    s2 = [];
            if(len(s2)!=0):
                s2.append(s[i])
        else:
            s2.append(s[i]);

    if(len(s2)==0):
        return '[]';
    
    ret = '[';
    for i in xrange(len(s2)-1):
        ret += s2[i] + ', ';
    ret += s2[-1];
    ret += ']';
    return ret
    
            

pf = 'C:\\Python27\\gcj11\\qual\\B';
#doProb(pf + '\\bsmall.in', pf + '\\bsmall.out')
doProb(pf + '\\blarge.in', pf + '\\blarge.out')
#doProb(pf + '\\b.in', pf + '\\b.out')

