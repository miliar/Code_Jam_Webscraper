def initialize_cake(m_in, R, C):
    
    _, rr, _ = find_next_alpha(m_in)
    first_row_str_out = get_row_str(m_in, rr, R, C)
    
    m_out = []
    for _ in range(rr+1):
        m_out.append(first_row_str_out)
    
    prev_row_str_out = first_row_str_out
    for r in range(rr+1, R):
        row_str_out = get_row_str(m_in, r, R, C)
        if row_str_out is None:
            m_out.append(prev_row_str_out)
        else:
            m_out.append(row_str_out)
            prev_row_str_out = row_str_out
    
    return m_out

def get_row_str(m, r, R, C):
    prev_a, prev_c = None, -1
    a,   _, c      = find_next_alpha(m, r, 0, R, C, just_in_row=True)
    if a is None:
        return None
    row_str_out = []
    while a:
        row_str_out.append( a*( c - (prev_c+1) +1 ) )
        prev_a, prev_c = a, c
        a,   _, c      = find_next_alpha(m, r, prev_c+1, R, C, just_in_row=True)
    row_str_out.append( prev_a*( (C-1) - (prev_c+1) +1 ) )
    row_str_out = ''.join(row_str_out)
    return row_str_out

def find_next_alpha(m, r=0, c=0, R=None, C=None, just_in_row=False):
    if R is None: R = len(m)
    if C is None: C = len(m[0])
    while r < R:
        while c < C:
            char = m[r][c]
            if char.isalpha():
                return char, r, c
            c += 1
        if just_in_row:
            return None, r, c
        c = 0
        r += 1
    return None, r, c