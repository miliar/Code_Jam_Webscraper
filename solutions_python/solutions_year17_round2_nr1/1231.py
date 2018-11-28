from math import pow, floor, log, ceil

with open(r'D:\PycharmProjects\GCJ_2017\A-large.in', 'r') as inp:
    lines = inp.readlines()

    with open(r'D:\PycharmProjects\GCJ_2017\A-large.out', 'w') as outp:
        idx = 0
        nr_tc = 0
        line_idx = 0
        while line_idx < len(lines):
            line = lines[line_idx]
            if line_idx  == 0:
                nr_tc = int(line.strip())
                line_idx +=1
            else:
                l = line.strip().split()
                destination, horses = long(l[0]), long(l[1])

                positions = []
                speeds = []
                time_to_destination = 0.0
                times_to_destination = []
                horse_idx = 0
                line_idx += 1

                while horse_idx < horses:
                    l = lines[line_idx].strip().split()
                    position, speed = float(l[0]), float(l[1])
                    positions.append(position)
                    speeds.append(speed)
                    time_to_destination = (destination - position)/speed
                    times_to_destination.append(time_to_destination)

                    horse_idx += 1
                    line_idx += 1

                #print 'Case #%s: %s\n' % (idx, destination/max(times_to_destination))
                outp.write('Case #%s: %s\n' % (idx, destination/max(times_to_destination)))
            idx += 1