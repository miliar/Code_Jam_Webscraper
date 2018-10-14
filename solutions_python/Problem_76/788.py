import sys

def splitPossible(candies):
    return reduce(lambda x, y:x^y, candies) == 0

def loop(ran):
    
    counter = [0] * len(ran)
    
    while True:
        yield counter

        for i in range(len(ran)-1, -1, -1):
            counter[i] += 1
            if(counter[i] < ran[i]): break
            counter[i] = 0
            if(i == 0): return
            
def main():
    cases = int(raw_input())    
    for c in xrange(1, cases+1):
        raw_input()
        candies = map(int, raw_input().split())
        
        candies.sort(reverse=True)
        
        result = 'NO'
        if splitPossible(candies):            
            for split in loop([2]*len(candies)):
                bags = [0, 0]
                sums = [0, 0]
                for i in xrange(len(candies)):
                    bags[split[i]] ^= candies[i]
                    sums[split[i]] += candies[i]
                
#                print split
                if bags[0] == bags[1] and 0 in split and 1 in split:
#                    print bags, sums
                    result = str(max(sums))
                    break
           
        print "Case #%d: %s"%(c, result)
#        print >> sys.stderr, "Case #%d: %d"%(c, result)
        
if __name__ == '__main__':
    main()
    
#    for i in loop([2, 2]):
#        print i
