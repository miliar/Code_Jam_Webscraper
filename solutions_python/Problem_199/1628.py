# Google Code Jam 2017 Qualifying A
# Last flip requires k consecutive -.
# It looks like naive flipping is optimal?  And maybe if naive
# flipping fails it's impossible?
'''
+-+-+-+- 2
++--+-+-
+++++-+-
++++++--
++++++++
+--+---- 2
++++----
++++++--
++++++++
+-+-+-+- 4
++-+--+-
+++-+++-
++++----
++++++++
+--++--+ 4
+++----+
++++++++
+--+---+ 4
+++-+--+
++++-+++
+++++--- fail
+--+---+ 4
+---++++ not naive fail
Try to concoct example where naive is suboptimal.
+--++---+ 3
+++-+---+
++++-+--+
+++++-+-+
++++++-++ fail
Try starting with final state and working backwards to find suboptimal
naive case.
+++++++++ 3 backwards
+++---+++
+++--+--+ OK, solve
+++++---+
+++++++++ optimal
+++-++-++
I should try to prove it's optimal.  With each step you're fixing at
least the first pancake you flip.
+++++++++ 5 backwards
++-----++
++--+++--
OK, naive looks optimal, this is easy.
Need to recognize failure.
Fail if first - is less than flipper width from end.
Can we delete leading plusses?  Yes.
'''

def flip(row, flipperWidth):
    # Flip the first flipperWidth pancakes.
    for i in range(flipperWidth):
        row[i] = not row[i]
    
def doCase(s):
    row = [c == '+' for c in s[0]] # Make list of bool
    flipperWidth = int(s[1])
    numFlips = 0
    while False in row:
        i = row.index(False)
        row = row[i:]           # Discard leading happy pancakes
        if flipperWidth > len(row):
            return 'IMPOSSIBLE'
        flip(row, flipperWidth)
        numFlips += 1
    return numFlips

cases = int(raw_input())
for i in range(cases):
    print 'Case #{}: {}'.format(i+1, doCase(raw_input().strip().split()))
