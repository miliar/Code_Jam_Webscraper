best_answer = {}

def patricksum(arr):
    return reduce(lambda x,y: x^y, arr, 0)

def best(available, set1sum=0, set2sum=0, set1=[], set2=[]):
    if len(available) == 0:
        if set1sum == set2sum and set1sum != 0:
            return sum(set1)
        else:
            return -1
    return max([
            best(available[1:], set1sum ^ available[0], set2sum, set1 + [available[0]], set2),
            best(available[1:], set1sum, set2sum ^ available[0], set1, set2  + [available[0]]),
                     ])
    
def calc(arr):
    ans = best(arr)
    if ans == -1:
        print "NO"
    else:
        print ans
    

n = int(raw_input())
for t in xrange(n):
    print "Case #%d:" % (t+1),
    a = raw_input()
    arr = map(int, raw_input().split())
    calc(arr)
