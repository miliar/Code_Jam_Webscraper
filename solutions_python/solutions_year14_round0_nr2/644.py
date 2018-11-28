import fileinput

try:
    import psyco
    psyco.full()
except:
    pass

class cookie_game(object):
    BASE_COOKIE_RATE = 2
    def __init__(self, C, F, X):
        self.C = C
        self.F = F
        self.X = X

    def cookie_generation_rate(self, num_factories):
        return self.BASE_COOKIE_RATE+(num_factories * self.F)

    def time_to_next_factory(self, num_factories):
        return self.C / self.cookie_generation_rate(num_factories)

    def time_to_goal(self, num_factories):
        return self.X / self.cookie_generation_rate(num_factories)

    def recurse(self, num_factories):
        time_to_next = self.time_to_next_factory(num_factories)
        time_to_goal = self.time_to_goal(num_factories)
        if time_to_goal <= (time_to_next + self.time_to_goal(num_factories+1)):
            return time_to_goal
        return min(time_to_next+self.recurse(num_factories+1), time_to_goal)

    def linear_search(self):
        factories_time = 0
        num_factories = 0
        time_to_goal = self.time_to_goal(num_factories)
        while True:
            time_to_next = self.time_to_next_factory(num_factories) 
            time_to_goal_with_next =  factories_time + time_to_next + self.time_to_goal(num_factories+1)
            if time_to_goal_with_next > time_to_goal:
                return time_to_goal
            time_to_goal = time_to_goal_with_next
            factories_time = factories_time + time_to_next
            num_factories += 1


def solve_case(case):
    game = cookie_game(*case)
    return game.linear_search()


def main():
    it = fileinput.input()
    num_cases = int(it.next())
    for i,l in enumerate(it):
        print "Case #%d: %0.8f" % (i+1,solve_case([float(x) for x in l.split()]))

if __name__ == "__main__":
    main()
