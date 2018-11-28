# ROYGBV
N = False
K = True
adjacency = [[N,N,K,K,K,N],
             [N,N,N,K,K,K],
             [K,N,N,N,K,K],
             [K,K,N,N,N,K],
             [K,K,K,N,N,N],
             [N,K,K,K,N,N]]

def solve_case(N, R, O, Y, G, B, V):
    assert N == R + O + Y + G + B + V
    
    # For small, we have only R, Y, and B unicorns
    assert O == 0
    assert G == 0
    assert V == 0
    
    # If we have approx more than half N of a single color,
    # then two would have to be adjacent, so it is impossible
    max_same_color = N // 2
    if R > max_same_color or Y > max_same_color or B > max_same_color:
        return 'IMPOSSIBLE'
    
    colors = []
    unicorns = []
    
    # sort em
    if R >= Y and R >= B:
        if Y > B:
            colors = ['R', 'Y', 'B']
            unicorns = [R, Y, B]
        else:
            colors = ['R', 'B', 'Y']
            unicorns = [R, B, Y]
    elif Y >= R and Y >= B:
        if R > B:
            colors = ['Y', 'R', 'B']
            unicorns = [Y, R, B]
        else:
            colors = ['Y', 'B', 'R']
            unicorns = [Y, B, R]
    else:
        if R > Y:
            colors = ['B', 'R', 'Y']
            unicorns = [B, R, Y]
        else:
            colors = ['B', 'Y', 'R']
            unicorns = [B, Y, R]
    
    result = []
    
    num_placed = 0
    
    while num_placed < N:
        first = unicorns[0]
        second = unicorns[1]
        third = unicorns[2]
        
        # All three equal:
        if first == second and second == third:
            result.append(colors[0])
            result.append(colors[1])
            result.append(colors[2])
            unicorns[0] -= 1
            unicorns[1] -= 1
            unicorns[2] -= 1
            num_placed += 3
        
        # First two equal:
        elif first == second:
            result.append(colors[0])
            result.append(colors[1])
            unicorns[0] -= 1
            unicorns[1] -= 1
            num_placed += 2
            
        
        # All different:
        # Can't just place one
        else:
            result.append(colors[0])
            result.append(colors[1])
            unicorns[0] -= 1
            unicorns[1] -= 1
            num_placed += 2
            
            # re-sort if necessary
            if unicorns[1] < unicorns[2]:
                temp = unicorns[2]
                unicorns[2] = unicorns[1]
                unicorns[1] = temp
                
                temp = colors[2]
                colors[2] = colors[1]
                colors[1] = temp
    
    return ''.join(result)
    
num_cases = int(input())

for case in range(num_cases):
    values = input().split(' ')
    
    N = int(values[0])
    R = int(values[1])
    O = int(values[2])
    Y = int(values[3])
    G = int(values[4])
    B = int(values[5])
    V = int(values[6])

    result = solve_case(N, R, O, Y, G, B, V)

    print("Case #" + str(case + 1) + ": " + str(result))