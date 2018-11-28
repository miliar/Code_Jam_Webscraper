import sys

def simulate(cakes, k):
    tot = 0
    for i in range(len(cakes)):
        if cakes[i] == 1:
            tot += 1
            for j in range(i, i + k):
                if j >= len(cakes):
                    return None
                cakes[j] = (cakes[j] + 1) % 2
    return tot

def num_flips(cakes, k):
    flips = [0] * len(cakes)
    k_tot = 0
    for i in range(len(cakes)):
        if i >= k:
            k_tot -= flips[i-k]        
        #print(flips)
        #print(k_tot)  
        flip = (cakes[i] + k_tot) % 2
        flips[i] = flip
        k_tot += flip
        if i + k > len(cakes) and flip == 1:
            return None
    return sum(flips)
    
def solve(in_file, out_file):
    neg = "IMPOSSIBLE"
    num_cases = int(in_file.readline().strip())
    for case in range(1, num_cases + 1):
        raw_cakes, raw_scoop = (val.strip() for val in in_file.readline().strip().split())

        #if case != 5:
        #    continue        
        scoop_size = int(raw_scoop)
        cakes = [0 if c == '+' else 1 for c in raw_cakes]
        #sol = simulate(cakes, scoop_size)
        sol = num_flips(cakes, scoop_size)
        if sol is None:
            sol = neg
        out_file.write("Case #{}: {}\n".format(case, sol))

if __name__ == '__main__':
    from_file = True
    
    if from_file:
        path='Data\\'
        #name='A-sample'
        #name='A-small-attempt1'
        name='A-large'
        file_input = open(path+name+'.in', 'r')
        #file_output = open(path+name + "naive" +'.out','w')
        file_output = open(path+name+'.out','w')
        solve(file_input, file_output)
        file_input.close()
        file_output.close()
    else:
        solve(sys.stdin, sys.stdout)
        
        
