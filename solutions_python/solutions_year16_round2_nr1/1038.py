def main():
    f=open('input1.txt','r')
    n=int(f.readline())
    testcases=[]
    for i in range(n):
        t=f.readline().rstrip('\n')
        testcases.append(calculate(t))
    #print testcases
    #return
    fo=open('output1.txt','w+')
    for i in range(n):
    #    print 'Case #{0}: {1}'.format(i+1,testcases[i])
        fo.write('Case #{0}: {1} \n'.format(i+1,testcases[i]))
#    print testcases

def calculate(t):
    l=[]
    while len(t)>1:
        #print "L:",l
        #print len(t)
        #input(t)
        if 'W' in t:
            t=t.replace('T','',1)
            t=t.replace('W','',1)
            t=t.replace('O','',1)
            l.append('2');
            continue;
        if 'U' in t:
            t=t.replace('F','',1)
            t=t.replace('O','',1)
            t=t.replace('U','',1)
            t=t.replace('R','',1)
            l.append('4')
            continue;
        if 'X' in t:
            t=t.replace('S','',1)
            t=t.replace('I','',1)
            t=t.replace('X','',1)
            l.append('6')
            continue;
        if 'G' in t:
            t=t.replace('E','',1)
            t=t.replace('I','',1)
            t=t.replace('G','',1)
            t=t.replace('H','',1)
            t=t.replace('T','',1)
            l.append('8')
            continue;
        if 'Z' in t:
            t=t.replace('Z','',1)
            t=t.replace('E','',1)
            t=t.replace('R','',1)
            t=t.replace('O','',1)
            l.append('0')
            continue;
        if 'O' in t:
            t=t.replace('O','',1)
            t=t.replace('N','',1)
            t=t.replace('E','',1)
            l.append('1')
            continue;
        if 'T' in t:
            t=t.replace('T','',1)
            t=t.replace('H','',1)
            t=t.replace('R','',1)
            t=t.replace('E','',1)
            t=t.replace('E','',1)
            l.append('3')
            continue;
        if 'F' in t:
            t=t.replace('F','',1)
            t=t.replace('I','',1)
            t=t.replace('V','',1)
            t=t.replace('E','',1)
            l.append('5')
            continue
        if 'V' in t:
            t=t.replace('S','',1)
            t=t.replace('E','',1)
            t=t.replace('V','',1)
            t=t.replace('E','',1)
            t=t.replace('N','',1)
            l.append('7')
            continue;
        if 'N' in t:
            t=t.replace('N','',1)
            t=t.replace('I','',1)
            t=t.replace('N','',1)
            t=t.replace('E','',1)
            l.append('9')
    return "".join(sorted(l))

    
if __name__=="__main__":
    main()
