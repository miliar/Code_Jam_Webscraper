import sys
#sys.argv[1] input
#sys.argv[2] output file


#get the input data
#open the file
read_file = open(sys.argv[1],"r");
write_file = open(sys.argv[2],"w");
data = read_file.readlines()
read_file.close()

test_cases = data.pop(0)

for i in range(0,int(test_cases)):
    
    blocks =int(data.pop(0))
  
    naomi = [float(f) for f in data.pop(0).split()]
    ken = [float(f) for f in data.pop(0).split()]
    naomi.sort()
    ken.sort()
    #war
    #print "i "+ str(i)
    #print "n "+ str(naomi)
    #print "k "+ str(ken)
    n = 0
    k = 0
    war = blocks
    d_war = blocks
    while n < blocks and k < blocks:
    	if naomi[n] < ken[k]:
    		war-=1
    		n+=1
    		k+=1
    	else:
    		k+=1
  	
    #deceitful war
    while naomi and ken:
    	if naomi[0] > ken[0]:
    			naomi.pop(0)
    			ken.pop(0)
    	else:
    		if naomi[0] < ken[-1] :
    			naomi.pop(0)
    			ken.pop(-1)
    			d_war-=1
    
    		
    		
    #print d_war, war
    
    write_file.write('Case #'+str(i+1)+': '+str(d_war)+' '+str(war)+'\n')
write_file.close()
