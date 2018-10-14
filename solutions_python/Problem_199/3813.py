#!/usr/bin/env python3

# ######################################################################

def main():
    for i, (seq, k) in enumerate( getinput() ):
        print( 'Case #' + str(i+1) + ':', nflips(seq, k) )
    return

# ######################################################################

def nflips(seq, k):
    n = 0
    # Work from left to right.
    for i in range( len(seq) ):
        # Stop when we hit the edge.
        if len( seq[i:i+k] ) < k:
            break
        # If this pancake needs to be flipped, flip it.
        if seq[i] == '-':
            seq = seq[:i] + flip( seq[i:i+k] ) + seq[i+k:]
            n += 1
    # Check if everything was flipped successfully.
    return n if all( x == '+' for x in seq ) else 'IMPOSSIBLE'

# ----------------------------------------------------------------------

def flip(seq):
    return ''.join( {'-':'+', '+':'-'}[x] for x in seq )

# ######################################################################

def getinput():
    n = int( input() )
    for _ in range(n):
        seq, k = input().split()
        yield seq, int(k)

# ######################################################################

if __name__ == '__main__':
    main()
