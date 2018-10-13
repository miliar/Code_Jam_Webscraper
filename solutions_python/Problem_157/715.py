InFile = open('C-small-attempt0.in','r')
OutFile = open('Output.out','w')

T = int(InFile.readline().rstrip('\n'))

def multQuat(a,b,s):
    if a == '1':
        return (s,b)   
    elif b == '1':
        return (s,a)
    elif a == b:
        return (-1*s,'1')
    
    elif a == 'i':
        if b == 'j':
            return (s,'k')
        else:
            return (-1*s,'j')
        
    elif a == 'j':
        if b == 'i':
            return (-1*s,'k')
        else:
            return (s,'i')
        
    elif a == 'k':
        if b == 'i':
            return (s,'j')
        else:
            return (-1*s,'i')





for i in range(T):

    line = [int(x) for x in InFile.readline().rstrip('\n').split(' ')]
    L = int(line[0])
    X = int(line[1])
    sizeString = L*X

    string = InFile.readline().rstrip('\n')
    longstring = ''
    for j in range(X):
        longstring = longstring + string

    a0 = '1'
    s0 = 1
    
    a1 = '1'
    s1 = 1
    
    a2 = '1'
    s2 = 1
    stage = 1
    
    for k in range(sizeString):
        if stage == 1:
            (s0,a0) = multQuat(a0,longstring[k],s0)
            if(a0 == 'i'):
                print(k)
                stage = 2
        elif stage == 2:
            (s1,a1) = multQuat(a1,longstring[k],s1)
            if(a1 == 'j'):
                print(k)
                stage = 3
        else:
            (s2,a2) = multQuat(a2,longstring[k],s2)

    if (s0*s1*s2 == -1)or(a2 != 'k'):
        OutFile.write('Case #'+str(i+1)+': NO\n')
    else:
        OutFile.write('Case #'+str(i+1)+': YES\n')



InFile.close()
OutFile.close()





    
#OutFile.write('Case #'+str(i+1)+': NO\n')              
#OutFile.write('Case #'+str(i+1)+': YES\n')   
