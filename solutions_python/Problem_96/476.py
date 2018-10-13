
def solve(case):
    N, S, p, rest = case.split(" ", 3)
    N = int(N)
    S = int(S)
    p = int(p)
    t = [int(x) for x in rest.split(" ")]
    #print N, S, p, t
    possible_surprising = S
    result = 0
    
    for total in t:
        if total <= 1:
            # surprising not possible
            max_score = total
            if max_score >= p:
                result += 1
        elif total >= 29:
            # surprising not possible
            max_score = 10
            if max_score >= p:
                result += 1
        elif total % 3 == 1:
            # surprising max == !surprising max
            max_score = (total / 3) + 1
            if max_score >= p:
                result += 1
        else:
            # surprising possible!
            
            max_score = ((total + 1) / 3)
            # not surprising case
            if max_score >= p:
                result += 1
            # surprising case
            elif possible_surprising and max_score + 1 >= p:
                result += 1
                possible_surprising -= 1
        
    return result


def main():
    input = open('B-large.in')
    output = open('output.txt', 'w')
    total_case_num = int(input.readline().strip())
    
    for case_num in range(1, total_case_num + 1):
        case = input.readline().strip()
        result = solve(case)
        output.write("Case #%s: %s\n" % (case_num, result))

if __name__ == '__main__':
    #solve("2 1 1 8 0")
    main()