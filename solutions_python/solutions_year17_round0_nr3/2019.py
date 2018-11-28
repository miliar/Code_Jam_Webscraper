#!/usr/bin/env python
import argparse
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input","-i", help="input file")
    parser.add_argument("--output","-o")
    args = parser.parse_args()
    return args

def bathroom(N,K):
    if N == K:
        return(0,0)
    # dic for position (L_s,R_s), key by the index
    #print ("N: {}, K: {}".format(N,K))
    dic = {}
    for i in range(N):
        dic[i] = (i,N-1-i)
    #print (dic)
    for user in range(K):
        closest_value = {}
        farthest_value = {}
        for key in dic:
            closest_value[key] = min(dic[key])
        for key in dic:
            farthest_value[key] = max(dic[key])
        max_dis = -1
        list_index = []
        for key in closest_value.keys():
            if closest_value[key]>max_dis:
                list_index = [key]
                max_dis = closest_value[key]
            elif closest_value[key] == max_dis:
                list_index.append(key)
#        print ("current max min distance is {} with list of index {}".format(max_dis,list_index))
        # will assign value 1 to list_index at index 0 
        # or it means that delete the key value at index0 from dic
        # from the list of index, find list of index that has maximum value of max
        second_index =[]
        max_dis = -1
        for index in list_index:
            if farthest_value[index]>max_dis:
                second_index = [index]
                max_dis = farthest_value[index]
            elif farthest_value[index] == max_dis:
                second_index.append(index)
#        print ("current max max distance is {} with list of index {}".format(max_dis,second_index))
        chosen_index = second_index[0]
        result = dic.pop(chosen_index)
        # recompute the value
        for key in dic:
            if key < chosen_index:
                dic[key] = (dic[key][0], min(chosen_index - 1- key,dic[key][1]))
            elif key > chosen_index:
                dic[key] = (min(key- 1- chosen_index,dic[key][0]),dic[key][1])
#        print ("After choosing index {}, our dic becomes {}".format(chosen_index,dic))
    return max(result),min(result)
if __name__ == "__main__":
    arguments = get_arguments()
    output    = arguments.output
    input     = arguments.input
    infile    = open(input,"r")
    outfile   = open(output,"w")
    test      = int(infile.readline().strip())
    for i in range(1,test+1):
        N,K = infile.readline().strip().split()
        result = bathroom(int(N),int(K))
        outfile.write("Case #{}: {} {}\n".format(i,result[0],result[1])) 
    infile.close()
    outfile.close()


    

