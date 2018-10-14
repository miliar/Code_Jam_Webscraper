import sys


def compute_velocity(destination, horses, case):
    horses.sort(reverse=True)
    worst_time = (destination - horses[0][0]) / horses[0][1] # time = space / velocity
    for horse in horses:
        todo = destination - horse[0]
        time = todo / horse[1]
        if time > worst_time:
            worst_time = time

    curise_velocity = destination / worst_time

    return "Case #" + str(case) + ": " + str(curise_velocity) + "\n"


def solve(input, output):
    # Read input
    with open(output, "w") as o:
        with open(input, "r") as f:
            f.readline() # Read number of examples
            # Process examples
            case = 1
            while True:
                line = f.readline()
                if not line:
                    break

                destination, num_horses = line.split(" ")
                horses = []
                for i in range(int(num_horses)):
                    row = f.readline()
                    pos, velocity = row.split(" ")
                    horses.append([int(pos), int(velocity)])

                o.write(compute_velocity(int(destination), horses, case))
                case += 1


if __name__ == '__main__':
    solve(sys.argv[1], sys.argv[2])
