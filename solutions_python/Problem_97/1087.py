#C prob

import sets

def Recycled():
    test_cases = int(raw_input())
    temp_set = sets.Set()
    for test in range(test_cases):
        A,  B =  raw_input().split()
        count = 0
        no_digits = len(A)
        A,  B  = int(A),  int(B)
        start,  end = A,  B
        while start  != end:
            for i in range(1, no_digits):
                new_no = (start % (10 ** i)) * (10 ** (no_digits - i)) + (start / (10 ** i))
                #print new_no,  
                if start< new_no <= B:
                    temp_set.add(new_no)
            
            count += len(temp_set)
            temp_set.clear()
            start += 1
        
        print 'Case #%d:'%(test+1), count
    return
    
if __name__ == '__main__':
    Recycled()
