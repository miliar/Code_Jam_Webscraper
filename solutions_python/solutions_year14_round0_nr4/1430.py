#input read
input_file = open("input1.in", 'rt')
num_cases = int(input_file.readline())

#output write
output_file = open("output1.txt", 'w')

# do the job
def deceit_war(num_blocks, naomi_blocks, ken_blocks):
    score = 0
    for i in range(num_blocks):
        if naomi_blocks[-1] < ken_blocks[-1]:
            naomi_blocks.pop(-1)
            ken_blocks.pop(0)
        else:
            naomi_blocks.pop(-1)
            ken_blocks.pop(-1)
            score = score + 1
    return score

def war(num_blocks, naomi_blocks, ken_blocks):
    score = 0
    for i in range(num_blocks):
        if naomi_blocks[0] > ken_blocks[0]:
            naomi_blocks.pop(0)
            ken_blocks.pop(-1)
            score = score + 1
        else:
            ken_block = 0
            for j in range(len(ken_blocks)):
                if ken_blocks[j] > naomi_blocks[0]:
                    ken_block = j
                else:
                    break
            naomi_blocks.pop(0)      
            ken_blocks.pop(ken_block)              
    return score

for i in range(num_cases):
    print str(i+1) +  "/" + str(num_cases)
    num_blocks = int(input_file.readline())
    naomi_blocks = [float(x) for x in input_file.readline().split() ]
    ken_blocks = [float(x) for x in input_file.readline().split() ]
    naomi_blocks.sort()
    naomi_blocks.reverse()
    ken_blocks.sort()
    ken_blocks.reverse()
    deceit_score = deceit_war(num_blocks, list(naomi_blocks), list(ken_blocks))
    war_score = war(num_blocks, list(naomi_blocks), list(ken_blocks))
    output = "Case #%d: %d %d\n" %(i+1, deceit_score, war_score)
    output_file.write(output)
    
    
input_file.close()
output_file.close()