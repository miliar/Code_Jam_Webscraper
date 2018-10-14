results = []

lines = [x for x in open('D-large.in', 'rt').readlines()]
count = 0

num_of_cases = int(lines[count])
count += 1
for case_num in xrange(num_of_cases):
    print case_num
    blocks = int(lines[count])
    count += 1
    
    n_blocks = [float(x) for x in lines[count].split()]
    n_blocks.sort()
    count += 1
    
    k_blocks = [float(x) for x in lines[count].split()]
    k_blocks.sort()
    count += 1

    d_war = 0
    temp_k = [x for x in k_blocks]
    temp_n = [x for x in n_blocks]
    for ind in xrange(blocks):
        if ind == blocks - 1:
            # Last block. Real answer
            if temp_n[0] > temp_k[0]:
                d_war += 1
        else:
            n_min = temp_n[0]
            k_min = temp_k[0]
            k_max = temp_k[-1]
            
            if n_min > k_min:
                d_war += 1
                temp_n.pop(0)
                temp_k.pop(0)
            elif n_min > k_max:
                d_war += 1
                temp_n.pop(0)
                temp_k.pop(-1)
            else:
                temp_n.pop(0)
                temp_k.pop(-1)
                
    o_war = 0
    #print '8'*88
    for ind in xrange(blocks):
        #print n_blocks
        #print k_blocks
        #print o_war
        if ind == blocks - 1:
            # Last block.
            if n_blocks[0] > k_blocks[0]:
                o_war += 1
        else:
            n_min = n_blocks[0]
            n_max = n_blocks[-1]
            k_min = k_blocks[0]
            k_max = k_blocks[-1]
            
            if n_min < k_min:
                n_blocks.pop(0)
                k_blocks.pop(0)
            elif n_max > k_max:
                o_war += 1
                n_blocks.pop(-1)
                k_blocks.pop(0)
            else:
                # Make Ken lose his best, while Naomi lose the minimum
                for i in range(1, blocks):
                    k_try = k_blocks[-i]
                    n_block_list = [x for x in n_blocks if x > k_try]
                    if len(n_block_list) > 0:
                        n_ind = n_blocks.index(n_block_list[0])
                        n_blocks.pop(n_ind)
                        k_blocks.pop(-i + 1)
                        break

    results.append((d_war, o_war))
        
        
# Print results
output_file = file('res.txt', 'wt')
for ind, res in enumerate(results):
    d_res, o_res = res
    print 'Case #%d: %d %d' % (ind + 1, d_res, o_res)
    output_file.write('Case #%d: %d %d\n' % (ind + 1, d_res, o_res))
output_file.close()
