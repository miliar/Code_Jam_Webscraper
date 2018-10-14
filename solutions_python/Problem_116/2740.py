
'''
Created on Apr 13, 2013

@author: Victor
'''
foo=open("input.in")
l=foo.readline().strip()
index=int(l)
for i in range(index):
    l1=foo.readline().strip()
    l2=foo.readline().strip()
    l3=foo.readline().strip()
    l4=foo.readline().strip()
    listX=["TXXXX","XTXX","XXTX","XXXT","XXXX"]
    listO=["TOOO","OTOO","OOTO","OOOT","OOOO"]
    listin=[l1,l2,l3,l4]
    temp=""
    for j in range(4):
        temp+=(l1[j]+l2[j]+l3[j]+l4[j])
        listin.append(temp)
        temp=""
    listin.append(l1[0]+l2[1]+l3[2]+l4[3])
    listin.append(l1[3]+l2[2]+l3[1]+l4[0])
    s=set(listin)
    sx=set(listX)
    so=set(listO)
    if len(so.intersection(s))>0:
        print "Case #"+repr(i+1)+": O won"
    elif len(sx.intersection(s))>0:
        print "Case #"+repr(i+1)+": X won"
    elif l1.find(".")==-1 and l2.find(".")==-1 and l3.find(".")==-1 and l4.find(".")==-1:
        print "Case #"+repr(i+1)+": Draw"
    else:
        print "Case #"+repr(i+1)+": Game has not completed"
    foo.readline()
