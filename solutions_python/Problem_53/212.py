'''
Created on May 8, 2010

@author: Darren
'''

if __name__ == "__main__":
    f = open("A-large.in", "r")
    fout = open("A-large.out", "w")
    # C, the number of test cases in the input file
    T = int(f.readline())
    for i in xrange(T):
        N, K = [int(x) for x in f.readline().split()]
        on = True
        for j in xrange(N):
            if K % 2 == 0:
                on = False
                break
            else: K /= 2
        result = "ON" if on else "OFF"
#        print result
        fout.write(''.join(('Case #', str(i+1), ': ', result, '\n')))
    fout.close()
    f.close()