import sys
import copy
import heapq

def regular( data ):
    return filter( lambda x: x!=0, [d+1 for d in data])

def special( data, factor ):
    if set(data) == set([-1]):
        return []
    result = heapq.heappop( data )
    val1, val2 = result/factor, (result - result/factor)
    heapq.heappush( data, val1)
    heapq.heappush( data, val2)
    return filter( lambda x:x!=0, data )

# def do_special( data ):
#     if len(data)> 1 and abs(data[0])/2 >= abs(data[1]) and (abs(data[0]) > 3):
#         return True
#     return (abs(data[0]/2) > len(data))

def solve( data, count, largest ):
    #print 'Data: %s, Count: %d'%(data, count)
    if not data:
        return count 
    if count > largest:
        return largest
    result = regular(data)
    heapq.heapify(result)
    brute_solve = solve( result, count+1, largest)
    if brute_solve == count+1:
        return brute_solve
    d1 = special( copy.copy( data ), factor=2 )
    d2 = special( copy.copy( data ), factor=3 )
    close_solve2 = solve( d1, count+1, largest )
    close_solve3 = solve( d2, count+1, largest )
    return min ( brute_solve , close_solve2, close_solve3 )

with open(sys.argv[1]) as f:
    num_cases = int(f.readline().rstrip())
    case = 0
    while num_cases:
        num_cases -= 1
        case +=1
        d = f.readline()
        data = [ -1*int(x) for x in f.readline().rstrip().split()]
        heapq.heapify( data )
        #print 'Data: ', data
        largest = abs(data[0] )
        print "Case #%d: %d" % (case, min( solve(data,0, largest), largest ) )
