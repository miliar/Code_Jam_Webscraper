# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

T = int(raw_input())  # read a line with a single integer

for i in xrange(1, T + 1):
#    line = raw_input().split()
#    flip_str = line[0]
#    pan = line[1]

    all_str = raw_input().split()
    N = int(all_str[0])
    K = int(all_str[1])

    if N-K == 0:
        print "Case #"+str(i)+": 0 0"
        continue

    if K == 1:
        print "Case #"+str(i)+": "+str((N-1)-(N-1)/2)+" "+str((N-1)/2)
    else:
        space = {}
        space[N] = 1

        count = 1
        add = 1
        while K > count:
            add *= 2
            count += add
            tmp = {}
            for s in space.keys():
                tmp[(s-1)/2] = tmp.get((s-1)/2, 0) + space[s]
                tmp[s-1-(s-1)/2] = tmp.get(s-1-(s-1)/2, 0) + space[s]
            space = tmp

        keylist = space.keys()
        keylist.sort()

        count -= add
        for key in keylist[::-1]:
            count += space[key]
            if count >= K:
                left_space = key
                break

        print "Case #"+str(i)+": "+str((left_space-1)-(left_space-1)/2)+" "+str((left_space-1)/2)
