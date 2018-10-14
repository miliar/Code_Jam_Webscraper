
def generate(total):
    solutions = []
    sols_closed = []
    ui = 10
    li = 0
    for i in range(ui, li-1, -1):

        if i+2 > 10:
            uj = 10
        else:
            uj = i+2

        if i-2 < 0:
            lj = 0
        else:
            lj = i-2

        for j in range(uj, lj-1, -1):
            k = total - (i+j)

            if k < 0 or k > 10 or abs(k-i) > 2 or abs(k-j) > 2:
                continue
            else:
                if (i,j,k) not in sols_closed:
                    solutions.append((i,j,k))
                    sols_closed.extend([(i,j,k), (i,k,j), (j,i,k), (j,k,i), (k,i,j), (k,j,i)])
    if len(solutions) == 0:
        solutions.append((0,0,0))
    return solutions

def surprise(a):
    (i,j,k) = a
    if abs(i-j) == 2 or abs(i-k) == 2 or abs(j-k) == 2:
        return True
    else:
        return False

def solve(totals, max_surp, best_p):
    solns = {}
    for i in range(len(totals)):
        solns[(totals[i], i)] = sorted(generate(totals[i]), key=lambda e: max(e))

    cur_surp = sum([1 if surprise(solns[k][-1]) else 0 for k in solns])

    if cur_surp > max_surp:
        # Remove surprises where it won't hurt the count
        while cur_surp > max_surp:
            chan = False
            for k in solns:
                if len(solns[k]) > 1 and max(solns[k][-1]) >= best_p and surprise(solns[k][-1]) and max(solns[k][-2]) >= best_p:
                    solns[k].pop()
                    chan = True
                    cur_surp = sum([1 if surprise(solns[k][-1]) else 0 for k in solns])
                if cur_surp == max_surp:
                    break
            if chan == False:
                break

        # Remove surprises that are below best_p
        while cur_surp > max_surp:
            chan = False
            for k in solns:
                if max(solns[k][-1]) < best_p and surprise(solns[k][-1]) and len(solns[k]) > 1:
                    solns[k].pop()
                    chan = True
                    cur_surp = sum([1 if surprise(solns[k][-1]) else 0 for k in solns])
                if cur_surp == max_surp:
                    break
            if chan == False:
                break

        # Remove surprises that are >= best_p if we still have more
        while cur_surp > max_surp:
            for k in solns:
                if surprise(solns[k][-1]) and len(solns[k]) > 1:
                    solns[k].pop()
                    cur_surp = sum([1 if surprise(solns[k][-1]) else 0 for k in solns])
                if cur_surp == max_surp:
                    break


    elif cur_surp < max_surp:
        # Add surprises that are below best_p
        while cur_surp < max_surp:
            chan = False
            for k in solns:
                if max(solns[k][-1]) < best_p and not surprise(solns[k][-1]) and len(solns[k]) > 1:
                    solns[k].pop()
                    chan = True
                    cur_surp = sum([1 if surprise(solns[k][-1]) else 0 for k in solns])
                if cur_surp == max_surp:
                    break
            if chan == False:
                break

        # Add surprise where it does not hurt
        while cur_surp < max_surp:
            chan = False
            for k in solns:
                if len(solns[k]) > 1 and max(solns[k][-1]) >= best_p and not surprise(solns[k][-1]) and max(solns[k][-2]) >= best_p:
                    solns[k].pop()
                    chan = True
                    cur_surp = sum([1 if surprise(solns[k][-1]) else 0 for k in solns])
                if cur_surp == max_surp:
                    break
            if chan == False:
                break

        # Add surprises that are >= best_p if we still have more
        while cur_surp < max_surp:
            for k in solns:
                if surprise(solns[k][-1]) and len(solns[k]) > 1:
                    solns[k].pop()
                    cur_surp = sum([1 if surprise(solns[k][-1]) else 0 for k in solns])
                if cur_surp == max_surp:
                    break
    return sum([1 if max(solns[k][-1]) >= best_p else 0 for k in solns])

if __name__ == "__main__":
    input()
    try:
        count = 1
        while True:
            inp = input().split()
            res = solve([int(i) for i in inp[3:]], int(inp[1]), int(inp[2]))
            print("Case #{0}: {1}".format(count, res))
            count += 1
    except:
        pass
