DEBUG = False

def log(msg):
    if DEBUG:
        print msg

def build_cache(R, k, N, groups, tot_riders):
    cache = {}
    lg = len(groups)
    # each cache entry is key = starting group index, value = (number of riders that can ride starting from here, end group index)
    initial_ig = 0
    ig = initial_ig
    riders = 0
    while riders < tot_riders and riders + groups[ig] <= k:
        riders = riders + groups[ig]
        ig = ig + 1
        if ig >= lg:
            ig = 0
    final_ig = ig
    cache[initial_ig] = (riders, final_ig)

    for initial_ig in range(1, lg):
#        (riders, final_ig) = cache[initial_ig -1]
        # subtract the previous riders
        riders = riders - groups[initial_ig -1]
        while riders < tot_riders and riders + groups[ig] <= k:
            riders = riders + groups[ig]
            ig = ig + 1
            if ig >= lg:
                ig = 0
        final_ig = ig
        cache[initial_ig] = (riders, final_ig)

    return cache
        
def execute(R, k, N, groups):
    total = 0
    tot_riders = sum(groups)
    if tot_riders <= k:
        return tot_riders * R

    # initialize a cache for each starting group
    cache = build_cache(R, k, N, groups, tot_riders)
    lc = len(cache)
    check = [-1]*lc
    history = []
    repeat_flag = False
    ig = 0
    r = 0
    while r < R:
        initial_ig = ig
        (riders, ig) = cache[initial_ig]
        if not repeat_flag and check[initial_ig] > -1:
            # already repeated, stop here
            prev_start = initial_ig
            prev_r = check[prev_start]
            total_repeats = int((R-prev_r)/(r-prev_r))
            partial_total = 0
            if prev_r > 0:
                partial_total = history[prev_r-1]
            total = partial_total + ((total - partial_total) * total_repeats)
            r = prev_r + ((r-prev_r) * total_repeats)
            if r == R:
                return total
            check[initial_ig] = -99
            repeat_flag = True
        else:
            if not repeat_flag:
                check[initial_ig] = r
                if r == 0:
                    history.append(riders)
                else:
                    history.append(history[r-1] + riders)
        total += riders
#        print "%d, %d : %d" % (initial_ig, r, total)
        r = r + 1
        
    return total

def runall(filename):
    f = open(filename)
    lines = f.readlines()
    count = int(lines[0])

    #print "There are %s cases" % count

    idx = 1

    for i in range(0, count):
        line1 = lines[idx]
        idx = idx + 1
        line2 = lines[idx]
        idx = idx + 1  

        [R, k, N] = [int(a) for a in line1.rstrip().split(" ")]
        groups = [int(a) for a in line2.rstrip().split(" ")  ]

        total = execute(R, k, N, groups)
        print "Case #%d: %d" % (i+1, total)                
    
    
import random
def random_case():
    R = random.randint(0, pow(10, 8))
    k = random.randint(0, pow(10, 9))
    N = random.randint(0, 1000)
    test_list = []
    for i in range(0, N):
        test_list.append(str(random.randint(0, pow(10, 7))))
    print "%d %d %d" % (R, k, N)
    print "%s" % ' '.join(test_list)

#for i in range(0, 50):
#    random_case()

if DEBUG:
    filename = "/home/roy/in.txt"
else:
    filename = "/home/roy/Downloads/C-small-attempt0.in"

filename = "/home/roy/Downloads/C-large.in"

runall(filename)
    
