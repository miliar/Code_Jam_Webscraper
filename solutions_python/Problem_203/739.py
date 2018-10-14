f = open("input_smallA.txt", "r")
text  = f.readlines()

first = text[0].rstrip('\n').split(' ')
T = int(first[0])

lineNum = 1
case = 1
for i in range(T):
    split = text[lineNum].rstrip('\n').split(' ')
    lineNum += 1
    R = int(split[0])
    C = int(split[1])
    

    bottom = {}
    top = {}
    left = {}
    right = {}


    A = [['?' for j in range(C)] for x in range(R)]

    def addEntry(r, c, x):
        if x not in bottom:
            bottom[x] = r
            top[x] = r
            left[x] = c
            right[x] = c
        else:
            bottom[x] = max(bottom[x], r)
            top[x] = min(top[x], r)
            left[x] = min(left[x], c)
            right[x] = max(right[x], c)


    for j in range(R):
        split = text[lineNum].rstrip('\n')
        lineNum += 1
        for k in range(C):
            if split[k] != "?":
                A[j][k] = split[k]
                addEntry(j, k, A[j][k])
    
    for nm in bottom.keys():
        for j in range(top[nm], bottom[nm]+1):
            for k in range(left[nm], right[nm]+1):
                A[j][k] = nm

    for nm in bottom.keys():
        while True:
            found = False
            def check(left, top, bottom, right):
                if left < 0 or right >= C or top < 0 or bottom >= R:
                    return False
                for j in range(top, bottom+1):
                    for k in range(left, right+1): 
                        if A[j][k] != '?': 
                            return False
                return True

            def apply(left, top, bottom, right, x):
                for j in range(top, bottom+1):
                    for k in range(left, right+1): 
                        A[j][k] = x
            x = nm
            if check(left[x], top[x] - 1, top[x]-1, right[x]):
                apply(left[x], top[x] - 1, top[x]-1, right[x], x)
                top[x] = top[x] -1
                found = True

            if check(left[x] - 1, top[x], bottom[x], left[x]-1):
                apply(left[x] - 1, top[x], bottom[x], left[x]-1, x)
                left[x] = left[x] -1
                found = True

            if check(right[x]+1, top[x], bottom[x], right[x] + 1):
                apply(right[x]+1, top[x], bottom[x], right[x] + 1, x)
                right[x] = right[x] + 1
                found = True

            if check(left[x], bottom[x]+1, bottom[x]+1, right[x]):
                apply(left[x], bottom[x]+1, bottom[x]+1, right[x], x)
                bottom[x] = bottom[x] + 1
                found = True

            if not found:
                break

        
    print "Case #{}:".format(case)

    for j in range(R):
        row = ""
        for k in range(C):
            row += A[j][k]
        print row
    case += 1
