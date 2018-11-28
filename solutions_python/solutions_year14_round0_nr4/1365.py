'''
Created on Apr 13, 2014

@author: Adam Speakman
'''

in_file = open("D-large.in")
out_file = open("D-large.out", "w")
num_cases = int(in_file.readline())

N = 0

def get_war_score(N_blocks, K_blocks):
    N_score = 0
    K_score = 0
    for block in range(0, N):
        N_block = N_blocks[block]
        K_blocks_greater = [i for i,v in enumerate(K_blocks) if v > N_block]
        if len(K_blocks_greater) > 0:
            # Ken has a block that beats that! Discard lowest winning block.
            del K_blocks[K_blocks_greater[0]]
            K_score += 1
        else:
            # Ken has no block that beats that; discard lowest.
            del K_blocks[0]
            N_score += 1
    return N_score

def get_deceitful_score(N_blocks, K_blocks):
    N_score = 0
    K_score = 0
    while len(N_blocks) > 0:
        # Does N have a block that can never win? Use this to clear K's maximal block
        # by lying and saying it's just smaller than that.
        if N_blocks[0] < K_blocks[0]:
            del K_blocks[len(K_blocks) - 1]
            del N_blocks[0]
            K_score += 1
        # N uses her 'lowest winning block' to beat K. Has to be lowest, 
        # but she *lies* and says it's larger than K's largest. 
        # K always discards lowest losing block, so N's smallest will 
        # still win and he never knows she's lying.
        else:
            del K_blocks[0]
            del N_blocks[0]
            N_score += 1
    return N_score

for case in range(0, num_cases):
    N = int(in_file.readline())
    N_blocks = sorted(map(float, in_file.readline().split()))
    K_blocks = sorted(map(float, in_file.readline().split()))
#    print N_blocks
#    print K_blocks
    
    # Pass a copy so the other method can manipulate the lists without breaking things
    war_score = get_war_score(N_blocks[:], K_blocks[:])
    
    deceitful_score = get_deceitful_score(N_blocks[:], K_blocks[:])
    
    out_str = "Case #" + str((case + 1)) + ": "
    out_str += str(deceitful_score)
    out_str += " "
    out_str += str(war_score)
    out_str += "\n"
    out_file.write(out_str)

out_file.close()
in_file.close()
