#-------------------------------------------------------------------------------
#Roller Coaster
#coder: TimGluz
#desc: task nr.3 from Google Code Jam

#--0 helper funcs

#-- convert string list to integer list
def convert_to_int(str_list):
    int_list = []
    for str1 in str_list:
        int_list.append(int(str1))
    return int_list
#--1.read given data
waiting_queue = []
fp = open('/home/timgluz/code/roller.txt', 'r')
out_fp = open('/home/timgluz/code/roller_sol1.txt', 'w')
count_test = fp.readline()

#--2. find solution 
for i in range(0, int(count_test)):
    print "test nr:",i
    r,k,n = convert_to_int(fp.readline().split())
    waiting_queue = convert_to_int(fp.readline().split())
    print "algandmed: r=%u, k=%u, n=%u \n %s "% (r,k,n, str(waiting_queue))
    #hardcoded and repeated solution
    total_sum =0 #how much money is earned
   
    #fill the wagon
    for round in range(0, r):
        roller_queue = []
        for group in waiting_queue:
            if(group+sum(roller_queue) <= k):
                roller_queue.append(group)
            else: break

        waiting_queue += roller_queue
        total_sum += sum(roller_queue)
        del waiting_queue[0:len(roller_queue)]
        #
    print str(total_sum)    
    out_fp.write( "Case #%u: %u \n"%(i+1,total_sum))
    total_sum = 0
#close files
fp.close()
out_fp.close()
