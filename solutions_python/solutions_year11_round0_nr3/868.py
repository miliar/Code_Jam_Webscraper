'''
Created on May 7, 2011

@author: paolovictor@gmail.com
'''
def solution(input):
    values = [int(s) for s in input.split()]
    n = len(values)
    
    num_subsets = 2 ** n - 1
    current_subset = 1

    sum_all = sum(values)
    max_possible = -1
    while current_subset < num_subsets:
        subset = set()
        i = current_subset
        k = 0

        sum_b = 0
        while i != 0:
            if i & (1 << k):
                subset.add(k)
                i ^= (1 << k)
                sum_b = sum_b ^ values[k]
            k += 1

        sum_a = 0
        sum_real = 0
        for i in xrange(len(values)):
            if not i in subset:
                sum_a = sum_a ^ values[i]
                sum_real += values[i]
                 
        if sum_a == sum_b and max_possible < sum_real:
            max_possible = sum_real

        current_subset += 1
        
    return max_possible > 0 and max_possible or "NO"
      
'''
3
5
1 2 3 4 5
3
3 5 6
3
1 2 3

'''      
      
if __name__ == '__main__':
    n = int(raw_input())
    i = 1

    while n > 0:
        raw_input() # skip N line
        
        print "Case #%d: %s" % (i, solution(raw_input()))

        n -= 1
        i += 1
