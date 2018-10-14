#Henry Maltby
#Code Jam 2017

def flip(pancakes, k, i):
    """
    Flips the k pancakes starting at i.
    """
    for j in range(k):
        pancakes[i + j] = '-' if pancakes[i + j] == '+' else '+'
    return pancakes

def oversized_pancake_flipper(pancakes, k):
    """
    Employs greedy algorithm to determine desired minimal number of flips. 
    This works because given a sequence of moves turning all pancakes to '+' 
    that is of minimal length,
        1. All moves are self-inverse.
        2. All moves commute with each other.
        3. The order of moves does not matter. (Follows from (2))
        4. The leftmost move takes place at the first '-'. (Follows from (1))
    And (3) and (4) are precisely what is needed for a proof by induction on 
    the size of the sequence.

    Runtime: O(n * k)
    """
    i, n = 0, len(pancakes)
    counter = 0
    while i + k <= n:
        if pancakes[i] == '-':
            pancakes = flip(pancakes, k, i)
            counter += 1
        i += 1
    if '-' in pancakes:
        return "IMPOSSIBLE"
    return str(counter)

def A():
    """
    Runs the problem as dictated in problem spec.
    """
    f = open('A-large.in')
    g = open('A-large.out', 'w')

    T = int(f.readline())
    for i in range(T):
        s, k = f.readline().strip().split(' ')
        ans = oversized_pancake_flipper(list(s), int(k))
        g.write("Case #" + str(i + 1) + ": " + ans)
        if i != T - 1:
            g.write("\n")

A()
