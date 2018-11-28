__author__ = 'mfranzen'
__input__ = 'A-small-attempt0.in'
__output__ = 'A-small-attempt0.out'

# read input
f = open(__input__, 'r')

# read number of instances
T = int(f.readline().strip())

GRID = 4

for t in range(T):
    # start of instance

    # first arrangement
    row_1 = int(f.readline().strip())
    for i in range(row_1 - 1):
        f.readline()
    cards_1 = f.readline().strip().split(' ')
    for i in range(GRID - row_1):
        f.readline()

    # second arrangement
    row_2 = int(f.readline().strip())
    for i in range(row_2 - 1):
        f.readline()
    cards_2 = f.readline().strip().split(' ')
    for i in range(GRID - row_2):
        f.readline()

    # card candidates
    candidates = set(cards_1).intersection(set(cards_2))

    # output generation
    if len(candidates) == 1:
        out = list(candidates)[0]
    elif len(candidates) > 1:
        out = "Bad magician!"
    else:
        out = "Volunteer cheated!"

    s = "Case #%d: %s\n" % (t+1, out)
    with open(__output__, 'a') as o:
        o.write(s)