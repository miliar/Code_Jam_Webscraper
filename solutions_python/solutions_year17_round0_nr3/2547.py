def find_biggest_gap(bathroom) -> tuple: 
    """
    Find the biggest gap in the bathroom
    Return the two edge index as a tuple
    """
    gaps = list(set(''.join(bathroom).split("O")))
    biggest_gap = 0

    try:
        gaps.remove('')
    except ValueError as err:
        pass
    
    for gap in gaps:
        biggest_gap = max(biggest_gap, len(gap))
    
    l = ''.join(bathroom).find('.' * biggest_gap)
    r = l + biggest_gap - 1
    return l, r


def insert_one(bathroom, gap, last_one = False) -> str: 
    """
    param bathroom: the schedual string
    param gap: a tuple of two numbers, which are the edges of the gap
    return bathroom: the new schedual string
    """
    index = int(sum(gap) / 2)
    temp = list(bathroom)
    temp[index] = 'O'

    if last_one:
        # print("last one.")
        # print the min(L, R) & max(L, R) for this insertion
        return ''.join(temp), find_side_gaps(bathroom, index)
    else:
        return ''.join(temp)


def generate_init_bathroom(capacity) -> str:
    bathroom = list('.' * capacity)
    bathroom.insert(0, 'O')
    bathroom.append('O')
    return list('.' * capacity)


def find_side_gaps(bathroom, index) -> str:
    l = 500
    r = 500

    # fidn left gap distance
    l = len(''.join(bathroom[0:index]).split('O')[-1])
    
    # fidn right gap distance
    r = len(''.join(bathroom[index+1:]).split("O")[0])
    return(str(max(l, r)) + " " + str(min(l, r)) + "\n")
    