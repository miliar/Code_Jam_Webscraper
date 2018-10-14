def horsr_calc(max_distance, horse_list):

    #print horse_list
    #print max_distance
    slowest_time = -1

    for e in horse_list:
        end_time = ((float(max_distance) - float(e[0]))/float(e[1]))
        if end_time > slowest_time:
            slowest_time = end_time

    answer = max_distance/slowest_time
    #print answer
    return answer


f = open('horsealarge.in.in', 'r')
g = open('testout.out', 'w')
content = f.readlines()
numOfCases = int(content[0])
iter = 0
iter2 = 0
case = 1
num_horses = -1
h_list = []
s = ""
max_dist = -1
for n in content:
    n_list = n.split()
    #print n_list[0]
    if iter == 0:
        pass
    else:

        if iter2 == 0:
            #print "Max distance = " + n_list[0]
            #print "horses = " + n_list[1]
            max_dist = n_list[0]
            #print max_dist
            num_horses = n_list[1]
            #print num_horses
            iter2 = iter2 + 1
        elif iter2 > 0 and iter2 <= int(num_horses):
            h_list.append([int(n_list[0]), int(n_list[1])])
            iter2 = iter2 + 1
            if (iter2 == int(num_horses) + 1):

                print "Case #" + str(case) + ": " + str(horsr_calc(float(max_dist), h_list))
                s = s + "Case #" + str(case) + ": " + str(horsr_calc(float(max_dist), h_list)) + "\n"
                iter2 = 0
                h_list = []
                case = case + 1


        #print "Case #"+str(iter)+": "+ str(flipPancakes (str(n_list[0]), int(n_list[1])))
        #s = s + "Case #"+str(iter)+": "+ str(flipPancakes(n_list[0], int(n_list[1]))) + "\n"
    iter = iter + 1
g.write(s)