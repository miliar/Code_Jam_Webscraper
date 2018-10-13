import sys

filename = 'CSmall'
output = open(filename + '_output.txt', 'w')

stalls = 0
n = 0

def main(argv=None):
    if argv is None:
        argv = sys.argv

    with open(filename + '.txt') as file:
        t = file.readline()
        input = file.readlines()
        case = 1
        for line in input:
            n, k = [int(x) for x in line.split()]

            # List with all of the stalls, including the ones for the guards
            stalls = ['.' for _ in range(n + 2)]
            stalls[0] = 'G'
            stalls[-1] = 'G'

            for person in range(k ):
                # List with tuples (Ls, Lr) for each stall
                values = []

                for stall in range(1, n + 1):
                    # If its occupied
                    if stalls[stall] != '.':
                        values.append((-1, -1))
                        continue

                    Ls = 0
                    Rs = 0

                    # Count the ones to the left
                    for left in range(stall, 1, -1):
                        if stalls[left - 1] == '.':
                            Ls += 1
                        else:
                            break

                    # Count the ones to the right
                    for right in range(stall + 1, n + 1):
                        if stalls[right] == '.':
                            Rs += 1
                        else:
                            break
                    values.append((Ls, Rs))

                # min(Ls, Rs) for each stall
                mins = [min(tup) for tup in values]

                # List with the indexes of those mins that are maximal
                mins_indexes = indexes(mins)
                if len(mins_indexes) == 1:
                    selected_stall = mins_indexes[0] + 1
                    stalls[selected_stall] = '0'
                else:
                    # max(Ls, Rs)
                    maxes = [-1 for _ in values]
                    for z in mins_indexes:
                        maxes[z] = (max(values[z]))
                    # List with those maxes that are maximal
                    maxes_indexes = indexes(maxes)
                    selected_stall = maxes_indexes[0] + 1
                    stalls[selected_stall] = '0'
            aux = values[selected_stall - 1]
            output.write('Case #{}: {} {}\n'.format(case, max(aux), min(aux)))
            case += 1
    output.close()


def indexes(l):
    res = []
    max_val = max(l)
    for i in range(len(l)):
        if l[i] == max_val:
            res.append(i)
    return (res)


if __name__ == "__main__":
    sys.exit(main())
