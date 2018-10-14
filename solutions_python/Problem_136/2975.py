def solve(C, F, X):
    STARTING_PACE = 2
    # Float parameters
    C, F, X = float(C), float(F), float(X)

    factories = 0
    current_pace = STARTING_PACE
    factories_building_time = 0

    old_cumulative_time = X / current_pace
    while True:
        factories += 1

        factories_building_time += C / current_pace
        # New cookies pace
        current_pace = STARTING_PACE + (F * factories)
        goal_cookies_time = X / current_pace

        # Building factories + generating cookies time
        cumulative_time = factories_building_time + goal_cookies_time

        if old_cumulative_time < cumulative_time:
            return old_cumulative_time
        else:
            old_cumulative_time = cumulative_time


def read_input():
    with open('B-large.in', 'r') as input_f:
        T = int(input_f.readline())
        for case in range(0, T):

            C, F, X = map(float, input_f.readline().split())

            solution = solve(C, F, X)

            print 'Case #%s: %.7f' % (case + 1, solution)

if __name__ == '__main__':
    read_input()
