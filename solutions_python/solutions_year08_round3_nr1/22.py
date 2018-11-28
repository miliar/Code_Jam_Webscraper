#! /usr/bin/python

import sys




def do_task(task_bite):

    [P, K, L] = [int(x) for x in task_bite[0].split()]
    frequencies = [int(x) for x in task_bite[1].split()]
    frequencies.sort()
    frequencies.reverse()
    keys = [[] for x in range(K)]

    print P,K,L, frequencies

    for k in frequencies:

        shortest_key_length = min([len(x) for x in keys])
        shortest_key_index = [x for x in range(K) if len(keys[x]) == shortest_key_length][0]
   #     print shortest_key_length, shortest_key_index
        keys[shortest_key_index].append(k)

    #    print keys

    return sum([sum([x[k]*(k+1) for k in range(len(x))])  for x in keys])

###############
#    MAIN     #
###############

input_lines = file(sys.argv[1]).read().split("\n")
out_handle = file(sys.argv[2], 'w')
ncases = int(input_lines[0])
bite_size = 2

for case in range(ncases):

    task_bite = input_lines[1 + (bite_size*case):1+(bite_size*(case+1))]
    
    out_string = "Case #%i: " %(case + 1) + str(do_task(task_bite))
    print out_string
    out_handle.write(out_string + "\n")

out_handle.close()
