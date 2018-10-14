
DEBUG = False

def debug(t):
    if DEBUG:
        print(t)

def dump_arr(arr):
    for i in range(len(arr)):
        print(''.join(arr[i]))

def fill(arr, j, k):
    debug("Filling (%d, %d)" % (j, k))
    # search backward first, then forward
    for l in range(k-1, -1, -1):
        debug("l=%d"%l)
        if arr[j][l] != '?':
            arr[j][k] = arr[j][l]
            return
    for l in range(k+1, C):
        debug("l=%d"%l)
        if arr[j][l] != '?':
            arr[j][k] = arr[j][l]
            return
        
def fill_empty_line(arr, j, k):
    debug("Filling (%d, %d)" % (j, k))
    # search backward first, then forward
    for l in range(j-1, -1, -1):
        debug("l=%d"%l)
        for m in range(k, -1, -1):
            debug("m=%d"%m)
            if arr[l][m] != '?':
                arr[j][k] = arr[l][m]
                return
        for m in range(k+1, C):
            debug("m=%d"%m)
            if arr[l][m] != '?':
                arr[j][k] = arr[l][m]
                return
    for l in range(j+1, R):
        debug("l=%d"%l)
        for m in range(k, -1, -1):
            debug("m=%d"%m)
            if arr[l][m] != '?':
                arr[j][k] = arr[l][m]
                return
        for m in range(k+1, C):
            debug("m=%d"%m)
            if arr[l][m] != '?':
                arr[j][k] = arr[l][m]
                return
    return '?' # should never reach here, unless all empty



T = raw_input()
T = int(T)

for i in range(T):
    line = raw_input()
    R, C = line.split()
    R = int(R)
    C = int(C)
    arr = []
    done = True
    for j in range(R):
        line = raw_input()
        if '?' in line:
            done = False
        #print(list(line))
        arr.append(list(line))
    if not done:
        # fill in the initials
        for j in range(R):
            empty_line = True
            for k in range(C):
                if arr[j][k] != '?':
                    empty_line = False
                    break
            if empty_line:
                for k in range(C):
                    fill_empty_line(arr, j, k)
                    #dump_arr(arr)
            else:
                for k in range(C):
                    if arr[j][k] == '?':
                        fill(arr, j, k)
                        #dump_arr(arr)
    
    print("Case #%d:" % (i + 1))
    dump_arr(arr)

    


