f = open('A-large-0.in','r')
lines = f.readlines()
f.close()

f_out = open('A-large-0.out', 'w')

for idx, line in enumerate(lines):
    if idx == 0:
        continue

    line_p = line.replace("\n","").split(" ")

    o_cmds = []
    b_cmds = []
    
    i = 0
    line_p.pop(0)

    while len(line_p):
        if line_p.pop(0) == 'O':
            o_cmds.append((i,int(line_p.pop(0))))
        else:
            b_cmds.append((i,int(line_p.pop(0))))
        i = i + 1
    
    s = 0
    o = 1
    b = 1
    i = 0
    pushed = False
    while len(o_cmds) or len(b_cmds):
        pushed = False
        if len(o_cmds):
            if o != o_cmds[0][1]:
                if o < o_cmds[0][1]:
                    o = o + 1
                else:
                    o = o -1
            elif i == o_cmds[0][0]:
                pushed = True
                o_cmds.pop(0)
                i = i + 1
        if len(b_cmds):
            if b != b_cmds[0][1]:
                if b < b_cmds[0][1]:
                    b = b + 1
                else:
                    b = b - 1
            elif i == b_cmds[0][0] and pushed == False:
                pushed = True
                b_cmds.pop(0)
                i = i + 1
        s = s + 1

    
    print 'Case #%s: %s' % (idx, s)
    f_out.write('Case #%s: %s\n' % (idx, s))

f_out.close()
