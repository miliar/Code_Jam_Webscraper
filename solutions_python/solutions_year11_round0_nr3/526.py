from functools import partial
from itertools import permutations, combinations
from operator import xor

log = open('log.txt', 'w')

def writeLog(s):
    pass
    #writeLog(s)
    
def memoize(f, cache={}):
    def g(*args, **kwargs):
        key = (f, tuple(args), frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = f(*args, **kwargs)
        return cache[key]
    return g

def recursive_sum(nested_num_list): 
    if len(nested_num_list) == 1:
        return nested_num_list[0]
    return nested_num_list[0] + recursive_sum(nested_num_list[1:])

def recursive_xor(nested_num_list): 
    if len(nested_num_list) == 1:
        return nested_num_list[0]
    return nested_num_list[0] ^ recursive_xor(nested_num_list[1:])

#mreduce = memoize(recursive_xor)
mreduce = memoize(partial(reduce, xor))
msum = memoize(sum)
    
if __name__=='__main__':    
    input_file = open('C-small-0.in', 'r')
    output_file = open('C-small-0.out', 'w')
    
    for line_num, line in enumerate(input_file.readlines()[2::2]):
        candy = map(int, line.split())
        max_sum = -1
        for i in range(1, len(candy)):
            c = combinations(candy, i)
            for i in c:
                i = i
                otherlist = list(candy)
                for b in i:
                    otherlist.remove(b)
                writeLog( (i, otherlist))
                XORer, summer = reduce(xor, i), sum(otherlist)
                if  XORer == summer:
                    sumOfP = sum(i)
                    if max_sum < sumOfP:
                        max_sum = sumOfP
                
        if max_sum==-1:
            candy_value='NO'
        else:
            candy_value=str(max_sum)
        print >>output_file,'Case #%s: %s' % (line_num+1, str(candy_value))#>>output_file, 
    log.close()
    input_file.close()
    output_file.close()
