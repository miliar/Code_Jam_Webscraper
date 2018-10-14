import sys, bisect
from itertools import permutations

filename, extension = sys.argv[1].split('.')
assert(extension=='in')
src = open(sys.argv[1])
result = open(filename + '.out', 'wb')

num_tests = int(src.readline().rstrip())

def test_cool(eachline):
    for idx in range(len(eachline)):
        if eachline[idx]==eachline[(idx+1) % len(eachline)]:
            return False
    return True


def restore(iterates, G,V,O):
    output = []
    for each in iterates:
        output.append(each)
        if each=='B' and O>0:
            O -= 1
            output.append('O')
            output.append('B')
        if each=='R' and G>0:
            G -= 1
            output.append('G')
            output.append('R')
        if each=='Y' and V>0:
            V -= 1
            output.append('V')
            output.append('Y')
    return ''.join(output)

def check_possible(N, R, O, Y, G, B, V):
        for x1,x2,c1,c2 in [('O','B', O, B), ('G','R',G,R), ('V','Y',V,Y)]:
            if (c1==c2) and (c1+c2==N):
                sol = []
                for idx in range(c1):
                    sol += [x1,x2]
                return ''.join(sol)
        R_SP = R - 2*G
        Y_SP = Y - 2*V
        B_SP = B - 2*O
        if (R_SP<0) or (B_SP<0) or (Y_SP<0):
            return 'IMPOSSIBLE'
        R_ = R - G
        Y_ = Y - V
        B_ = B - O
        leftovers = sorted([('R',R_),('Y',Y_),('B',B_)], key = lambda x:x[1])
        # print '\n',leftovers
        if leftovers[2][1] > leftovers[0][1] + leftovers[1][1]:
            return 'IMPOSSIBLE'
        reduced_one = ['R']*R_ + ['Y']*Y_ + ['B']*B_

        reduced_one = []
        prev = '?'
        while len(reduced_one)< (R_ + Y_ + B_):
            leftovers = sorted(leftovers, key = lambda x:x[1])
            for j in range(2,0, -1):
                if (leftovers[j][0] != prev) and (leftovers[j][1]>0):
                    prev = leftovers[j][0]
                    reduced_one.append(prev)
                    leftovers[j] = (prev, leftovers[j][1]-1)
                    break


        for eachline in permutations(reduced_one):
            if test_cool(eachline):
                return restore(eachline, G, V, O)

for test_idx in range(1,num_tests+1):
    N, R, O, Y, G, B, V = [int(each) for each in src.readline().split(' ')]
    print '\n\nsolve (R=%s, Y=%s, B=%s), (G=%s, V=%s, O=%s)' % (R,Y,B,G,V,O)
    solution = check_possible(N, R, O, Y, G, B, V)
    print 'Sol:', solution
    result.write('Case #{}: {}\n'.format(test_idx, solution) )
