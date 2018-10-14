import sys
from collections import namedtuple
import GraphAlgo

Horse = namedtuple('Horse', 'dist speed')
Event = namedtuple('Event', 'city time horse_remain horse_speed')


class PonyGraph(GraphAlgo.GraphBase):
    def __init__(self):
        self.horse_of_city = {}
        self.neighbors_of_city = {}  # {city: [(index, dist), ...]}
        self.events_by_city_and_speed = {}

    def add_city(self, index, dist, speed):
        self.horse_of_city[index] = Horse(dist, float(speed))

    def add_road(self, src, dst, dist):
        self.neighbors_of_city.setdefault(src, []).append((dst, dist))

    def reset(self):
        self.events_by_city_and_speed = {}

    def set_start(self, city):
        horse = self.horse_of_city[city]
        event = Event(city, 0.0, horse.dist, horse.speed)
        self.events_by_city_and_speed[(city, horse.speed)] = [event]
        return event

    def getSuccessors(self, state):
        """Returns a list of (node, time)"""
        res = []
        if not isinstance(state, Event):
            return res
        city = state.city

        for (index, roadlen) in self.neighbors_of_city.get(city, []):
            remain = state.horse_remain - roadlen
            if remain >= 0:
                hspeed = state.horse_speed
                takes_time = roadlen / float(hspeed)
                res.append((Event(index, state.time + takes_time, remain, hspeed), takes_time))

        # Possibly replace horse
        new_horse = self.horse_of_city[city]
        res.append((Event(city, state.time, new_horse.dist, new_horse.speed), 0))

        ##@@
        #print "---- Successors of", state, ": "
        #import pprint; pprint.pprint(res)
        res = self._filter(res)
        res.append((city, 0))
        return res

    def _filter(self, succ):
        res = []
        for (state, weight) in succ:
            if self._is_good(state):
                res.append((state, weight))
        return res

    def _is_good(self, state):
        existing = self.events_by_city_and_speed.setdefault((state.city, state.horse_speed), [])
        indices_to_delete = []
        for i, known in enumerate(existing):
            if state.horse_remain == known.horse_remain and state.time == known.time:
                return True
            if state.horse_remain <= known.horse_remain and state.time >= known.time:
                return False
            if state.horse_remain >= known.horse_remain and state.time <= known.time:
                indices_to_delete.append(i)
        for i in reversed(indices_to_delete):
            del existing[i]
        existing.append(state)
        return True

if __name__ == "__main__":
    ncases = int(sys.stdin.readline().strip())
    for i in range(ncases):
        graph = PonyGraph()
        N, Q = [int(part) for part in sys.stdin.readline().split()]
        for index in xrange(1, N+1):
            dist, speed = [int(part) for part in sys.stdin.readline().split()]
            graph.add_city(index, dist, speed)
        for index in xrange(1, N+1):
            neigh = [int(part) for part in sys.stdin.readline().split()]
            for j, dist in enumerate(neigh):
                if dist > 0:
                    graph.add_road(index, j+1, dist)
        answers = []
        for _ in xrange(Q):
            src, dst = [int(part) for part in sys.stdin.readline().split()]
            graph.reset()
            root = graph.set_start(src)
            data = GraphAlgo.aStar(graph, root, dst)
            if dst not in data:
                answers.append(-1)
            else:
                answers.append(data[dst].distFromRoot)
        answer_str = ' '.join(str(a) for a in answers)
        print "Case #%d: %s" % (i+1, answer_str)
