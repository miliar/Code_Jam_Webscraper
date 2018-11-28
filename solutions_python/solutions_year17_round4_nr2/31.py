def rli():
    return list(map(int, input().split()))

def solve(N, C, D):
    by_pos = [[] for _ in range(N)]
    for P, B in D:
        if P > N:
            P = N
        by_pos[P].append(B)

    buyer_count = [0 for _ in range(C)]
    ride_count = 0
    free_seats = 0
    for pos, buyers in enumerate(by_pos):
        free_seats += ride_count
        for buyer in buyers:
            if free_seats == 0 or buyer_count[buyer] == ride_count:
                free_seats += pos + 1
                ride_count += 1
            free_seats -= 1
            buyer_count[buyer] += 1
    promotions = 0
    for buyers in by_pos:
        if len(buyers) > ride_count:
            promotions += len(buyers) - ride_count
    return ' '.join(map(str, [ride_count, promotions]))

def read_input():
    N, C, M = rli()
    D = [rli() for _ in range(M)] # P B
    D = [(x[0] - 1, x[1] - 1) for x in D]
    return (N, C, D)

no_inputs = int(input())
inputs = [read_input() for _ in range(no_inputs)]
solutions = [solve(*inp) for inp in inputs]

for i, s in enumerate(solutions):
    print("Case #{}: {}".format(i+1, s))
