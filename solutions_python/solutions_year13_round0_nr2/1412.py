filename = "B-large.in" # change later
f = open(filename)
T = int(f.readline())
for case in range(1,T+1):
    s = f.readline()
    tmp = s.split()
    N = int(tmp[0])
    M = int(tmp[1])
    lawn = {}
    for i in range(N):
        s = f.readline()
        s = map(int, s.split())
        for j in range(M):
            lawn[M*i+j] = s[j]
    lawnlist = lawn.items()
    lawnlist.sort(key = lambda a: a[1])
    lawnlist.reverse()
    
    lawn_index = 0
    forbidden_x = set()
    forbidden_y = set()
    impossible_flag = 0
    unchecked_flag = 0
    while True:
        ind, biggest = lawnlist[lawn_index]
        tmp_fob_x = set()
        tmp_fob_y = set()
        x = ind / M
        y = ind % M
        if (x in forbidden_x) and (y in forbidden_y):
            impossible_flag = 1
            break
        elif unchecked_flag == 1 and lawn_index == N*M-1:
            impossible_flag = 0
            break
        else:
            tmp_fob_x.add(x)
            tmp_fob_y.add(y)
        unchecked_flag = 0
        while lawn_index < N*M-1:
            lawn_index += 1
            ind, value = lawnlist[lawn_index]
            if value != biggest:
                unchecked_flag = 1
                break
            else:
                x = ind / M
                y = ind % M
                if (x in forbidden_x) and (y in forbidden_y):
                    impossible_flag = 1
                    break
                else:
                    tmp_fob_x.add(x)
                    tmp_fob_y.add(y)
        if impossible_flag == 1:
            break
        elif lawn_index == N*M-1 and unchecked_flag != 1:
            break
        else:
            forbidden_x |= tmp_fob_x
            forbidden_y |= tmp_fob_y

    print "Case #" + str(case) + ": ",
    if impossible_flag == 1:
        print "NO"
    else:
        print "YES"
            