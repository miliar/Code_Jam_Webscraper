
fname="A-small-attempt0.in"
inputF=open(fname,'r+')
outF=open('output','a+')

T=int(inputF.readline())
for i in xrange(T):
    x=str(i+1)
    aanswer=inputF.readline()
    alay=[]
    for j in xrange(4):
        aline=inputF.readline().split()
        alay.append(aline)
   
    banswer=inputF.readline()
    blay=[]
    for j in xrange(4):
        bline=inputF.readline().split()
        blay.append(bline)
    
    A=alay[int(aanswer)-1]
    B=blay[int(banswer)-1]
    
    C=list(set(A).intersection( set(B) ))
    if len(C)==0:
        #~ print 'Case #'+x+': Volunteer cheated!'
        outF.write('Case #'+x+': Volunteer cheated!\n')
    elif len(C)==1:
        #~ print 'Case #'+x+': '+C[0]
        outF.write('Case #'+x+': '+C[0]+'\n')
    else:
        #~ print 'Case #'+x+': Bad magician!'
        outF.write('Case #'+x+': Bad magician!\n')
    #~ print A,B

inputF.close()
outF.close()
