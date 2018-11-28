def solve_case(D, N, K, S):
    latest_arrival = -1.0
    latest_horse = -1
    for i in range(N):
        horse_start = K[i]
        horse_speed = S[i]
        
        arrival = (D - horse_start) / horse_speed
        
        assert arrival >= 0
        
        if arrival > latest_arrival:
            latest_arrival = arrival
            latest_horse = i
            
    optimal_speed = D / latest_arrival
    return optimal_speed

num_cases = int(input())

for case in range(num_cases):
    case_string = input()
    D = int(case_string.split(' ')[0])
    N = int(case_string.split(' ')[1])

    K = []
    S = []
    for i in range(N):
        line = input().split(' ')
        Ki = float(line[0])
        Si = float(line[1])
        K.append(Ki)
        S.append(Si)
    
    result = float(solve_case(D, N, K, S))

    print("Case #" + str(case + 1) + (": %0.6f" % result))