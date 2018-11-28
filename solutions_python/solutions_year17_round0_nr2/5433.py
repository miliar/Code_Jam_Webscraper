import math

def find_lowest_tn(s):
    for j in range(s, 0, -1):
        helper = j
        digits = []
        #puts digits of the number in a list in reverse order
        #example: 1234 becomes [4,3,2,1]
        while(not(helper == 0)):
            digits.append(helper % 10)
            helper = helper // 10
        #if list is non_increasing, this means number is non_decreasing(aka tidy)    
        if (is_non_increasing(digits)):
            return j 
        
        #for debug
        
                
def is_non_increasing(l):
    for i in range(len(l) - 1):
        if (l[i] < l[i + 1]):
            return False
    return True


if __name__ == '__main__':
    
    
    t = int(input())
    for i in range(1, t + 1):
        s = int(input()) 
        res = find_lowest_tn(s)        
        print("Case #{}: {}".format(i, res))