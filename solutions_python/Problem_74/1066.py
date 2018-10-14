#############################
# Script description
import string
import math

##################
# Main function  #
##################
#in_file_name = "B-large.in"
in_file_name = "A-small-attempt1.in"
#in_file_name = "simple.in"
in_file= open(in_file_name, 'r')

out_file = open('out.txt','w')


##Parse in file
#Parse in file
num_of_tescases = in_file.readline()
for count in range (1,int(num_of_tescases)+1):
    inline = in_file.readline().split()
    time = 0
    num_of_trgt = int(inline[0])
    idx = 1
    o_pos = 1
    b_pos = 1
    o_trgt_list = []
    b_trgt_list = []
    o_idx_list = []
    b_idx_list = []
    while(num_of_trgt > 0):
        if inline[idx] == 'O' :
            o_trgt_list.append(int(inline[idx+1]))
            o_idx_list.append((idx+1)/2)
        if inline[idx] == 'B' :
            b_trgt_list.append(int(inline[idx+1]))
            b_idx_list.append((idx+1)/2)
        idx+=2
        num_of_trgt-=1
    #actual calculation
    while (len(o_trgt_list)> 0 and len(b_trgt_list)>0):
        print o_trgt_list, b_trgt_list
        o_trgt = o_trgt_list[0]
        b_trgt = b_trgt_list[0]
        o_idx = o_idx_list[0]
        b_idx = b_idx_list[0]
        o_dist = abs(o_trgt-o_pos)
        b_dist = abs(b_trgt-b_pos)
        #Orange is closer and should be done 1'st
        if(o_dist < b_dist and (o_idx<b_idx)):
            print 'Orange is closer and should be done 1'
            #advance blue
            if (b_trgt > b_pos):
                b_pos = b_pos+o_dist+1
            else:
                b_pos = b_pos-o_dist-1
            #perform orange
            o_pos = o_trgt
            o_trgt_list.pop(0)
            o_idx_list.pop(0)
            #advance time
            time+=o_dist+1
        #Blue is closer and should be done 1'st
        if(b_dist < o_dist and (b_idx < o_idx)):
            print 'Blue is closer and should be done 1'
            #advance orange
            if (o_trgt > o_pos):
                o_pos = o_pos+b_dist+1
            else:
                o_pos = o_pos-b_dist-1
            #perform blue
            b_pos = b_trgt
            b_trgt_list.pop(0)
            b_idx_list.pop(0)
            #advance time
            time+=b_dist+1
        #Orange is closer, but should be done 2'nd
        if(o_dist < b_dist and (o_idx > b_idx)):
            print 'Orange is closer, but should be done 2'
            #advance orange to target
            o_pos = o_trgt
            #perform blue
            b_pos = b_trgt
            b_trgt_list.pop(0)
            b_idx_list.pop(0)
            #advance time
            time+=b_dist+1
        #Blue is closer, but should be done 2'nd
        if(b_dist < o_dist and (b_idx > o_idx)):
            print 'Blue is closer, but should be done 2'
            #advance blue to target
            b_pos = b_trgt
            #perform orange
            o_pos = o_trgt
            o_trgt_list.pop(0)
            o_idx_list.pop(0)
            #advance time
            time+=o_dist+1
        #dist is equal , but orange should be done 1'st
        if(o_dist == b_dist and (o_idx<b_idx)):
            print 'ist is equal , but orange should be done 1'
            #advance blue
            if (b_trgt > b_pos):
                b_pos = b_pos+o_dist
            else:
                b_pos = b_pos-o_dist
            #perform orange
            o_pos = o_trgt
            o_trgt_list.pop(0)
            o_idx_list.pop(0)
            #advance time
            time+=o_dist+1
        #dist is equal, but blue should be done 1'st
        if(b_dist == o_dist and (b_idx < o_idx)):
            print 'dist is equal, but blue should be done 1'
            #advance orange
            if (o_trgt > o_pos):
                o_pos = o_pos+b_dist
            else:
                o_pos = o_pos+b_dist
            #perform blue
            b_pos = b_trgt
            b_trgt_list.pop(0)
            b_idx_list.pop(0)
            #advance time
            time+=b_dist+1

    if (len(b_trgt_list) > 0):
        left_trgt_list = b_trgt_list
        left_pos = b_pos
    else:
        left_trgt_list = o_trgt_list
        left_pos = o_pos

    while(len(left_trgt_list)>0):
        trgt = left_trgt_list[0]
        dist = abs(trgt-left_pos)
        left_pos = trgt
        time+=dist+1
        left_trgt_list.pop(0)




    #Final print
    str_to_print = "Case #"+str(count)+':'+ ' '+str(time)
    print str_to_print
    print >> out_file, str_to_print
    #print >> out_file,  "Case #"+str(count)+':'+ ' '+inline[-1].split()



#Close files
in_file.close()
out_file.close()


