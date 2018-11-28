import math
from collections import defaultdict

class TestCase(object):
    def __init__(self, data):
        self.data = data
        
    @classmethod
    def from_input(cls, input):
        l = map(int, input.split())
        num_boosters, booster_time, num_stars, num_distances = l[:4]
        star_distances = []
        for i in xrange(num_stars):
            star_distances.append(l[i%num_distances+4])
        return cls([num_boosters, booster_time, star_distances])
    
    def solve(self):
        num_boosters, booster_time, star_distances = self.data
        distance_before = []
        for i, d in enumerate(star_distances):
            if i > 0:
                distance_before.append(distance_before[-1]+star_distances[i-1])
            else:
                distance_before.append(0)
        
        check_earlier = []
        booster_savings = []
        booster_savings_map = {}
        for i, d in enumerate(distance_before):
            dist = star_distances[i]
            time_begin = d*2
            booster_completion = max(booster_time-time_begin,0)
            booster_completion_boosted = max(booster_time-d,0)
            if booster_completion_boosted != booster_completion and booster_completion_boosted < dist*2:
                check_earlier.append(True)
            else:
                check_earlier.append(False)
            saving = max(dist*2-booster_completion, 0)//2
            booster_savings.append((saving, i))
            booster_savings_map[i] = saving
        booster_savings.sort(reverse=True)

        prel_booster_stars = [s[1] for s in booster_savings[:num_boosters]]
        
        time = (distance_before[-1]+star_distances[-1])*2
        for i, star in enumerate(prel_booster_stars):
            time -= booster_savings_map[star]
        return time
    
    
f = open("inputs/space-large.in", "r")
test_cases = int(f.readline())
s = []
for i in range(test_cases):
    test_case = TestCase.from_input(f.readline().strip())
    s.append("Case #%d: %s" % (i+1, test_case.solve()))
    print s[-1]
f = open("outputs/space-large.out", "w")
f.write("\n".join(s))
    
