#!/usr/bin/python

def get_min(iterable):
    """Gets the minimum non-None in iterable"""
    l = [i for i in iterable if i is not None]
    return min(l) if len(l) > 0 else None

def strips(lawn, rows, cols):
    for i in xrange(cols):
        yield slice(i, None, cols)
    for i in xrange(rows):
        yield slice(i * cols, (i + 1) * cols)

def unmow(lawn, rows, cols, height):
    """ Replace some height-high strip of the lawn with a None strip.
    
    If there is any strip of the lawn (row or column) with only values of
    height and None, replace one such strip with only values of None. This
    preserves the "mowability" of the lawn if run on the minimum height.
    Return False if this could not be done, True otherwise.
    """
    
    for strip in strips(lawn, rows, cols):
        grass = lawn[strip]
        if height in grass and set(grass) <= {height, None}:
            lawn[strip] = [None] * len(grass) # Use lawn[strip] to avoid copy
            return True
    
    # No strip matched
    return False

def attempt(lawn, rows, cols):
    current = get_min(lawn) # Not None at this point
    while unmow(lawn, rows, cols, current):
        current = get_min(lawn)
        if current is None:
            return True
    # Here, we must have called unmow, which returned False.
    return False

def main():
    num_cases = int(raw_input())
    for case in xrange(num_cases):
        # Get size
        rows, cols = (int(s) for s in raw_input().split())
        
        # Get lawn
        lawn = []
        for row in xrange(rows):
            lawn += [int(s) for s in raw_input().split()]
        
        # Try mowing
        results = {"num": case + 1,
                   "status": "YES" if attempt(lawn, rows, cols) else "NO"}
        print "Case #{num}: {status}".format(**results) 
        
        

if __name__ == "__main__":
    main()
