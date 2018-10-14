INPUT_FILE = 'A-large.in'
OUTPUT_FILE = 'A-large.out'


def read_file():
    with open(INPUT_FILE) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        content = [x.split() for x in content]
        f.close()
    return content

def find_slowest_horse(list_horses, total_distance):
    time_horses = 0
    for i in list_horses:
        distance = total_distance - float(i[0])
        time = distance / float(i[1])
        if (time > time_horses):
            time_horses = time
    return time_horses

def main():
    with open(OUTPUT_FILE, 'w') as f:
        file_in = read_file()
        size_file = int(file_in[0][0])
        aux = 0;
        for i in range(1, size_file + 1):
            size_case = int(file_in[i + aux][1])
            total_distance = int(file_in[i + aux][0])
            list_horses = []
            for j in range(1, size_case + 1):
                list_horses.append(file_in[i + aux + j])
            time_slowest = find_slowest_horse(list_horses, total_distance)
            res = total_distance / time_slowest
            f.write('Case #{0}: {1:.06f} \n'.format(i, res))
            aux += size_case;


main()
