import bisect

input_fname = "input.txt"
output_fname = "output.txt"
lines = [line.strip() for line in open(input_fname)]

lines_per_test = 3

def solve(inputs):
    n_blocks = inputs[0]
    naomi_blocks = [float(wt) for wt in inputs[1].split(' ')]
    ken_blocks = [float(wt) for wt in inputs[2].split(' ')]
    naomi_blocks.sort()
    ken_blocks.sort()
    dwar_wins = dwar(naomi_blocks, list(ken_blocks))
    war_wins = war(naomi_blocks, list(ken_blocks))
    
    
    return str(dwar_wins) + ' ' + str(war_wins)

def war(n_wts, k_wts):
    res = 0
    for wt in n_wts:
        index = bisect.bisect(k_wts, wt)
        if index == len(k_wts):
            k_wts.pop(0)
            res += 1
        else:
            k_wts.pop(index)
    return res

def dwar(n_wts, k_wts):
    res = 0
    for wt in n_wts:
        if wt < k_wts[0]:
            k_wts.pop()
        else:
            res += 1
            k_wts.pop(0)
    return res
    

def format_output(test_num, result):
    return "Case #" + str(test_num) + ": " + result + "\n"

fout = open(output_fname, "w")
for i in range(0,int(lines[0])):
    ans = solve(lines[i*lines_per_test+1:(i+1)*lines_per_test+1])
    fout.write(format_output(i+1,ans))
fout.close()
    
