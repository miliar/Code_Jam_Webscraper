#def FriendsNum():




def main():
    #input
    inf=open('A-large.in')

    #output
    outf=open('large-out.txt','w')

    caseNum=int(inf.next())

    for case in range(caseNum):
        line=inf.next().rstrip().split(' ')
        Smax=int(line[0])
        aud=line[1]
        outf.write('Case #'+str(case+1)+': '+str(friendsNum(Smax, aud))+'\n')

    inf.close()
    outf.close()


def friendsNum(Smax, audience):
    Sum=0
    friends=0
    for p in range(Smax+1):
        if Sum < p :
            Sum+=1
            friends+=1
            
        Sum+=int(audience[p])
        #print Sum
        #print p

    return friends
