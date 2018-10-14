import math

in_file = open('bathroom_stalls.in')
cases = int(in_file.readline().strip())
results = []

for case in range(cases):
    n,k = map(int,in_file.readline().strip().split())
    biggest_block = 1
    tier = math.floor(math.log(k,2))
    
    step = 2**tier
    
    low_num = (n-(step-1))//step
    
    num_of_big_nums = n-((step-1)+low_num*step)
    
    k_pos_on_tier = k-step
    
    if k_pos_on_tier < num_of_big_nums:
        biggest_block = low_num+1
    else:
        biggest_block = low_num
    
    #print(n,k,tier)
    results.append("Case #{}: {} {}".format(case+1,biggest_block//2,(biggest_block-1)//2))
in_file.close    

out_file = open('bathroom_stalls.out','w')
    
for result in results:
    print(result)
    out_file.write(result+'\n')

out_file.close