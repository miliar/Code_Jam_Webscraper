
def solve(N, R, O, Y, G, B, V):
    assert O == 0 and G == 0 and V == 0
    from collections import OrderedDict
    d=[(R,'R'), (Y, 'Y'), (B, 'B')]
    d = sorted(d, key=lambda x: x[0])
    if d[2][0] > d[0][0] + d[1][0]:
        res = "IMPOSSIBLE"
        return res
    max_k = d[2][1]
    max_v = d[2][0]
    
    other_vs =  d[1][0] + d[0][0]
    num_pairs = (d[1][0] + d[0][0]) - max_v
    second_count = d[1][0]
    tail_char =  d[1][1]
    res = ""
    while (N > 0):
        res += max_k
        N -= 1
        if num_pairs > 0:
            num_pairs -= 1
            res += d[1][1] 
            res += d[0][1]
            second_count -= 1
            N -= 2
        else:
            if second_count > 0:
               second_count -= 1
               res += d[1][1]
            else:
               res += d[0][1]
            N -= 1
    return res

def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        N, R, O, Y, G, B,  V = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
        print "Case #{}: {}".format(i, solve(N, R, O, Y, G, B, V))

if __name__ == "__main__":
    main()
