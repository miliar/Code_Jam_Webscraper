import heapq
import sys

def find_period(barbers):
    queue = [(minutes, n + 1) for n, minutes in enumerate(barbers)]
    heapq.heapify(queue)

    next_barber = None
    period = None
    i = 0

    while True:
        next_barber = heapq.heappop(queue)
        if next_barber[0] == 0:
            heapq.heappush(queue, (barbers[next_barber[1] - 1], next_barber[1]))
            i = i + 1
            continue

        queue = map(lambda x: (x[0] - next_barber[0], x[1]), queue)

        if sum(map(lambda x: x[0], queue)) == 0:
            period = i + len(barbers)
            break

        heapq.heappush(queue, (barbers[next_barber[1] - 1], next_barber[1]))
        i = i + 1

    return period


def solve_problem(position, barbers):
    period = find_period(barbers)

    if position % period != 0:
        position = position % period
    else:
        position = position - period * (position / period - 1)

    next_barber = None
    queue = [(0, n + 1) for n, minutes in enumerate(barbers)]
    heapq.heapify(queue)

    #print period, position, len(barbers)

    for i in xrange(position):
        next_barber = heapq.heappop(queue)
        if next_barber[0] == 0:
            heapq.heappush(queue, (barbers[next_barber[1] - 1], next_barber[1]))
            continue

        queue = map(lambda x: (x[0] - next_barber[0], x[1]), queue)
        heapq.heappush(queue, (barbers[next_barber[1] - 1], next_barber[1]))

    return next_barber[1]



if __name__ == "__main__":
    num_of_cases = int(sys.stdin.readline().strip())

    for i in xrange(1, num_of_cases + 1):
        _, position = map(int, sys.stdin.readline().split())
        barbers = map(int, sys.stdin.readline().split())
        print "Case #{0}: {1}".format(i, solve_problem(position, barbers))

