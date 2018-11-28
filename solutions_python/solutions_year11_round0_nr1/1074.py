INPUT = """
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
"""

OUTPUT = """
Case #1: 6
Case #2: 100
Case #3: 4
"""

import itertools

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=fillvalue, *args)

def solve(line):
    count, data = line.split(' ', 1)
    terms = data.rsplit(' ', int(count) * 2)
    b_ops = []
    o_ops = []
    for (index, (bot, pos)) in enumerate(grouper(2, terms)):
        if bot == 'O':
            o_ops.append((index, int(pos)))
        else:
            assert bot == 'B'
            b_ops.append((index, int(pos)))

    t = 0
    index = 0
    b_pos = 1
    o_pos = 1    
    while b_ops or o_ops:
        pressed = False

        if b_ops:
            b_op_index, b_next_pos = b_ops[0]
            if (not pressed) and (index == b_op_index) and (b_next_pos == b_pos):
                pressed = True
                #print t, "B press", b_pos
                b_ops = b_ops[1:] # B pressed button
            elif (b_next_pos > b_pos):
                b_pos += 1      # B move forward
                #print t, "B move", b_pos
            elif (b_next_pos < b_pos):
                b_pos -= 1      # B move backwards
                #print t, "B move", b_pos
            else:
                #print t, "B wait", b_pos
                pass            # B waiting
            
                

        if o_ops:
            o_op_index, o_next_pos = o_ops[0]
            if (not pressed) and (index == o_op_index) and (o_next_pos == o_pos):
                pressed = True
                #print t, "O press", o_pos
                o_ops = o_ops[1:] # B pressed button
            elif (o_next_pos > o_pos):
                o_pos += 1      # B move forward
                #print t, "O move", o_pos
            elif (o_next_pos < o_pos):
                o_pos -= 1      # B move backwards
                #print t, "O move", o_pos
            else:
                #print t, "O wait", o_pos
                pass            # B waiting
            
        t += 1
        
        if pressed:
            index += 1

    return t
                
        


lines = open("input.txt", "rt").xreadlines()
num_problems = int(next(lines))
lines = list(lines)
assert num_problems == len(lines)

out = open("output.txt", "wt")
for (n, line) in enumerate(lines):
    s = "Case #%d: %d\n" % (n+1, solve(line))
    print s,
    out.write(s)

out.close()
              
