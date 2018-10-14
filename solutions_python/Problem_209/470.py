from math import pi
from operator import itemgetter

with open("A-large.in", "r") as inp:
    with open("A-large.out", "w") as outp:
        cases = int(inp.readline())
        for i in range(cases):
            total, stack = [int(k) for k in inp.readline().split()]
            top_s = {}
            lat_s = {}
            for j in range(total):
                rad, hei = [int(k) for k in inp.readline().split()]
                top_s[j] = pi * rad**2
                lat_s[j] = 2 * pi * rad * hei
            sorted_lat = sorted(lat_s.items(), key=itemgetter(1), reverse=True)
            my_pancakes_lat = sorted_lat[:stack]
            min_lat_s = min([x[1] for x in my_pancakes_lat])
            curr_lat = [x[1] for x in my_pancakes_lat]
            curr_lat_s = sum(curr_lat)

            my_ids = [x[0] for x in my_pancakes_lat]
            max_top_s = max([top_s[k] for k in my_ids])

            total_surface = curr_lat_s + max_top_s

            for x in sorted_lat[stack:]:
                key = x[0]
                this_top = top_s[key]
                this_lat = lat_s[key]
                diff = this_top + this_lat - max_top_s - min_lat_s
                if (diff > 0):
                    total_surface += diff
                    max_top_s = this_top
                    min_lat_s = this_lat
            outp.write("Case #" + str(i+1) + ": " + str(total_surface) + "\n")
