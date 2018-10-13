'''
Created on 22 apr 2017

@author: algestam
'''

def solve(D, horses):
    longest_time_to_finish = None
    
    for h in horses:
        dist = D-h['K']
        t = dist/float(h['S'])
        if not longest_time_to_finish or t > longest_time_to_finish:
            longest_time_to_finish = t
    return D/longest_time_to_finish

for case in xrange(input()):
    D, N = [int(c) for c in raw_input().split()]
    
    horses = []
    for horse in range(N):
        K, S = [int(d) for d in raw_input().split()]
        horses.append({'K': K, 'S': S})
    
    res = solve(D, horses)

    print "Case #%i: %.6f" % (case+1, res)