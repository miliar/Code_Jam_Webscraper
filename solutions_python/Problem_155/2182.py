def solve():
    cases = int(input())
    for case in range(cases):
        max_shy, audience = input().strip().split()
        max_shy = int(max_shy)
        frnds = 0
        run_sum = 0
        run_sum += int(audience[0])
        for aud in range(1, max_shy+1):
            if run_sum < aud:
                frnds += 1
                run_sum += 1
            run_sum += int(audience[aud])
            #print(frnds, run_sum, audience[aud], aud)
        print("Case #{}: {}".format(case+1, frnds))

solve()
