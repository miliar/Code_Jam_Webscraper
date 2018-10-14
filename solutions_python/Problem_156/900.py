import sys

dict_res = {}

def min_time(d):
#    print d
    global dict_res
    if tuple(d) in dict_res:
        #print "Hit" + str(tuple(d))
        return dict_res[tuple(d)]
    #if all(v == 0 for v in d):
    #    dict_res[tuple(d)] = 0
    #    return 0
    else:
        max_elem = max(d)
        new_d = [v for v in d]
        if max_elem == 1:
            dict_res[tuple(d)] = 1
            return 1
        elif max_elem != 1:
            new_d_list = []
            del new_d[new_d.index(max_elem)]
            for i in range(2, max_elem/2+1):
                _new_d = [v for v in new_d]
                _new_d.append(i)
                _new_d.append(max_elem - i)
                new_d_list.append(_new_d)

            time = [min_time(new_d)+1 for new_d in new_d_list]
            #time.append(min_time([v-1 for v in d if v > 0])+1)
            time.append(max_elem)

#        print "Minus 1: " + str(min_time([v-1 for v in d if v > 0]) + 1)
#        print [v-1 for v in d if v > 0]
#        print "Saparta" + str(min_time(new_d) + 1)
#        print new_d
            min_value = min(time)
            dict_res[tuple(d)] = min_value
            return min_value

n = int(sys.stdin.readline())

r = 1
while n > 0:
    n = n-1
    count = int(sys.stdin.readline())
    dinners = sys.stdin.readline().strip().split(" ")
    dinners = [int(v) for v in dinners]
    print "Case #"+str(r)+": "+str(min_time(dinners))
    #print dinners
    r += 1

