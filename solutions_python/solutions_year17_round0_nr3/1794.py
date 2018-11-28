#! /usr/bin/python3

in_file = open('/home/blaidd-drwg/jam_input.txt', 'r')
out_file = open('/home/blaidd-drwg/jam_output.txt', 'w')

in_data = in_file.readlines()
cases = int(in_data[0])

for case in range(1, cases + 1):
    print(case)
    case_data = in_data[case].split()
    n = int(case_data[0])
    people = int(case_data[1])

    l = [None] * (n+2)
    r = [None] * (n+2)
    occupied = [None] * (n+2)
    for i in range(1, n+1):
        occupied[i] = False
        l[i] = i - 1
        r[i] = n - i

    occupied[0] = True
    occupied[n+1] = True
    l[0], r[n+1] = 0, 0 

    max_max = None
    min_max = None

    for p in range(0,people):
        min_indices = []
        min_max = float('-inf') 
        for i in range(0, n+2):
            if not occupied[i] and min(l[i], r[i]) > min_max:
                min_indices = [i]
                min_max = min(l[i], r[i])
            elif not occupied[i] and min(l[i], r[i]) == min_max:
                min_indices.append(i)


        max_indices = []
        max_max = float('-inf') 
        for i in min_indices:
            if max(l[i], r[i]) > max_max:
                max_indices = [i]
                max_max = max(l[i], r[i])
            elif max(l[i], r[i]) == max_max:
                max_indices.append(i)

        if len(min_indices) == 1:
            final_index = min_indices[0]
        else:
            final_index = max_indices[0]
        
        # print("Case:")
        # print(case)
        # print(final_index)

        occupied[final_index] = True
        i = final_index
        while True:
            i -= 1
            r[i] = final_index - (i + 1)
            if occupied[i]:
                break

        i = final_index
        while True:
            i += 1
            l[i] = i - (final_index + 1)
            if occupied[i]:
                break

    out_file.write('Case #%d: %d %d' % (case, max_max, min_max))
    out_file.write('\n')

in_file.close()
out_file.close()
