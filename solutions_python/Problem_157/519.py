#! /opt/local/bin/python

#f = open("C-small-attempt0.in")
f = open("C-large.in")
#f = open("exC.in")

T= int(f.readline().strip());

#dict of mult, sign
Tab = {'1':{'1':('1',1),'i':('i',1) ,'j':('j',1), 'k':('k',1)},
       'i':{'1':('i',1),'i':('1',-1) ,'j':('k',1), 'k':('j',-1)},
       'j':{'1':('j',1),'i':('k',-1),'j':('1',-1),'k':('i',1)},
       'k':{'1':('k',1),'i':('j',1) ,'j':('i',-1),'k':('1',-1)}}

def searchfor (string,ch,l0,X0,Xf):
    found = False
    chi = ('1',1)
    li,Xi =l0,X0
    while(not chi==(ch,1)):
        #print li,chi
        chi_tup=Tab[chi[0]][string[li]]
        chi=(chi_tup[0],chi[1]*chi_tup[1])
        li+=1
        if li>len(string)-1:
            Xi+=1
            li=0
            if(Xi>Xf or Xi-X0>4):
                return (False,(li,Xi))
    return (True,(li,Xi))

def checkfork(string,l0,X0,Xf):
    #remaining should be k .. can leave out if we find a boundary s.t. 4*String remaining
    chi = ('1',1)
    li,Xi =l0,X0
    while(1):
        #print li,chi
        #print Xi
        chi_tup=Tab[chi[0]][string[li]]
        chi=(chi_tup[0],chi[1]*chi_tup[1])
        li+=1
        if li>len(string)-1:
           if chi == ('k',1): # check that 4*string are left
               if((X-Xi)%4==0):
                    return True
           Xi+=1
           li=0
           if(Xi>Xf or Xi-X0>4):
                return False

    return False




for t in range(T):
    L,X=[int(x) for x in f.readline().strip().split()]
    string = f.readline().strip().split()[0]
    (foundi,(l1,X1))=searchfor(string,'i',0,1,X)
    if not foundi:
        print "Case #"+str(t+1)+": NO"
        continue
    (foundj,(l2,X2))=searchfor(string,'j',l1,X1,X)
    if not foundi:
        print "Case #"+str(t+1)+": NO"
        continue
    (foundk)=checkfork(string,l2,X2,X)
    if not foundk:
        print "Case #"+str(t+1)+": NO"
        continue
    print "Case #"+str(t+1)+": YES"


