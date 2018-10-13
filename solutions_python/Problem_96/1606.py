'''
Created on Apr 14, 2012

@author: Josh
'''

def possible_higher (threshold, total):
    possible_surprise = 0
    possible_standard = 0
    
    low = max(0, int(round(float(total)/3)) - 1)
    
    r_max = min(10, low + 2) + 1
    
    for i in range(low, r_max):
        for j in range(i, r_max):
            for k in range(j, r_max):
                if i + j + k == total and k >= threshold:
                    if k - i == 2:
                        possible_surprise = 1
                    else:
                        possible_standard = 1
    
    if possible_standard == 1:
        possible_surprise = 0
    
    return possible_standard, possible_surprise


#print possible_higher(8, 29)

if __name__ == '__main__':
    input_file = open ('two.txt', 'r')
    output_file = open('two_out.txt', 'w')
    
    cases = int(input_file.readline())
    
    for idx, line in enumerate(input_file, 1):
        non_surprise_higher = 0
        surprise_higher = 0
        nums = line.split()
        num_googlers = int(nums[0])
        num_surprises = int(nums[1])
        threshold = int(nums[2])
        scores = [int(x) for x in nums[3:]]
        
        print num_googlers, num_surprises, threshold, scores
        
        for score in scores:
            standard, surprises = possible_higher(threshold, score)
            surprise_higher += surprises
            non_surprise_higher += standard
        
        result = non_surprise_higher + min(num_surprises, surprise_higher)
        print non_surprise_higher, surprise_higher
        s = 'Case #%i: %s \n' % (idx,result)
        print s
        output_file.writelines([s])



''' 
4 (number of cases)
N S p t1 t2 t3 ...
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21

Case #1: 3
Case #2: 2
Case #3: 1
Case #4: 3
'''