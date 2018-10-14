import itertools    

f = open("ampleSyrupSmall.in", "r")
new_file = open("ampleSyrupSmallSolBrute", "w")
t = int(f.readline())

pi = 3.14159265359
def ample_syrup(n, k, rihis):
    memo = {}
    def dp_sol(k, rihis):
        if k == 0:
            return (0, 0)
        current_max = 0
        current_max_r = 0
        for i in range(len(rihis)):
            current_r, current_h = rihis[i]
            print current_r
            current_score = pi* current_r**2 + 2*pi*current_r*current_h
            if (k-1, i+1) in memo:
                next_score, r = memo[(k-1, i+1)]
            else:
                next_score, r = dp_sol(k-1, rihis[i+1:])
                memo[(k-1, i+1)] = (next_score, r)
            whole_score = current_score + next_score - pi*r**2
            if whole_score > current_max:
                current_max = whole_score
                current_max_r = current_r
        return (current_max, current_max_r)

    
    return dp_sol(k, rihis)[0]

def brute_force(k, rihis):
    all_combinations = itertools.combinations(rihis, k)
    max_value = 0
    for combination in all_combinations:
        current = evaluate_combination(combination)
        max_value = max(current, max_value)
    return max_value


def evaluate_combination(rihis):
    max_r = max(rihis, key=lambda tup: tup[0])[0]
    all_height_area = 0
    for i in rihis:
        all_height_area+= 2*pi*i[0]*i[1]
    print max_r
    return pi*max_r**2 + all_height_area

for i in range(1,t+1):
    n, k = [int(x) for x in f.readline().split(' ')]
    rihis = []
    for j in range(n):
        ri, hi = [int(x) for x in f.readline().split(' ')]
        rihis.append((ri,hi))
    # new_file.write("Case #"+str(i)+ ": "+str(ample_syrup(n,k,sorted(rihis, key= lambda tup: tup[0],reverse=True )))+"\n")
    new_file.write("Case #"+str(i)+ ": "+str(brute_force(k,sorted(rihis, key= lambda tup: tup[0],reverse=True )))+"\n")



