

def get_input(path):
    
    file_des = open(path)
    t  = int(file_des.readline())
    in_list = [tuple(map(int,l.split())) for l in file_des.readlines()]
    file_des.close()
    return in_list

def get_min_max_of_bathStall(in_list):
    if not in_list:
        print "in_list is empty"
        return
    out_list = []
    for t in in_list:
        bStall_list = []
        n, k = t[0], t[1]
        print n,k
        if (n * 0.6) > k-1:
            l = n/2
            r = n - l
            if l > r:
                l = l -1
            else:
                r = r-1
            #result_element = (l,r)
            bStall_list.append(l)
            bStall_list.append(r)
            k = k-1
            
            while k >0:
                max_ele = max(bStall_list)
                l = max_ele/2
                r = max_ele - l
                if l > r:
                    l = l -1
                else:
                    r = r-1
                
                #print "b stalls - ", bStall_list
                
                max_ele_count = bStall_list.count(max_ele) 
                
                #print "ele - ", max_ele, "count - ", max_ele_count, "k - ",k
                
                bStall_list = list(filter(lambda ele: ele != max_ele, bStall_list))
                
                for i in range(max_ele_count):
                    #print "i, l, r", i, l, r
                    bStall_list.append(l)
                    bStall_list.append(r)
                
                k = k - max_ele_count 
              
                #print "b stalls - ", bStall_list
                #print "k - ", k
                #raw_input()
            
            result_element =  (max(l,r),min(l,r))
            out_list.append(result_element)
        else:
            out_list.append((0,0))
        print "out list - ", out_list
        print "-"*20
    return out_list

def print_output(out_list):
    if not out_list:
        print "nothing to print"
        return
    for i in range(1, len(out_list)+1):
        print "Case #{}: {} {}".format(i,out_list[i-1][0],out_list[i-1][1])
    
    
def main():
    
    in_list = get_input(raw_input("file path : "))
    print in_list
    out_list = get_min_max_of_bathStall(in_list)
    print_output(out_list)

main()
