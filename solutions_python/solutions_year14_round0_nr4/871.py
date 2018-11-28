
input_file = open('D-large.in','r')
input_data = ''.join(input_file.readlines())
input_file.close()

lines = input_data.split('\n')
no_of_test_cases = int(lines[0])
f=open("out.txt",'w')
for i in range (1,no_of_test_cases+1):
    j=3*i-2
    blocks_Naomi = []
    blocks_Ken = []
    no_of_blocks = int (lines[j])
    inp = [lines[j+1].split(' ')]
    inp.append(lines[j+2].split(' '))
    for k in range(no_of_blocks):
        blocks_Naomi.append(float(inp[0][k]))
        blocks_Ken.append(float(inp[1][k]))
    blocks_Naomi.sort()
    blocks_Ken.sort()
    #print blocks_Naomi
    #print blocks_Ken
    #Deceiptive WAR
    deceiptive_war_score = 0
    start,end=0,no_of_blocks-1
    for k in range(no_of_blocks):
        Naomi_select = blocks_Naomi[k]
        if Naomi_select < blocks_Ken[start]:
            blocks_Ken[end]=-blocks_Ken[end]
            end-=1
        else:
            deceiptive_war_score+=1
            blocks_Ken[start]=-blocks_Ken[start]
            start+=1
    #print "Deceptive : %d"%deceiptive_war_score


    #War
    T = []
    for k in range(no_of_blocks):
        blocks_Ken[k]=-blocks_Ken[k]
        T.append(blocks_Ken[k])
    war_score = 0
    #start,end=0,no_of_blocks-1
    for k in range(1,no_of_blocks+1):
        Naomi_select = blocks_Naomi[-k]
        #print Naomi_select,blocks_Ken[-1]
        if Naomi_select > T[-1]:
            T.remove(T[0])
            war_score+=1
        #    print "won"
        else:
            l=0
            while T[l]<Naomi_select:
                l+=1
            T.remove(T[l])
        #    print "lost"
        #print blocks_Ken
    #print "War : %d"%war_score
    #print deceiptive_war_score
    #print ("Case #%d: %d %d"%(i,war_score,deceiptive_war_score))



    f.write("Case #%d: %d %d\n"%(i,deceiptive_war_score,war_score))
f.close()


