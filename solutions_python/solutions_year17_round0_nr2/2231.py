# small input
# 1 <= N <= 100


# large input
# 1 <= N <= 10^18


# O(lgN)
def general(N):
    """
    Returns the largest tiddy number that is
      less than or equal to N.
    """
    
    N_str = str(N)
    L = len(N_str)
    
    # Let N[i] denote the ith digit of N
    #   with N[0] being the leftmost digit of N
    #
    # Note that N[i] == int(N_str[i])
    
    # find the d s.t. N[d-1] > N[d]
    d = 1
    while d < L:
        if int(N_str[d-1]) > int(N_str[d]):
            break
        d += 1
    
    if d == L:
        return N
    
    # N[d-1] > N[d]
    
    # find c s.t. all digits N[c..(d-1)] are equal
    c = d-1
    const = int(N_str[c])
    while c-1 >= 0:
        if int(N_str[c-1]) != const:
            break
        c -= 1
    
    if c == 0:
        # c == 0 is handled appropriately
        # by the subsequent code
        pass
    
    # N[c-1] != N[c]
    # N[c..(d-1)] == const
    
    non_decreasing_part = N_str[:c]
    constant_part       = str( int(N_str[c]) - 1 ) + '9' * ( (d-1) - (c+1) + 1 )
    trailing_nines      = '9' * ( (L-1) - (d) + 1 )
    
    return int(non_decreasing_part + constant_part + trailing_nines)


# O(N*MlgM)
def bruteforce(N):
    
    candidate = N
    while candidate > 0:
        if is_tidy(candidate):
            return candidate
        candidate -= 1

# O(MlgM)
# - where M == O(lg(num)) == len(str(num))
def is_tidy(num):
    return sorted(str(num)) == list(str(num))


# def small(N):
#     return general(N)


# def large(N):
#     return general(N)


def t(L=1, R=100):
    """
    Tests the general solution against the bruteforce solution
      for the range(L, R+1).
    """
    
    assert 1 <= L <= R
    
    for N in range(L, R+1):
        assert general(N) == bruteforce(N), "%d" % N