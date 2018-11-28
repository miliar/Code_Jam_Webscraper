import sys
import copy

def get_War_count(count, Ken, Naomi):
    War_count = 0
    for _ in range(count):
        if Ken[-1] < Naomi[-1]:
            Ken.pop(0)
            Naomi.pop()
            War_count += 1
        else:
            Ken.pop()
            Naomi.pop()
        #print Naomi
        #print Ken
    return War_count

def get_Deceitful_War_count(count, Ken, Naomi):
    War_count = 0
    for _ in range(count):
        if Ken[-1] < Naomi[-1]:
            Ken.pop()
            Naomi.pop()
            War_count += 1
        else:
            Ken.pop()
            Naomi.pop(0)
        #print Naomi
        #print Ken
    return War_count

def main():
    T = int(sys.stdin.readline())
    for case in range(1,T+1):
        
        count = int(sys.stdin.readline())
        line = sys.stdin.readline()
        Naomi_weight = map(float,line.split())
        line = sys.stdin.readline()
        Ken_weight = map(float,line.split())
        
        assert(len(Naomi_weight) == count)
        assert(len(Ken_weight) == count)
        #print sorted(Naomi_weight)
        #print sorted(Ken_weight)
        
        War_count = get_War_count(count, copy.copy(sorted(Ken_weight)), copy.copy(sorted(Naomi_weight)))
        Deceitful_War_count = get_Deceitful_War_count(count, copy.copy(sorted(Ken_weight)), copy.copy(sorted(Naomi_weight)))        
        print 'Case #%d: %d %d' %(case, Deceitful_War_count, War_count)   
              
main()
'''
Input
  	

4
[0.5]
[0.6]
[0.2, 0.7]
[0.3, 0.8]
[0.1, 0.5, 0.9]
[0.3, 0.4, 0.6]
[0.186, 0.3,   0.389, 0.557, 0.832, 0.899, 0.907, 0.959, 0.992]
[0.215, 0.271, 0.341, 0.458, 0.52,  0.521, 0.7,   0.728, 0.916]

Output

Case #1: 0 0
Case #2: 1 0
Case #3: 2 1
Case #4: 8 4

'''
