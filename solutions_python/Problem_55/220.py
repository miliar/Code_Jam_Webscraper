'''
Created on May 8, 2010

@author: Darren
'''

if __name__ == "__main__":
    f = open("C-small-attempt0.in", "r")
    fout = open("C-small-attempt0.out", "w")
    # C, the number of test cases in the input file
    T = int(f.readline())
    for i in xrange(T):
        # R rollercoaster runs
        # k = capacity
        R, k, N = [int(x) for x in f.readline().split()]
        gs = [int(x) for x in f.readline().split()]
        
        result = 0
        index = 0
        total_riders = sum(gs)
        if total_riders <= k:
            result = total_riders * R
        else:
            for j in xrange(R):
                space_left = k
                while gs[index] <= space_left:
                    space_left -= gs[index]
                    result += gs[index]
                    index = (index + 1) % N

#        print result
        fout.write(''.join(('Case #', str(i+1), ': ', str(result), '\n')))
    fout.close()
    f.close()