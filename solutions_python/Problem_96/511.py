import sys

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for x in range(1, T+1):
        line = map(int, sys.stdin.readline().strip().split())
        N, S, p = line[:3]
        scores = line[3:] 

        non_special_limit = p + 2*max(p-1, 0)
        special_limit = p + 2*max(p-2, 0)
       
        result = 0        

        for score in scores:
            if non_special_limit <= score:
                result += 1
            elif S > 0 and special_limit <= score:
                result += 1
                S -= 1

        print("Case #%d: %d" % (x, result))
