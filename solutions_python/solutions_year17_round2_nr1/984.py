# D = kilometers to destination
# N = number of horses
# Ki = Initial position of horse i
# si = Speed of horse i (kph)

# For each horse find time of arrival
# Take slowest one's time
# Divide total distance by slowest time

# Input:
# T
# D N (T times)
# Ki Si (N times)


def solve(total_distance, num_horses, horses):
    """Returns the solution to case case."""
    arrival_times = []
    for h in horses:
        h_distance = total_distance - h[0]
        h_speed = h[1]
        arrival_times.append(h_distance / h_speed)
    arrival = max(arrival_times)  # All horses will slow down to match slowest
    speed = total_distance / arrival
    return speed


def main():
    solutions = []
    for __ in range(int(input())):
        d, n = [int(x) for x in input().split()]
        h = [tuple(int(x) for x in input().split()) for __ in range(n)]
        solutions.append(solve(d, n, h))
    for i, s in enumerate(solutions):
        print('Case #{i}: {s}'.format(i=i+1, s=s))


if __name__ == '__main__':
    main()
