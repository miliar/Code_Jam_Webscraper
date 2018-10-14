magic = {'a': [17], ' ': [7, 10, 15], 'c': [3, 11], 'e': [1, 6, 14], 'd': [13], 'j': [16], 'm': [5, 18], 'l': [2], 'o': [4, 9, 12], 't': [8], 'w': [0]}
init_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

lines = input()
for z in xrange(0, lines):
    line = raw_input()
    counts = list(init_counts)
    for x in xrange(-1,0-1-len(line),-1):
        if line[x] in magic:
            for pos in magic[line[x]]:
                counts[pos] = (counts[pos] + counts[pos+1]) % 10000
#                print line[x], counts, pos, counts[pos], counts[pos+1], len(counts)
    print ("Case #"+str(z+1)+": %04d") % counts[0]



    
