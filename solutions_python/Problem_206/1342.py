T = int(raw_input())

class Horse(object):
    def __init__(self, distance, speed):
        self.distance = distance
        self.speed = speed

    def calculate_arrival_time(self, D):
        return (D  - self.distance) / float(self.speed)

def solve(D, horses):
    arrival_of_last_horse = horses[len(horses) - 1].calculate_arrival_time(D)

    for horse in reversed(horses):
        arrival_of_last_horse = max(arrival_of_last_horse, horse.calculate_arrival_time(D))

    return D / arrival_of_last_horse

for t in xrange(1, T + 1):
    D, N = map(int, raw_input().split())
    horses = sorted([Horse(*map(int, raw_input().split())) for i in xrange(N)], key=lambda x: x.distance)
    print 'Case #{}: {}'.format(t, solve(D, horses))
