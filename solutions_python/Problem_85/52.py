from __future__ import division
from bisect import bisect_left, bisect_right
import heapq
def rins():
    return raw_input().strip()


# This function copied from bisect docs: http://docs.python.org/library/bisect.html
def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def solve_next():
    input_values = [int(x) for x in rins().split()]
    l,t,n,c = input_values[:4]
    distances = input_values[4:]
    cumulative_distances = []
    dd=0
    for d in distances:
        dd+=d
        cumulative_distances.append(dd)
    distance_sum = sum(distances)
    zero_p_cum = [0] + cumulative_distances
    assert distance_sum == dd
    def distance_before_planet(i):
        return distances[(i+1)%c]
    def distance_after_planet(i):
        return distances[i%c]
    def total_distance_to_planet(i):
        cycles = (i) // c
        return distance_sum * cycles + zero_p_cum[(i) % c]
    def last_planet_passed_at_distance(d):
        cycles = int(d // distance_sum)
        offset_distance = d % distance_sum
        #print distance_sum
        #print "offset_distance:", offset_distance
        index = bisect_right(cumulative_distances, offset_distance)
        assert index<c+1
        return cycles * c + index

    slow_travel_distance = t//2
    if slow_travel_distance==0:
        slow_travel_cycles = 0
        slow_travel_offset = 0
        last_planet_passed_slow = 0
    else:
        assert 2*slow_travel_distance == t
        slow_travel_cycles = distance_sum // slow_travel_distance
        slow_travel_offset = distance_sum % slow_travel_distance
        last_planet_passed_slow = last_planet_passed_at_distance(slow_travel_distance)
    #print "last_p", last_planet_passed_slow
    distance_to_last_planet = total_distance_to_planet(last_planet_passed_slow)
    #print "std", slow_travel_distance
    #print "d1", distance_to_last_planet
    overshoot = slow_travel_distance - distance_to_last_planet
    #print "overshoot", overshoot
    distance_remaining_to_next_planet = distance_after_planet(last_planet_passed_slow) - overshoot
    #print "remaining =", distance_remaining_to_next_planet
    assert distance_remaining_to_next_planet >= 0 # >0?
    booster_heap = []
    booster_total_value = [0]
    def add_booster(planet, value):
        heapq.heappush(booster_heap, (value, planet))
        booster_total_value[0] += value
    def pop_booster():
        value, planet = heapq.heappop(booster_heap)
        booster_total_value[0] -= value
        return planet, value
    def add_booster_if_better(planet, value):
        if l==0:
            return
        if len(booster_heap) < l:
            add_booster(planet, value)
        else:
            other_planet, other_value = pop_booster()
            if other_value >= value:
                add_booster(other_planet, other_value)
            else:
                add_booster(planet, value)
    if l>0:
        add_booster(last_planet_passed_slow, distance_remaining_to_next_planet)
    planet = last_planet_passed_slow + 1
    travelled = total_distance_to_planet(planet)
    while planet < n:
        add_booster_if_better(planet, distance_after_planet(planet))
        planet += 1
    #print "I will use this set of boosters:"
    #for value, planet in booster_heap:
    #    print "#{0} (providing a boost of {1})".format(planet, value)
    #print total_distance_to_planet(n)
    #print booster_total_value[0]
    return total_distance_to_planet(n) * 2 - booster_total_value[0]
        

    

    #slow_time = 2*sum(distances)
    


def run():
    t = int(rins())
    for i in xrange(t):
        print "Case #{0}: {1}".format(i+1, solve_next())

run()
