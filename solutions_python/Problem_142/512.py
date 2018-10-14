import sys

def extract_blocks(s):
    blocks = []
    prev_end = 0
    for i in xrange(1, len(s)):
        if s[i] != s[i-1]:
            blocks.append(s[prev_end:i])
            prev_end = i
    blocks.append(s[prev_end:])
    return blocks

T = int(sys.stdin.readline())
for case in xrange(1, T+1):
    #print "========================="
    #print "========================="
    #print "another case"
    N = int(sys.stdin.readline())
    strings = []
    for _ in xrange(N):
        strings.append(sys.stdin.readline().rstrip())
    
    #print "strings:", strings
    
    blocks = []
    for s in strings:
        blocks.append(extract_blocks(s))
    #print blocks
    
    ##print map(len, blocks)
    error = False
    if len(set(map(len, blocks))) != 1:
        error = True
        ##print "Case #"+str(case)+": Fegla Won"
        #continue
    if not error:
        steps = 0
        for i in xrange(len(blocks[0])):
            #print "------------------------------"
            #print "considering letter:", blocks[0][i]
            #print "first letter of this letter from all blocks:", map(lambda x: x[i][0], blocks)
            if len(set(map(lambda x: x[i][0], blocks))) != 1:
                error = True
            
            #to mozna zrobic szybciej; ale czy trzeba?
            max_len = max(map(lambda x: len(x[i]), blocks))
            sub_steps = max_len*(max_len+1)
            for ii in xrange(1, max_len+1):
                #print blocks, "map(lambda x: abs(i-len(x[i])), blocks)", map(lambda x: x[i], blocks)
                curr = sum(map(lambda x: abs(ii-len(x[i])), blocks))
                #print "for i=", ii, "the number of steps is:", curr
                sub_steps = min(curr, sub_steps)
            #print "the best value is:", sub_steps
            steps += sub_steps
    if error:
        print "Case #"+str(case)+": Fegla Won"
    else:
        print "Case #"+str(case)+": "+str(steps)
