import math


with open("A-large.in") as f:
    with open("output.txt", "w") as g:
        t = int(f.readline().strip())
        for i in range(1, t + 1):
            # print("i = {}".format(i))
            [n, k] = map(int, f.readline().split())
            rh = [None] * n
            for j in range(n):
                [ri, hi] = map(int, f.readline().split())
                rh[j] = (ri, hi, ri * hi)

            # base case: k = 1
            if k == 1:
                sur_area = 0
                for j in rh:
                    tmp = math.pi * j[0] * (j[0] + 2 * j[1])
                    if tmp > sur_area:
                        sur_area = tmp
            else:
                # only largest radius affects top down i.e. pi * r ^ 2
                # the rest just need to be best trade off for 2 * pi * r * h
                # so, r * h needs to be maximised for all BUT the bottom

                # pick the top ones first, add to surface area
                sur_area = 0
                # also keep track of biggest radius
                max_radius = 0
                for j in sorted(rh, key = lambda x: x[2], reverse = True)[:k-1]:
                    # might need to somehow prefer lower or higher radii...?
                    if j[0] > max_radius:
                        max_radius = j[0]
                    sur_area += 2 * math.pi * j[2]
                    rh.remove(j)
                    # print(rh)

                # need to pick last one

                best_choice = 0
                for j in rh:
                    # if radius is smaller than max_radius...
                    if j[0] <= max_radius:
                        tmp = math.pi * max_radius ** 2
                        tmp += 2 * math.pi * j[2]
                        if tmp > best_choice:
                            best_choice = tmp
                    else:
                        tmp = math.pi * j[0] ** 2
                        tmp += 2 * math.pi * j[2]
                        if tmp > best_choice:
                            best_choice = tmp

                sur_area += best_choice

            g.write("Case #{}: {}\n".format(i, sur_area))