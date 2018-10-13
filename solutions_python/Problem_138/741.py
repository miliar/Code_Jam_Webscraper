'''
Created on Apr 12, 2014

@author: learning-python
'''

def zero_point_situation(n, k):
    return n[-1] < k[0]

def has_larger (key, s2):
    '''
    Return boolean and smallest value in s2 larger then key (s2 is sorted)
    '''
    for value in s2:
        if value > key:
            return True, value
    return False, None

def can_win_every_point(n, k):
    for i in range(len(n)):
        if n[i] < k[i]:
            return False
    return True


def make_move (n_move, k_move, n, k):
    n.remove(n_move)
    k.remove(k_move)
    return n, k

def honest_total(n, k):
    '''
    Iterate through n in descending order
    For each value, check if k can beat and return smallest k that can
    If not, k burns smallest block
    '''
    total = 0
    for i in range(len(n)):
        n_move = n[-1]
        k_can_beat, k_move = has_larger(n_move, k)
        if not k_can_beat:
            k_move = k[0]
            total += 1
        n, k = make_move(n_move, k_move, n, k)
    return total
        
def dishonest_total(n, k):
    '''
    Iterate through k in descending order
    If n has a value less then k, assume k is used and burn smallest n
    '''
    if can_win_every_point(n, k):
        return len(n)
    while len(n) != 0:
        largest_k = k[-1]
        smallest_n = n[0]
        n, k = make_move(smallest_n, largest_k, n, k)
        if (can_win_every_point(n, k)):
            return len(n)
    return 0
        

if __name__ == '__main__':
    lines = [line.strip() for line in open("test_input2", "r")]
    
    
    tests = lines[1:]
    threes = lambda l: (l[i:i + 3] for i in range(0, len(l), 3))
    process = lambda s: sorted(s.split(" "))
    test_cases = [(process(n), process(k)) for num, n, k in threes(tests)]
    
    for index, values in enumerate(test_cases):
        n, k = values
        copy_n, copy_k = list(n), list(k)
        honest = honest_total(n, k)
        dishonest = dishonest_total(copy_n, copy_k)
        print ("#%d: %d %d" % (index + 1, dishonest, honest))