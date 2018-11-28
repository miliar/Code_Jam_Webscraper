prob = "a"
size = "large"

f = open('{0}-{1}.in'.format(prob, size))
o = open('{0}-{1}.out'.format(prob, size), 'w+')
n = int(f.readline());

for t in range(n):
    line = f.readline().replace("\n", '')
    
    count = int(line[:1])
    
    temp_ins = line.split()
    ins = []

    bots = {
        'O': {
            'position': 1,
            'buttons': []
        },
        'B': {
            'position': 1,
            'buttons': []
        }
    
    }
    
    for j in range(1,len(temp_ins), 2):
        bots[temp_ins[j]]['buttons'].append(int(temp_ins[j+1]))
        ins.append((temp_ins[j], int(temp_ins[j+1])))
    
    o_btn_count = len(bots['O']['buttons'])
    b_btn_count = len(bots['B']['buttons'])
        
    if o_btn_count > b_btn_count or o_btn_count == b_btn_count:
        l_range = o_btn_count
    else:
        l_range = b_btn_count
    
    s = 0
    
    done = False
    while bots['O']['buttons'] or bots['B']['buttons']:
        
        next_button = ins[0];
        
        pushing = False
        for k in bots:
            if bots[k]['buttons']:    
                if bots[k]['position'] == bots[k]['buttons'][0]:
                    if pushing == False and next_button[0] == k and next_button[1] == bots[k]['buttons'][0]:
                        pushing = True
                        del(ins[0])
                        del(bots[k]['buttons'][0])
                    else:
                        continue
                else:
                    if bots[k]['position'] < bots[k]['buttons'][0]:
                        bots[k]['position'] = bots[k]['position'] + 1
                    else:
                        bots[k]['position'] = bots[k]['position'] - 1
        
        s = s+1
    
    o.write("Case #{0}: {1}\n".format(t+1, s))
