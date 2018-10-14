f = open(r'K:\Codes\code jam solutions\2014 Round 1\Problem A Magic Trick\A-small-attempt0.in')
out = open(r'K:\Codes\code jam solutions\2014 Round 1\Problem A Magic Trick\testSOL.txt','w')

tc = int(f.readline())
cardlist = [list() for i in range(1,tc+1)]
sollist = list()

#print cardlist

for i in range(1,tc+1):
    sollist.append(int(f.readline())-1)
    for j in range(1,5):
        cardlist[i-1].append(f.readline().split())
    sollist.append(int(f.readline())+3)
    for j in range(1,5):
        cardlist[i-1].append(f.readline().split())
        
iter= 0
case = 1
for lists in cardlist:
    list1 = lists[sollist[iter]]
    iter += 1
    #print list1
    list2 = lists[sollist[iter]]
    iter += 1
    #print list2
    com = list(set(list1).intersection(list2))
    res = len(com)
    if (res == 0):
        out.write('Case #'+str(case)+': Volunteer cheated!\n')
    elif (res == 1):
        out.write('Case #'+str(case)+': '+str(com[0])+'\n')
    else:
        out.write('Case #'+str(case)+': Bad magician!\n')
    
    case += 1

out.close()
f.close()
        
#print cardlist
#print '\n'
#print sollist