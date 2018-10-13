#############################
# Script description
import string


##################
# Main function  #
##################
in_file_name = "B-large.in"
#in_file_name = "B-small-attempt2.in"
#in_file_name = "simple.in"
in_file= open(in_file_name, 'r')

out_file = open('out.txt','w')


##Parse in file
#Parse in file
num_of_tescases = in_file.readline()
for count in range (1,int(num_of_tescases)+1):
    inline = in_file.readline().split()
    idx = 0
    list_of_comb = []
    list_of_opp = []
    #Get list of comb
    num_of_comb = int(inline[idx])
    while (num_of_comb > 0):
        idx+=1
        num_of_comb-=1
        list_of_comb.append(inline[idx])
    #print list_of_comb
    #Get list of opposite
    idx+=1
    num_of_opp = int(inline[idx])
    while (num_of_opp > 0):
        idx+=1
        num_of_opp-=1
        list_of_opp.append(inline[idx])
    #print list_of_opp
    #Get string of elems
    idx+=1
    num_of_elems = inline[idx]
    idx+=1
    str_of_elems = inline[idx]

    #Bild actual list
    curr_elems_list = []
    for i in range (0, len(list(str_of_elems))):
        curr_elems_list.append(list(str_of_elems)[i])
        comb_found = 0
        #check combs
        if len(curr_elems_list) > 1 :
            if len(list_of_comb) > 0:
                for k in range (0, len(list_of_comb)):
                    last_2_elems_0 = curr_elems_list[-1]+curr_elems_list[-2]
                    last_2_elems_1 = curr_elems_list[-2]+curr_elems_list[-1]
                    comb_list = list(list_of_comb)[k]
                    comb_pair = comb_list[0]+comb_list[1]
                    if (comb_pair == last_2_elems_0 or comb_pair == last_2_elems_1):
                        curr_elems_list.pop()
                        curr_elems_list.pop()
                        curr_elems_list.append(comb_list[2])
                        comb_found = 1
                        break
        #check opp
        opp_found = 0
        if (comb_found == 0):
            if len(curr_elems_list) > 1 :
                if len(list_of_opp) > 0:
                    for k in range (0, len(curr_elems_list)-1):
                        opp_2_elems_0 = curr_elems_list[-1]+curr_elems_list[k]
                        opp_2_elems_1 = curr_elems_list[k]+curr_elems_list[-1]
                        for j in range (0,len(list_of_opp)):
                            if opp_2_elems_0 == list_of_opp[j] or opp_2_elems_1 == list_of_opp[j]:
                                curr_elems_list = []
                                opp_found = 1
                                break
                        if (opp_found == 1):
                            break

    #Final print
    str_to_print = "Case #"+str(count)+':'+ ' '+'['
    for i in range (0, len(list(curr_elems_list))):
        str_to_print = str_to_print+list(curr_elems_list)[i]
        if (i != len(list(curr_elems_list))-1):
            str_to_print = str_to_print+', '
    str_to_print = str_to_print+']'
    print str_to_print
    print >> out_file, str_to_print
    #print >> out_file,  "Case #"+str(count)+':'+ ' '+inline[-1].split()



#Close files
in_file.close()
out_file.close()


