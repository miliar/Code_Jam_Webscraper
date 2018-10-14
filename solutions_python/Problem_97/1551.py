import time
def calc(string):
    string = string.split('\n')
    num_cases = int(string[0])
    cases = string[1:]
    k = 0
    while k < num_cases:
        case = cases[k]
        split = case.split(' ')
        low = int(split[0])
        high = int(split[1])
        curr_list = list(range(low, high))
        perm_count = 0
        for i in curr_list:
            curr_perm = permute(i, low, high)
            for j in curr_perm:
                perm_count += 1
        print("Case #{0}: {1}".format(str(k+1), str(perm_count)))
        k+=1
        
def permute(i, low, high):
    i = str(i)
    orig = i
    j = len(i) - 1
    permutations = []
    seen_so_far = []
    while j > 0:
        i = i[-1] + i[:-1]
        if (int(i)>high or int(i)<low or int(i)<=int(orig) or int(i) in seen_so_far):
            j-=1
            continue
        permutations.append((orig, i))
        seen_so_far.append(int(i))
        j-=1
    return permutations
