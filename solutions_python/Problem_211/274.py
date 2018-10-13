#Problem C-small 1

def get_inputs():
    t = int(input())
    case_list = []

    for i1 in range(t):
        n, k = tuple([int(i2) for i2 in input().split()])
        u = float(input())
        p_list = [float(i3) for i3 in input().split()]

        case_list.append((n, k, u, p_list))

    return t, case_list

def case_prob(case_list, case_num):
    n, k, u, p_list = case_list[case_num]

    p_list.sort()
        
    while u > 0:
        lowest = p_list[0]
        low_count = 0
        next_highest = 1
        
        for p in range(n):
            if p_list[p] == lowest:
                low_count += 1
            else:
                next_highest = p_list[p]
                break
            
        if u/low_count + lowest == next_highest:
            p_list[0:low_count] = [next_highest]*low_count
            u = 0
        elif u > (next_highest - lowest) * low_count:
            p_list[0:low_count] = [next_highest]*low_count
            u -= (next_highest - lowest) * low_count
        else:
            p_list[0:low_count] = [u/low_count + lowest]*low_count
            u = 0
            
        p_list.sort()

    P = 1
    for p in p_list:
        P *= p

    print("Case #{0}: {1}".format(case_num + 1, P))
    

def main():
    t, case_list = get_inputs()

    for case_num in range(t):
        case_prob(case_list, case_num)

main()
