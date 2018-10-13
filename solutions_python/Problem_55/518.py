import sys

def solve(R, k, groups):
    total = 0
    for time in range(R):
        tmp_list = []
        tmp_total = 0
        while (len(groups)>0) and (tmp_total + groups[0] <= k):
            tmp_total += groups[0]
            tmp_list.append(groups.pop(0))
        groups.extend(tmp_list)
        total += tmp_total
    return total
            
def main():
    file = open(sys.argv[1])
    output = open('result.c', 'w')

    # number of maps
    cases = int(file.readline())

    for index in range(cases):
        R, k, N = [int(x) for x in file.readline().split()]
        groups = [int(x) for x in file.readline().split()[:N]]
        result = solve(R, k, groups)
        template = "Case #%d: %d\n"
        output.write(template%((index+1, result)))

    output.flush()
    output.close()
    file.close()
    
main()