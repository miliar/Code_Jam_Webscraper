from collections import defaultdict

# best_points = 0
# best_accumulator = None


# def backtrack(accumulator, choices, allowed, decided, taken, points, goal):
#     global best_points
#     global best_accumulator
#     if points > best_points:
#         best_points = points
#         best_accumulator = [x for x in accumulator]
#     if points == goal:
#         return

#     curr = len(accumulator)
#     if curr > n:
#         return
#     if curr in decided:
#         accumulator.append(decided[curr])
#         backtrack(accumulator, choices, allowed, decided, taken, points + 1, goal)
#         accumulator.pop()
#     else:
#         for choice in choices:
#             if choice in taken or (curr, choice) not in allowed:
#                 continue
#             accumulator.append(choice)
#             taken.add(choice)
#             backtrack(accumulator, choices, allowed, decided, taken, points + 1, goal)
#             taken.remove(choice)
#             accumulator.pop()
#             if best_points == goal:
#                 return
#         accumulator.append(None)
#         backtrack(accumulator, choices, allowed, decided, taken, points, goal)
#         accumulator.pop()


# def bishops(grid, n):
#     global best_points
#     global best_accumulator
#     best_points = 0
#     best_accumulator = None

#     diagonals = range(2 * n - 1)
#     decided = {}
#     for i, j in grid.keys():
#         upright = i + j
#         downright = n - i - 1 + j
#         decided[upright] = downright
#         diagonals.remove(downright)

#     allowed = {}
#     for i in xrange(n):
#         for j in xrange(n):
#             upright = i + j
#             downright = n - i - 1 + j
#             allowed[upright, downright] = True

#     backtrack([], diagonals, allowed, decided, set(), 0, 2 * n - 1)

#     def ij_from_diagonals(upright, downright, _ij={}):
#         if len(_ij) == 0:
#             for i in xrange(n):
#                 for j in xrange(n):
#                     ur = i + j
#                     dr = n - i - 1 + j
#                     _ij[ur, dr] = (i, j)
#         return _ij[upright, downright]

#     answer = {}
#     for ur, dr in enumerate(best_accumulator):
#         if dr is None:
#             continue
#         i, j = ij_from_diagonals(ur, dr)
#         answer[i, j] = True

#     return best_points, answer


# def rooks(grid, n):
#     global best_points
#     global best_accumulator
#     best_points = 0
#     best_accumulator = None

#     files = range(n)
#     decided = {}
#     for i, j in grid.keys():
#         decided[i] = j
#         files.remove(j)
#     allowed = {}
#     for i in xrange(n):
#         for j in xrange(n):
#             allowed[i, j] = True

#     backtrack([], files, allowed, decided, set(), 0, n)

#     answer = {}
#     for i, j in enumerate(best_accumulator):
#         if j is None:
#             continue
#         answer[i, j] = True
#     return best_points, answer

def bishops(grid, n):
    assignments = {}

    diagonals = range(2 * n - 1)
    choices = set(diagonals)

    for i, j in grid.keys():
        upright = i + j
        downright = n - i - 1 + j
        assignments[upright] = downright
        choices.remove(downright)

    priority = defaultdict(int)
    allowed = {}
    for i in xrange(n):
        for j in xrange(n):
            upright = i + j
            downright = n - i - 1 + j
            priority[upright] += 1
            allowed[upright, downright] = True

    unassigned = [d for d in diagonals if d not in assignments]
    unassigned.sort(key=lambda d: priority[d])
    for d in unassigned:
        asg = None
        for c in choices:
            if (d, c) in allowed:
                asg = c
                break
        if asg is not None:
            assignments[d] = c
            choices.remove(c)

    def ij_from_diagonals(upright, downright, _ij={}):
        if len(_ij) == 0:
            for i in xrange(n):
                for j in xrange(n):
                    ur = i + j
                    dr = n - i - 1 + j
                    _ij[ur, dr] = (i, j)
        return _ij[upright, downright]

    answer = {}
    for ur, dr in assignments.items():
        if dr is None:
            continue
        i, j = ij_from_diagonals(ur, dr)
        answer[i, j] = True

    return len(assignments), answer


def rooks(grid, n):
    assignments = {}

    files = range(n)
    choices = set(files)

    for i, j in grid.keys():
        assignments[i] = j
        choices.remove(j)

    unassigned = [d for d in files if d not in assignments]
    for d in unassigned:
        asg = None
        for c in choices:
            asg = c
            break
        if asg is not None:
            assignments[d] = c
            choices.remove(c)

    answer = {}
    for i, j in assignments.items():
        answer[i, j] = True

    return len(assignments), answer


def solve(grid, n):
    bish = {}
    for i in xrange(n):
        for j in xrange(n):
            if (i, j) in grid and (grid[i, j] == 'o' or grid[i, j] == '+'):
                bish[i, j] = True
    bss, bs = bishops(bish, n)

    rook = {}
    for i in xrange(n):
        for j in xrange(n):
            if (i, j) in grid and (grid[i, j] == 'o' or grid[i, j] == 'x'):
                rook[i, j] = True

    rss, rs = rooks(rook, n)
    combined = {}
    for i in xrange(n):
        for j in xrange(n):
            if (i, j) in bs and (i, j) in rs:
                combined[i, j] = 'o'
            elif (i, j) in bs:
                combined[i, j] = '+'
            elif (i, j) in rs:
                combined[i, j] = 'x'
    return bss + rss, combined


cases = int(raw_input())
for ctr in xrange(cases):
    ss = raw_input().split(" ")
    n = int(ss[0])
    m = int(ss[1])
    grid = {}
    for x in xrange(m):
        ss = raw_input().split(" ")
        r = int(ss[1]) - 1
        c = int(ss[2]) - 1
        grid[r, c] = ss[0]
    score, answer = solve(grid, n)
    changes = []
    for (i, j) in answer:
        if (i, j) not in grid or answer[i, j] != grid[i, j]:
            changes.append((answer[i, j], i, j))
    print "Case #{}: {} {}".format(ctr + 1, score, len(changes))
    for c, i, j in changes:
        print "{} {} {}".format(c, i + 1, j + 1)
