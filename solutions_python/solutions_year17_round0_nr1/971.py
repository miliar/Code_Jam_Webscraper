
def Flip(s,K):

    r = ''
    for idx in range(K):
        if s[idx] is '+':
            r += '-'
        else:
            r += '+'

    r += s[K:]

    return r

def Remove(s):

    for idx,v in enumerate(s):
        if v is '-':
            return s[idx:]

    return ''

def Solver(s,K):

    s = Remove(s)
    i = 0
    while len(s)>0:

        if len(s) <K:
            return 'IMPOSSIBLE'

        s = Flip(s,K)
        s = Remove(s)
        i += 1

    return i

def main():

    with open('A-large.in') as f:
        nums = int(f.readline())

        for i in xrange(nums):
            s,K = f.readline().strip().split()
            K = int(K)

            r = Solver(s,K)

            print "Case #{:d}: ".format(i+1)+str(r)

    #print Solver('---+-++-',3)
    #print Solver('+++++',4)
    #print Solver('-+-+-',4)

main()
