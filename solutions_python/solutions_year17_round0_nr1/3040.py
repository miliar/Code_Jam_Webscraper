num_cases = int(input())

for case in range(1,num_cases+1):
    pancakes, K = input().split()
    K = int(K)
    position = 0
    flips = 0
    possible = True

    cakestring = list(pancakes)

    while position + K <= len(cakestring):
        if cakestring[position] == '-':
            flips += 1
            for i in range(K):
                if cakestring[position+i] == '-':
                    cakestring[position+i] = '+'
                else:
                    cakestring[position+i] = '-'
#            print(cakestring)
        position += 1

    while position < len(cakestring):
        if cakestring[position] == '-':
            possible = False
            break
        position += 1

    if not possible:
        print("Case #%d: IMPOSSIBLE" % (case))
    else:
        print("Case #%d: %d" % (case,flips))
        
