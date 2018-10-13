import math 


# def solve_p(p, k):
    # count = 0
    # if len(p) < k:
        # return 0
    
    # for j in range(min(k, len(p) - k)):
        # if not p[j]:
            # for t in range(k):                    
                # p[j+t] = not p[j+t]
            # count += 1
    # for j in range(len(p) - 1, len(p) - k, -1):
        # print(j)
        # if not p[j]:
            # for t in range(k):                    
                # p[j-t] = not p[j-t]
            # count += 1
    # import pdb; pdb.set_trace()
    # if False in p[0:k] or False in p[len(p) - k: len(p)]:
        # return 0
    
    # return count + solve_p(p[k:len(p) - k], k)
def solve_p(p, k, start, stop):
    count = 0
    if stop - start < k:
        return 0
    
    for j in range(start, min(start + k, stop - k)):
        if not p[j]:
            for t in range(k):                    
                p[j+t] = not p[j+t]
            count += 1
    for j in range(stop - 1, stop - k - 1, -1):
        #print(j)
        if not p[j]:
            for t in range(k):                    
                p[j-t] = not p[j-t]
            count += 1
    #import pdb; pdb.set_trace()
    if False in p[start:k + start] or False in p[stop - k: stop]:
        return 0
    return count + solve_p(p, k, start + k, stop - k)
    #return count + solve_p(p, k, start + k, stop)

    
import sys
def main():
    input_file = open(sys.argv[1],'r')
    points = int(input_file.readline().strip())
    for i in range(points):
        splitted_row = input_file.readline().split()
        p,k = splitted_row
        p = [pp=='+' for pp in p]
        k = int(k)
        
        
        count = solve_p(p, k, 0, len(p))
        #print p
        print 'Case #%d:' % (i+1,), count if False not in p else 'IMPOSSIBLE'
        

if __name__ == '__main__':
    main()