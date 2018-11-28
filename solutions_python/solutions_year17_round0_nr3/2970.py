def get_distance_from_left(stalls, stall):
    for i in range(stall, -1, -1):
        if stalls[i]:
            return abs(stall - i - 1)


def get_distance_from_right(stalls, stall):
    for i in range(stall, len(stalls)):
        if stalls[i]:
            return abs(i - stall - 1)


def calculate_distances(stalls):
    distances = []
    for stall in range(1, len(stalls) - 1):
        if not stalls[stall]:
            distances.append((get_distance_from_left(stalls, stall), get_distance_from_right(stalls, stall)))
        else:
            distances.append((0, 0))
    return distances


def get_max_min_distances(distances):
    min_distances = []
    max_min_distance = 0
    for left_dist, right_dist in distances:
        min_distance = min(left_dist, right_dist)
        min_distances.append(min_distance)

        if min_distance > max_min_distance:
            max_min_distance = min_distance

    max_min_distance_stalls = []
    for i in range(len(min_distances)):
        if min_distances[i] == max_min_distance:
            max_min_distance_stalls.append(i)

    return max_min_distance_stalls


def get_max_stall_distance_stall(distances, stall_numbers):
    max_distance = 0
    max_distance_stall = 0
    for stall_number in stall_numbers:
        local_max = max(distances[stall_number][0], distances[stall_number][1])
        if local_max > max_distance:
            max_distance = local_max
            max_distance_stall = stall_number

    return max_distance_stall


def calculate(num_stalls, num_of_people):
    stalls = [True] + [False] * num_stalls + [True]
    result = 0
    for _ in range(num_of_people):
        distances = calculate_distances(stalls)
        max_min_distances = get_max_min_distances(distances)

        if len(max_min_distances) > 1:
            result = get_max_stall_distance_stall(distances, max_min_distances)
        else:
            result = max_min_distances[0]

        stalls[result + 1] = True

    max_dist_for_chosen = max(distances[result][0], distances[result][1])
    min_dist_for_chosen = min(distances[result][0], distances[result][1])
    return max_dist_for_chosen, min_dist_for_chosen


if __name__ == "__main__":
    print("Test Starting")
    input_file = open("C:\\Users\\Yash\\Downloads\\input.txt")
    output_file = open("C:\\Users\\Yash\\Downloads\\output.txt", 'w')
    input_number = int(input_file.readline())
    for i in range(input_number):
        line = input_file.readline()
        args = line.split()
        max_dist, min_dist = calculate(int(args[0]), int(args[1]))
        output_file.write("case #" + str(i + 1) + ": " + str(max_dist) + " " + str(min_dist) + "\n")

    input_file.close()
    output_file.close()
    print("FIN")
