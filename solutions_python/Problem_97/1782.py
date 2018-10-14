def move_to_front(n, s):
    '''(int, int) -> int
    Given integers n and s, moves the last n digits of the integer s to
    the front of the number, and returns this new number.
    '''
    if n == 0:
        return s
        
    s = str(s)
    res = s[-n:] + s[:len(s)-n]
    
    return int(res)
    
    
def check_pairs(pairs):
    '''(list of ints) -> NoneType
    Checks if the list pairs contains tuples (n, m) where n and m
    satisfy basic conditions for the recycled pairs problem. This
    is on the fly, just adding checks one at a time.
    '''
    for pair in pairs:
        assert pair[0] < pair[1], 'Failed in check_pairs.'
        
    # Found the problem, this was the check I needed.
    # "Yes, we're sure about the output to Case #4."
    assert set(pairs) == pairs, 'Duplicate pair in count.'

    
def count_recycled_pairs(A, B=None):
    '''(int, int) -> int
    Given integers A and B with the same number of digits and no leading
    zeroes, counts the number of distinct recycled pairs (n, m) there
    are with A <= n < m <= B and returns this count.
    '''
    if not B:
        return 0
    
    len_digits = len(str(A))
        
    n = A
    pairs = []
    
    while n < B:
        m = n + 1
        while m <= B:
            for k in range(1, len_digits):
                if m == move_to_front(k, n):
                    pairs.append((n, m))
            m += 1
        n += 1
        
    pairs = set(pairs)
    check_pairs(pairs)
    return len(pairs)
    
def convert_to_ints(line):
    '''Lazy.'''
    for k in range(len(line)):
        try:
            line[k] = int(line[k])
        except:
            pass
    
    
if __name__ == "__main__":
    # assert 1 == move_to_front(0, 1)
    # assert 1 == move_to_front(1, 1)
    # assert 32 == move_to_front(1, 23), 'Length 2 case failed.'
    # assert 12345 == move_to_front(0, 12345)
    # assert 34512 == move_to_front(3, 12345)
    
    # assert count_recycled_pairs(1, 9) == 0, 'Case 1 failed.'
    # assert count_recycled_pairs(10, 40) == 3, 'Case 2 failed.'
    # assert count_recycled_pairs(100, 500) == 156, 'Case 3 failed.'
    # assert count_recycled_pairs(1111, 2222) == 287, 'Case 4 failed.'
    
    f = open('C-small-attempt0.in')
    num_test_cases = f.readline()
    c = 1
    
    output = open('C-small-output.txt', 'w')
    
    for line in f:
        line = line.split()
        convert_to_ints(line)
        x = "Case #{}: {}" .format(c, count_recycled_pairs(line[0], line[1]))
        output.write(x + '\n')
        c += 1
        