import math

cache = {}

def find_stalls(dat):
    numstl = dat[0]
    numppl = dat[1]

    if numstl == numppl:
        return (0, 0)

    # Initialize stall states to [1, 0...0, 1]
    stall_states = [1] + [0]*numstl + [1]
    num_stalls = numstl + 2
    # For each person:
    x = 0
    filled = [0, num_stalls - 1]
    while x < numppl:
        # Step 2. find the resulting mid points
        mids = []
        last_f = 0

        for f in filled[1:]:
            p = math.floor((f - last_f)/2 + last_f)
            mids.append([p, p - last_f - 1, f - p - 1])
            last_f = f

        # Step 3. Get the optimal position
        best = [0, -2, -2]
        for m in mids:
            if m[1] > best[1] or (m[1] == best[1] and m[2] > best[2]):
                best = [ n for n in m ]
       
        filled.append(best[0])
        filled.sort()

        x += 1
    
    return (best[1], best[2]) if best[1] > best[2] else (best[2], best[1])

numinp = int(input())

for i in range(0, numinp):
    try:
        inp = list(map(int, input().split(' ')))
    except (ValueError, EOFError):
        break

    mx, mn = find_stalls(inp)
    print("Case #{}: {} {}".format(i+1, mx, mn))

