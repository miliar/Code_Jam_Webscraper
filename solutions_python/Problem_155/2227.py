filein = open('A-large.in' )
fileout = open('output-large.in', 'w')
#T = int(raw_input()) #Number of test cases
T = int(filein.readline().strip())
for case in range(T):
    
    #question = str(raw_input()).split(" ")
    question = filein.readline().strip().split(" ")
    Smax, shyness_lv = int(question[0]), list(question[1]) #shyness level
    #print Smax,shyness #Pass render test
    auxiliary = 0
    available = 0
    for aud_indx in range(Smax+1): #Increasing index for audience; needed amount = audience_index
        #print "aud_indx,available",aud_indx,available
        join_aux = 0
        if aud_indx > available and int(shyness_lv[aud_indx])>0:
            join_aux = aud_indx - available
            auxiliary += join_aux
            #print "adding",join_aux
        #Number of people available for next turn is sum of auxiliary guests and num of people in that shyness level
        available += join_aux + int(shyness_lv[aud_indx])
    fileout.write("Case #"+str(case+1)+": "+str(auxiliary)+"\n")
filein.close()
fileout.close()
    
    
    
