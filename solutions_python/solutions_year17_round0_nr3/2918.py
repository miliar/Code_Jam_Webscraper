t = int(input())
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    stalls = []
    #setup
    for j in range(n+2):
        stalls.append(0)
    stalls[0] = 1
    stalls[-1] = 1

    for people in range(k):
        stall_info = []
        for stall in range(n+2):
            current_stall = []
            if stalls[stall] != 1:
            #calculate L and R if stall is not occupied
                for left in range(stall, -1, -1):
                    if stalls[left] == 1:
                        current_stall.append(stall - left - 1)
                        break
                for right in range(stall, len(stalls)):
                    if stalls[right] == 1:
                        current_stall.append(right - stall - 1)
                        break
            stall_info.append(current_stall)
        #print(stall_info)

        #take stall info and find the min(L, R) and max(L, R)
        stall_values = []
        for stall in range(len(stall_info)):
            if stall_info[stall] != []:
                current_stall_values = []
                current_stall_values.append(min(stall_info[stall][0], stall_info[stall][1]))
                current_stall_values.append(max(stall_info[stall][0], stall_info[stall][1]))
                stall_values.append(current_stall_values)
            else:
                stall_values.append([])
        #print(stall_values)
        max_min = -1
        max_max = 0
        max_min_indexes = []
        max_max_indexes = []
        # those for which min(L, R) is maximal
        # if only one, then choose it
        for values in range(len(stall_values)):
            if stall_values[values] != []:
                if stall_values[values][0] >= max_min:
                    max_min = stall_values[values][0]
                    #print(stall_values[values], values)
                    max_min_indexes.append(values)
        pls_help = []
        for each in max_min_indexes:
            if stall_values[each][0] == max_min:
                pls_help.append(each)
        # otherwise choose the one among where max(L, R) is maximal
        # MIKS TA VÕTAB STALL NR 2, KAS MIDAGI ON MAX KATKI VÄ
        #print("indexes", len(pls_help))
        #print(pls_help)
        if len(pls_help) > 0:
            for value in pls_help:
                if stall_values[value][1] > max_max:
                    max_max = stall_values[value][1]
                    max_max_indexes.append(value)

        y = max_max
        z = max_min

        # if still more than 1, choose leftmost
        # put person into appropriate stall
        if len(max_max_indexes) > 0:
            stalls[max_max_indexes[0]] = 1
        else:
            stalls[max_min_indexes[0]] = 1

        #print(stall_values)

    #print the last max(lr) and min(lr)
    print("Case #{}: {} {}".format(i, y, z))