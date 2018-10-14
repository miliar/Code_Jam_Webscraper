def getAns(v1, v2):
    # perm 1: first sorted and second backsorted
    permutationV1 = v1[:]
    permutationV2 = v2[:]
    
    permutationV1.sort()
    permutationV2.sort(reverse=True)
    
    min = scalar(permutationV1, permutationV2)
    
    # perm 2
    permutationV1 = v1[:]
    permutationV2 = v2[:]
    
    permutationV1.sort(reverse=True)
    permutationV2.sort()
    
    k = scalar(permutationV1, permutationV2)
    
    if k < min:
        min = k
        
    return min
    
    
    
def cmpInverse(a, b):
    if a > b:
        return -1
    if a == b:
        return 0
    else:
        return 1

def scalar(v1, v2):
    sum = 0
    for i in range(len(v1)):
        sum += (v1[i] * v2[i])
    return sum
        
    
if __name__ == "__main__":
    testCases = int(raw_input())
    
    for k in range(1, testCases + 1):
        vectorLen = int(raw_input())
        
        v1 = []
        v2 = []
        # Get v1
        tv1 = str(raw_input()).split(' ')
        tv2 = str(raw_input()).split(' ')
        
        for i in tv1:
            v1.append(int(i))
            
        for i in tv2:
            v2.append(int(i))
                
      #  print 'Got v1: %s' % v1
      #  print 'Got v2: %s' % v2
        
        ans = getAns(v1, v2)
        print 'Case #%d: %d' % (k, ans)