T = int(raw_input())

def reverse_cake(cakes):
    new_cakes = ""
    for cake in cakes:
        if cake == "+":
            new_cakes += "-"
        else:
            new_cakes += "+"
    return new_cakes

for case in range(1, T+1):
    cakes, K = raw_input().strip().split()
    K = int(K)
    cakes_no = len(cakes)
    switches = 0
    is_impossible = False
    for cake_index in range(cakes_no)[::-1]:
        if cake_index+1 >= K and cakes[cake_index] == "-":
            cakes = cakes[:cake_index-K+1] + reverse_cake(cakes[cake_index-K+1:cake_index+1]) + cakes[cake_index+1:]
            switches += 1
        elif cake_index < K and cakes[cake_index] == "-":
            is_impossible = True
            break
        else:
            continue

    if is_impossible:
        print "Case #{}: {}".format(case, "IMPOSSIBLE")
    else:
        print "Case #{}: {}".format(case, switches)


