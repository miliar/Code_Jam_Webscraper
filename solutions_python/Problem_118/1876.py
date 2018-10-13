


def nextNum(num,index=0):
    if index >= len(num)/2+1:
        return set()
    else:
        result = set()
        for i in range(0,10):
            if i==0 and index == 0:
                continue
            else:
                num[index] = str(i)
                num[-(index+1)] = str(i)
                result.add(''.join(num))
                result = result.union(nextNum(num,index+1))
        return result
    
if __name__ == "__main__":
    t = input()
    
    orig = t
    output = []
    
    while True:
        gridsize = [j for j in raw_input().strip().split()]
        a = gridsize[0].__len__()
        b = gridsize[1].__len__()
        A = int(gridsize[0])
        B = int(gridsize[1])
        palindrome = set()
        allPalindromes = set()
        for number in xrange(a,b+1):
            palindrome = palindrome.union(nextNum(['1' for j in range(number)]))   
            
        #print 'len',b/2+1
        for number in xrange(1,b/2+2):
            allPalindromes = allPalindromes.union(nextNum(['1' for j in range(number)]))
        
        count = 0
        palindromeCopy = palindrome.copy()
        for num in palindromeCopy:
            numVal = int(num)
            if numVal<A or numVal > B:
                palindrome.remove(num)
                continue
            
        for num in allPalindromes:
            numVal = int(num)
            sqarePal = str(numVal * numVal)
            #print sqarePal
            #print palindrome
            if sqarePal in palindrome:
                count = count + 1
                    
        output.append('Case #'+str(orig - t + 1)+': '+str(count))
            
        
        t =t -1
        if t == 0:
            break
        
    for val in output:
        print val