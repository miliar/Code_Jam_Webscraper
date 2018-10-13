#Bathroom Stall
import itertools
import pprint
def find_true(l):
    true_elements = []
    for stall_num, val in enumerate(l):
        if val == 1:
            true_elements.append(stall_num)
    true_elements = sorted(true_elements)
    return true_elements
def next_stall(stall_list):
    minLR = {}
    maxLR = {}
    for stall_num, stall in enumerate(stall_list):
        if stall == 0:
            leftSide = list(reversed(stall_list[0:stall_num]))
            rightSide = stall_list[stall_num+1:]
            x = 0
            while 1:
                if leftSide[x] == 1:
                    leftDistance = x
                    break
                x += 1
            x = 0
            while 1:
                if rightSide[x] == 1:
                    rightDistance = x
                    break
                x += 1
            minLR[stall_num] = min([leftDistance,rightDistance])
            maxLR[stall_num] = max([leftDistance,rightDistance])
    
    sortedMin = list(reversed(sorted(minLR.items(), key=lambda x: x[1])))
    cur_max = -99
    cur_at_max = []
    cur_at_max_ids = []
    max_at_max = {}
    for item in sortedMin:
        if item[1] > cur_max:
            cur_max = item[1]
            cur_at_max = [item]
            cur_at_max_ids.append(item[0])
            max_at_max = {}
            max_at_max[item[0]] = [maxLR[item[0]]]
        elif item[1] == cur_max:
            cur_at_max.append(item)
            cur_at_max_ids.append(item[0])
            max_at_max[item[0]] = [maxLR[item[0]]]
    cur_at_snd_max = []
    if len(cur_at_max) > 1:
        sortedMax = sorted(maxLR.items(), key=lambda x: x[1])
        cur_snd_max = -99
        cur_at_snd_max = []
        for item in sortedMax:
            if item[1] > cur_snd_max and item[0] in cur_at_max_ids:
                cur_snd_max = item[1]
                cur_at_snd_max = [item]
            if item[1] == cur_max  and item[0] in cur_at_max_ids:
                cur_at_snd_max.append(item)
    else:
        result = {}
        result['min'] = minLR[cur_at_max[0][0]]
        result['max'] = maxLR[cur_at_max[0][0]]
        stall_list[cur_at_max[0][0]] = 1
        return stall_list, cur_at_max[0][0], result
    if len(cur_at_snd_max) != 1:
        cur_at_snd_max = sorted(enumerate(cur_at_snd_max), key=lambda x: x[0])
        chosen = cur_at_snd_max[0][1]
        result = {}
        result['min'] = minLR[chosen[0]]
        result['max'] = maxLR[chosen[0]]
        stall_list[chosen[0]] = 1
        return stall_list, cur_at_snd_max[0][1], result
    else:
        result = {}
        result['min'] = minLR[cur_at_snd_max[0][0]]
        result['max'] = maxLR[cur_at_snd_max[0][0]]
        stall_list[cur_at_snd_max[0][0]] = 1
        return stall_list, cur_at_snd_max[0][0], result
        
results = []
num_of_in = int(input())
for inter in xrange(num_of_in):
    sys.stderr.write("on case " + str(inter) + "\n")
    the_in = raw_input()
    the_in = the_in.split(" ")
    N = int(the_in[0])
    K = int(the_in[1])
    stall_list = [1]
    for x in xrange(N):
        stall_list.append(0)
    stall_list.append(1)
    next_stall_choice = 0
    for x in xrange(K):
        stall_list, next_stall_choice, choice_info = next_stall(stall_list)
    results.append(choice_info)
res_num = 0
for result in results:
    q = "Case #" + str(res_num+1) + ": " + str(result['max']) + " "
    q += str(result['min'])
    print(q)
    res_num += 1
