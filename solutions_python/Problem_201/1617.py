import math

def get_left(a, i):
    for j in range(i-1, -1, -1):
        if a[j] == 1:
            return i - (j+1)
    return i

def get_right(a, i):
    for j in range(i+1, len(a)):
        if a[j] == 1:
            return j-1-i
    return len(a) - 1 - i

def brute_force(N, K):
    a = [0]*N
    maxMin = -1
    maxMax = -1
    for j in range(K):
        maxMin = -1
        maxMax = -1
        bestI = -1
        for i in range(N):
            if a[i] != 1:
                leftside = get_left(a, i)
                rightside = get_right(a, i)
                curMin = min(leftside, rightside)
                curMax = max(leftside, rightside)
                if curMin > maxMin or curMin == maxMin and curMax > maxMax:
                    maxMin = curMin
                    maxMax = curMax
                    bestI = i
        a[bestI] = 1
        #print a
    return maxMin, maxMax    

        
def stalls():
    f = open("input2_small3.txt", "r")
    text  = f.readlines()

    first = text[0].rstrip('\n').split(' ')
    T = int(first[0])

    case = 1
    for i in range(T):
        split = text[case].rstrip('\n').split(' ')
        N = int(split[0])
        K = int(split[1])
        # this is wrong

        numN = len("{0:0b}".format(N))
        numK = len("{0:0b}".format(K))
        left = 0
        right = 0
        if numN == numK:
            left = 0
            right = 0
        else:
            powertwo = 1<<(K.bit_length() - 1)
            position = K - powertwo
            evens = 0
            odds = 0
            if N % 2 == 0:
                evens = 1
            else:
                odds = 1


            num = N
            c = N
            f = N

            for i in range(numK-1):
                oodd = odds
                if c % 2 == 1:
                    oddN = c
                elif f % 2 == 1:
                    oddN = f
                else:
                    oddN = 5
                    
                if ((oddN-1)/2) % 2 == 0:
                    odds = evens
                    evens = evens + oodd*2
                else:
                    odds = evens + oodd*2
                    evens  = evens

                c = int(math.ceil((c-1)/2.0))
                f = int(math.floor((f-1)/2.0))

                #print odds, evens, c, f
                num = int(math.floor((num-1)/2.0))

            #print position, evens, odds
            greater = False
            if c % 2 == 0:
                greater = position < evens
            else:
                greater = position < odds
            

            if greater:
                left = int(math.floor((c-1)/2.0))
                right = int(math.ceil((c-1)/2.0))
            else:
                left = int(math.floor((f-1)/2.0))
                right = int(math.ceil((f-1)/2.0))

        curMax = max(left,right)
        curMin = min(left, right)

        '''
        bruteRes = brute_force(N, K)
        
        if curMin != bruteRes[0] or curMax != bruteRes[1]:
                    print "Case #{}: {} {} {} {}".format(
                        case, curMin, bruteRes[0], curMax, bruteRes[1])
        '''    
        print "Case #{}: {} {}".format(case, max(left, right), min(left,right))
        case +=1 

stalls()
                
