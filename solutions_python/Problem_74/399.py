def other_robot(r):
    return {'O': 'B', 'B': 'O'}[r]

def solve_robots(positions):
    now = {'O': 1, 'B': 1}
    bonus = {'O': 0, 'B': 0}

    total_time = 0
    for position in positions:
        current, button = position
        other = other_robot(current)

        original_distance = abs(now[current] - button)
        distance = original_distance - bonus[current]

        round_time = (distance + 1) if distance > 0 else 1

        bonus[current] = 0
        bonus[other] += round_time
        now[current] = button

        total_time += round_time

    return total_time

if __name__ == '__main__':
    number_of_tests = int(raw_input())
    for t in range(1, number_of_tests+1):
        test = raw_input().split(' ')
        n = int(test[0])
        positions = [(test[i], int(test[i+1]))
                     for i in range(1, 2*n, 2)]
        answer = solve_robots(positions)
        print 'Case #%d: %d' % (t, answer)
