import sys
fp = file(sys.argv[1])
#fp = open("test.in")

#read nb of cases
T = int(fp.next())

for i in range(T):
    line = list(fp.next().split())
    N = int(line[0])
    colors = {'B':[],'O':[]}
    orders = []
    timer = 0
    positions = {'B':1,'O':1}
    for j in range(N):
        col = line[2*j+1]
        pos = int(line[2*j+2])
        orders.append((col,pos))
        colors[col].append(pos)

    while(len(orders)>0):
        current_order = orders.pop(0)
        curr_col = current_order[0]
        curr_pos = current_order[1]
        time_taken = abs(curr_pos - positions[curr_col])+1
        timer += time_taken
        colors[curr_col].pop(0)
        positions[curr_col] = curr_pos
        if curr_col == 'B':
            if len(colors['O']) > 0:
                target_pos = colors['O'][0]
                time_nec = abs(target_pos-positions['O'])
                if time_nec <= time_taken:
                    positions['O'] = target_pos
                else:
                    if target_pos < positions['O']:
                        positions['O'] = positions['O']-time_taken
                    else:
                        positions['O'] = positions['O']+time_taken
        else:
            if len(colors['B']) > 0:
                target_pos = colors['B'][0]
                time_nec = abs(target_pos-positions['B'])
                if time_nec <= time_taken:
                    positions['B'] = target_pos
                else:
                    if target_pos < positions['B']:
                        positions['B'] = positions['B']-time_taken
                    else:
                        positions['B'] = positions['B']+time_taken
        
    print "Case #%d: %d" % (i+1, timer)
    
fp.close()
