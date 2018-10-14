import collections

Horse = collections.namedtuple('Horse', ['distance', 'speed', 'left_distance', 'left_time'])


def solution(distance, horses_raw):
    # print(distance, horses_raw)
    # horses = []
    left_time_max = 0
    for h_dist, h_speed in horses_raw:
        left_distance = distance - h_dist
        left_time = left_distance / h_speed
        left_time_max = max(left_time, left_time_max)
        # horses.append(Horse(h_dist, h_speed, left_distance, left_time))
    # print(left_time_max, horses)
    return "{0:.6f}".format(distance / left_time_max)


def process(filepath):
    with open(filepath.replace('.in', '.out'), 'w') as outp:
        with open(filepath) as filep:
            inputs = None
            lines_to_read = None
            case = 0
            current_kwargs = dict()

            for line in filep:
                line = line.strip()
                if inputs is None:
                    inputs = int(line)
                elif lines_to_read is None:
                    distance, num_horses = [int(item) for item in line.split(' ', 1)]
                    lines_to_read = num_horses
                    current_kwargs['distance'] = distance
                    current_kwargs['horses_raw'] = []
                else:
                    lines_to_read -= 1
                    current_kwargs['horses_raw'].append([int(item) for item in line.split(' ')])

                if lines_to_read == 0:
                    lines_to_read = None
                    case += 1
                    result = 'Case #{}: {}\n'.format(case, solution(**current_kwargs))
                    print(result, end='')
                    outp.write(result)


if __name__ == '__main__':
    # process('A-sample.in')
    process('A-large.in')