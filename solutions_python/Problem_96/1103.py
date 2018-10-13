def calcBest(s):   
    b = s / 3
    if (s % 3) > 0:
        b += 1
    return b

def calcBestSur(s):
    if s == 0:
        return 0
    
    b = s / 3
    if (s % 3) == 2:
        b += 2
    else:
        b += 1
    return b


num_cases = int(raw_input())

for case in range(num_cases):
    in_str = raw_input()
    data = in_str.split()
    data = map(lambda x: int(x), data)
    N = data[0]
    S = data[1]
    p = data[2]
    t = data[3:len(data)]
    t.sort()
    counter = 0
    for score in t:
        if calcBest(score) >= p:
            counter += 1
        elif S > 0:
            if calcBestSur(score) >= p:
                counter += 1
                S -= 1
    print "Case #{0}: ".format(case+1) + str(counter) 
        

    
    
