T=int(raw_input())
for cases in range(1,T+1):
    n=int(raw_input())
    naomi = map(float,raw_input().split())
    ken = map(float,raw_input().split())
    war=0
    dwar=0
    naomi.sort()
    ken.sort()
    nnaomi=naomi[:]
    kken=ken[:]
    turns=0
    naomi.reverse()
    ken.reverse()
    
    while turns < n:
        #print naomi
        #print ken
        # if naomi > ken's greatest:
            # ken chooses his smallest
        # elif naomi < ken's greatest, >ken's smallest:
            # ken searches for element just greater than naomi
            # if found, he selects that element
            # else, he plays his smallest
        # elif naomi < ken's smallest:
            # ken chooses element just greater than naomi
        pos_naomi=0
        pos_ken=0
        if naomi[pos_naomi] > ken[pos_ken]:
            war+=1
            ken.pop(len(ken)-1)
            naomi.pop(pos_naomi)
        elif naomi[pos_naomi] < ken[pos_ken] and naomi[pos_naomi] > ken[len(ken)-1]:
            found=False
            for i in range(pos_ken,len(ken)):
                if ken[i] > naomi[pos_naomi]:
                    found=True
                    pos_ken=i
                    break
            if found:
                ken.pop(pos_ken) # choose just greater
                naomi.pop(pos_naomi)
            else:
                ken.pop(len(ken)-1) # choose smallest
                naomi.pop(pos_naomi)
            
        else:
            # naomi < ken's smallest
            ken.pop(len(ken)-1)
            naomi.pop(pos_naomi)
        
        turns+=1
            
        
    '''
    while turns<n:
        pos_naomi = len(naomi)-1
        if pos_naomi>0:
            choice_naomi = naomi[pos_naomi]
            pos_ken = len(ken)-1
        elif pos_naomi==0:
            choice_naomi = naomi[pos_naomi]
        
        pos_ken = len(ken)-1
        if ken[pos_ken] > choice_naomi: 
            # take smallest ken that is greater than naomi
            if pos_ken>0:
                while ken[pos_ken] > choice_naomi and pos_ken>0:
                    pos_ken-=1
                pos_ken+=1
                if ken[pos_ken-1] > choice_naomi:
                    pos_ken = pos_ken-1
                ken.pop(pos_ken)
                naomi.pop(pos_naomi)
        elif ken[pos_ken] < choice_naomi:
            pos_ken=0
            ken.pop(0)
            naomi.pop(pos_naomi)
            war+=1
        turns+=1
    '''
    # end of calculation of war score
    
    turns=0
    dwar=0
    pos_nnaomi=0
    pos_kken=0
    while turns < n:
        # always pick smallest naomi
        #print nnaomi
        #print kken
        if nnaomi[pos_nnaomi] < kken[pos_kken]:
            # swap current val of ken with his max, to inflict more damage
            '''
            temp=kken[pos_kken]
            kken[pos_kken]=kken[len(kken)-1]
            kken[len(kken)-1]=temp
            '''
            kken.pop(len(kken)-1)
            nnaomi.pop(pos_kken)
        else:
            kken.pop(pos_kken)
            nnaomi.pop(pos_nnaomi)
            dwar+=1
            
        turns+=1

    print "Case #{0}: {1} {2}".format(cases, dwar, war)
