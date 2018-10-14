class State:
    def __init__(self, diners, time=0):
        self.diners = diners
        self.minutes = time

    def __repr__(self):
        return "State({}, {})".format(self.diners, self.minutes)

    def special_minute(self):
        pancakes = self.diners
        max_pan = pancakes[-1]
        new_states = []
        for p in xrange(2, max_pan/2+1):
            aux = pancakes[:-1] + [p, max_pan-p]
            aux.sort()
            new_states.append(State(aux, self.minutes + 1))
        return new_states

    def normal_minute(self):
        pancakes = self.diners
        new_pan = []
        for p in pancakes:
            if p > 1:
                new_pan.append(p-1)
        return [State(new_pan, self.minutes + 1)]

    def is_final_solution(self):
        return len(self.diners) == 0

    def get_minutes(self):
        return self.minutes


if __name__ == "__main__":
    test_cases = int(raw_input())
    for i in xrange(test_cases):
        diners = int(raw_input())
        pancakes = [int(n) for n in raw_input().split()]
        pancakes.sort()
        states = [State(pancakes)]
        best_solution = max(pancakes)
        while len(states) > 0:
            s = states.pop(0)
            if s.is_final_solution():
                if s.get_minutes() < best_solution:
                    best_solution = s.get_minutes()
            elif s.get_minutes() < best_solution:
                states += s.normal_minute()
                states += s.special_minute()
        print("Case #{}: {}".format(i+1, best_solution))
