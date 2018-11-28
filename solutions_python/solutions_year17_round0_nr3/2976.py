t = int(raw_input())

for v in range(t):
    n, k = raw_input().split()
    n = int(n)
    k = int(k)

    stalls = [False] * n
    ls = [n] * n
    rs = [n] * n

    actual_ls = 0
    actual_rs = 0
    for q in range(k):
        # Set ls rs
        for a, i in enumerate(stalls):
            if i:
                ls[a] = -1
                rs[a] = -1
            else:
                if a == 0:
                    ls[a] = 0
                else:
                    ls[a] = 0
                    for b in range(a-1,-1,-1): # From a-1 to 0
                        if stalls[b] == True:
                            break
                        ls[a] += 1

                if a == len(stalls)-1:
                    rs[a] = 0
                else:
                    rs[a] = 0
                    for b in range(a+1,len(stalls)):
                        if stalls[b] == True:
                            break
                        rs[a] += 1

        # Occupy
        cond_1_max = 0 # not sure if 0 is okay but we're getting max
        for i in range(n):
            nxt = min(ls[i],rs[i])
            if cond_1_max < nxt:
                cond_1_max = nxt

        # Get all indices with cond_1_max
        indices = []
        for i in range(n):
            if min(ls[i],rs[i]) == cond_1_max:
                indices.append(i)

        if len(indices) == 1:
            stalls[indices[0]] = True
            actual_ls = ls[indices[0]]
            actual_rs = rs[indices[0]]
        else:
            cond_2_max = 0
            for i in indices:
                nxt = max(ls[i],rs[i])
                if cond_2_max < nxt:
                    cond_2_max = nxt

            # Get all indices with cond_2_max
            indices_2 = []
            for i in indices:
                if max(ls[i],rs[i]) == cond_2_max:
                    indices_2.append(i)

            stalls[indices_2[0]] = True
            actual_ls = ls[indices_2[0]]
            actual_rs = rs[indices_2[0]]

    print 'Case #' + str(v+1) + ': '  + str(max(actual_ls,actual_rs)) + ' ' + str(min(actual_ls,actual_rs))
