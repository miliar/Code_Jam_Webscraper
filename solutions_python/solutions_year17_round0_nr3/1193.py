import sys
import math

def find_prev_power_of_2(n):
    log=math.log(n,2)
    # if log%1==0:
    #     prev_power=2**log-1
    # else:
    prev_power=2**math.floor(log)
    return prev_power

def find_stalls(stalls,men):
    prev_power=find_prev_power_of_2(men)
    stalls_to_split=stalls-prev_power+1
    splitted=float(stalls_to_split)/prev_power
    split_ratio=splitted%1
    index= (float(men) / prev_power)%1
    if index<split_ratio:
        last_split=math.ceil(splitted)
    else:
        last_split=math.floor(splitted)
    return str(int(math.ceil(float(last_split-1)/2)))+' '+str(int(math.floor(float(last_split-1)/2)))

output = []

with open(sys.argv[1], 'rb') as input_file:
    inp = input_file.readlines()
for line_num in range(1, int(inp[0])+1):
    stalls,men= inp[line_num].split()
    output.append('Case #'+str(line_num)+': '+find_stalls(int(stalls),int(men)))
    output.append("\r\n")
output.pop()
with open(sys.argv[2], 'wb') as out:
    out.writelines(output)
