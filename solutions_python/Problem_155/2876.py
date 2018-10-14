input_list=[]
input_text=""
no_of_standings=0
no_of_invitees=0
shy_level_count=-1
p=0


no_of_test_cases=int(raw_input())
for i in xrange(0,no_of_test_cases):
    input_text=raw_input()
    input_list.append(input_text.split(" "))


for i in xrange(0,no_of_test_cases):
    for j in xrange(0,int(input_list[i][0])+1):
        shy_level_count=int(input_list[i][1][j])
        
        

        no_of_standings+=shy_level_count
        
        if no_of_standings<j+1:
            no_of_invitees+=1
            no_of_standings+=1
    print "Case #"+str(i+1)+": "+str(no_of_invitees)
    no_of_standings=0
    no_of_invitees=0
    
        
        
        


















