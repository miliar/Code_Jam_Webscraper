#! /usr/bin/python3
name = 'horses'

in_file = open('/home/blaidd-drwg/jam/' + name + '.in', 'r')
out_file = open('/home/blaidd-drwg/jam/' + name + '.out', 'w')

in_data = in_file.readlines()
cases = int(in_data[0])
pointer = 1

for case in range(1, cases + 1):
    case_data = in_data[pointer].split()
    d = int(case_data[0])
    horses = int(case_data[1])
    pointer += 1

    horse_data = []
    for i in range(horses):
        horse_data.append(in_data[pointer].split())
        pointer += 1

    t = [(d - int(distance)) / int(speed) for distance, speed in horse_data]
    max_t = max(t)

    v = d / max_t

    out_file.write('Case #%d: %f' % (case, v))
    out_file.write('\n')

in_file.close()
out_file.close()

