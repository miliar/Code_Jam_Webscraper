"""
Output
Case #1: 6
Case #2: 100
Case #3: 4
"""

input = """3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1"""

input = open('A-large.in').read()

def parse_input(input):
    input = input.strip().split('\n')
    num_cases = int(input[0])
    cases = []
    for j,row in enumerate(input[1:1+num_cases]):
        moves = {'O': [], 'B': []}
        blocks = []
        items = row.split(' ')
        for i in xrange(1, len(items)-1, 2):
            moves[items[i]].append(items[i+1])
            blocks.append(items[i])
        move(j+1, moves, blocks)

def move(case, moves, blocks):
    moves['O'] = moves['O'][::-1]
    moves['B'] = moves['B'][::-1]
    blocks = blocks[::-1]
    t = 0
    o_loc = 1
    b_loc = 1
    o_target = moves['O'] and int(moves['O'].pop())
    b_target = moves['B'] and int(moves['B'].pop())
    while blocks:
        blocker = blocks and blocks.pop()
        if blocker == 'O':
            dt = abs(o_target-o_loc)+1
            t += dt
            o_loc = o_target
            o_target = moves['O'] and int(moves['O'].pop())
            if b_target:
                if dt > abs(b_target-b_loc):
                    b_loc = b_target
                elif b_loc < b_target:
                    b_loc += dt
                elif b_loc > b_target:
                    b_loc -= dt
                else:
                    t += 1
                    b_target = moves['B'] and int(moves['B'].pop())
        elif blocker == 'B':
            dt = abs(b_target-b_loc)+1
            t += dt
            b_loc = b_target
            b_target = moves['B'] and int(moves['B'].pop())
            if o_target:
                if dt > abs(o_target-o_loc):
                    o_loc = o_target
                elif o_loc < o_target:
                    o_loc += dt
                elif o_loc > o_target:
                    o_loc -= dt
                else:
                    t += 1
                    o_target = moves['O'] and int(moves['O'].pop())
    print 'Case #%d: %d' % (case,t)


parse_input(input)
