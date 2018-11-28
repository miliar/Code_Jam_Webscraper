def solve(N):
    N = list(map(int, list(N)))
    
    mid_start = 0
    
    for i in range(len(N)):
        if N[i] > N[mid_start]:
            mid_start = i

        if N[i] < N[mid_start]:
            if mid_start == 0:
                N[0] = N[0] - 1
                
                for j in range(1, len(N)):
                    N[j] = 9
            else:
                for j in range(mid_start, i):
                    N[j] = N[j] - 1
                for j in range(i, len(N)):
                    N[j] = 9
                    
            break

    N = ''.join(map(str, N))

    return N[N.rfind('0')+1:]
    
    
input = open('B-small-attempt0.in', 'r')
output = open('B-small-attempt0.out', 'w')

cases = int(input.readline())


for i in range(1, cases+1):
    N = input.readline().strip()
    #print('Case #{}: {}\n'.format(i, solve(N)))
    output.write('Case #{}: {}\n'.format(i, solve(N)))


input.close()
output.close()
