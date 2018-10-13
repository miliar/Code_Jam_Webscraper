import sys

def IsListSorted_sorted(lst):
    return sorted(lst) == lst

def check_sort(N):
    a = list()
    for i in str(N):
        a.append(int(i))
    #print a
    #print sorted(a)
    if IsListSorted_sorted(a):
        #print IsListSorted_sorted(a)
        return True 
    else:
        return False  
    
input_file = open("B-small-attempt0.in", "r")
output_file = open("B-small-attempt0.txt", "w")
sys.stdout = output_file
lines = input_file.readlines()
T = lines[0].rstrip('\n')
T = int(T)
for case in xrange(T):
    N = lines[case+1].rstrip('\n')
    N = int(N)
    while not check_sort(N):
        N = N-1
    print 'Case #%d: %s' % (case+1, N)