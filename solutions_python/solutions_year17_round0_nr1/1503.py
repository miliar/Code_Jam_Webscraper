def flip(k, cakes, start):
    cakes[start:(start+k)] = map(lambda x: (x+1) % 2, cakes[start:(start+k)])        

def check(cakes):
    if sum(cakes) == len(cakes):
        return True
    return False


def solve(cakes, k):
    flips = 0
    for i in range(len(cakes)-k + 1):
        #print cakes
        if cakes[i] == 0:
            flip(k, cakes, i)
            flips += 1
    if check(cakes):
        return flips
    return "IMPOSSIBLE"

def translator(seq):
    res = []
    for i in seq:
        if i == "-":
            res.append(0)
        else:
            res.append(1)
    return res


def run_test(test_case):
    cakes = translator(test_case[0])
    return str(solve(cakes, int(test_case[1])))


def run_for_file(f_loc, o_loc):
    count = 1
    with open(f_loc, "r") as f:
        with open(o_loc, "w") as o:
            for line in f:
                split_up = line.split(" ") 
                if len(split_up) == 2:
                    o.write("Case #%d: " % count)
                    o.write(run_test(split_up))
                    o.write("\n")
                    count += 1
                    
run_for_file("in_dat_big", "big_real.txt")


