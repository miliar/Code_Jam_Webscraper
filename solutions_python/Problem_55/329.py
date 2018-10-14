import re, sys


#TODO: 
#Check for boundary condtions like: k>= sum(groups)
def cost(r,k,groups):
    print "@Input:", r,k, groups
    s=sum(groups)
    if(s<=k): return r*s


    cycle_start=0
    gnum = len(groups)
    trans={}
    idx = 0
    turns=0
    running_cost = 0 #in case we finish r before processing groups
    while(True):
        ppl=0
        turns+=1
        if(turns>r): break   #exiting before discovering full cycle
        curr_node=idx+1
        temp_idx = idx
        while(True):
            print "@temp_idx:",temp_idx
            ppl+= groups[temp_idx]
            if(ppl>k):
                print "@br"
                break
            print "@ppl:", ppl
            temp_idx = (temp_idx+1)%gnum
        idx = temp_idx
        next_node = temp_idx+1
        trans[curr_node]=(next_node,ppl-groups[next_node-1])
        running_cost+=ppl-groups[next_node-1]
        if(next_node in trans):  # we have found a cycle. Exit loop 
            cycle_start = next_node
            break
    
    print "@transition", trans
    if(turns>=r): return running_cost
    print "@cycle start:", cycle_start
    cycle_length, cycle_cost = 0,0
    len_to_cycle, cost_to_cycle = 0,0
    
    curr=1
    
    while(True):
        if(curr==1 and curr==cycle_start): break
        temp, temp_cost = trans[curr]
        len_to_cycle+=1
        cost_to_cycle += temp_cost
        if(temp==cycle_start):break
        curr=temp
    print "@to cycle:", len_to_cycle, cost_to_cycle 


    curr= cycle_start
    while(True):
        temp, temp_cost = trans[curr]
        cycle_length+=1
        cycle_cost += temp_cost
        if(temp==cycle_start):break
        curr =  temp
    print "@cycle:", cycle_length, cycle_cost    

    #we are sure that r is > len_to_cycle + cycle_len
    total_cost= cost_to_cycle + cycle_cost
    print "@base cost:", total_cost
    rem = r - len_to_cycle - cycle_length
    print "@rem:", rem 
    traverse_cycle , leftover  = divmod(rem, cycle_length)
    total_cost += traverse_cycle * cycle_cost
    
    print "@traverse_cycle:%d , leftover:%d"%(traverse_cycle , leftover)
    print '@cost after cycle:', total_cost
    curr =  cycle_start
    for i in range(leftover):
        curr, temp_cost = trans[curr]
        total_cost += temp_cost 
    print '@total cost:', total_cost    
    return total_cost
    
   



def process(filename):
    fw=open("op",'w')
    f=open(filename)
    case, line_no =0,-1
    pat = re.compile(r'\s+')

    for line in f:
        line_no +=1
        if(line_no==0):continue
        line=line.strip()
        if(line_no%2==1):
            case+=1
            r,k,x = map(lambda(x):int(x),pat.split(line)) 
               
        else:
            groups = map(lambda(x):int(x),pat.split(line))
            revenue = cost(r,k,groups)
            fw.write( "Case #%d: %d\n"%(case, revenue))
            fw.flush()
    f.close()
    fw.close()


process(sys.argv[1])









 
