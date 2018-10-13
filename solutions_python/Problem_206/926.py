import sys

def solve(horses, dest_k):
    min_speed = None
    for start_k, speed_k in horses:
        needed_k = dest_k - start_k
        hours_left = needed_k / speed_k
        speed = dest_k / hours_left
        if speed < min_speed or min_speed is None:
            min_speed = speed
    return '%.6f' % min_speed

lines = [x for x in open(sys.argv[1], 'rt').readlines()]
count = int(lines.pop(0))
with open('out.txt', 'wt') as outfile:
    for i in xrange(count):
        dest_k, horse_count = lines.pop(0).strip().split(' ')
        horses = []
        dest_k = int(dest_k)
        horse_count = int(horse_count)
        for j in xrange(horse_count):
            start_k, speed_k = lines.pop(0).strip().split(' ')
            start_k = int(start_k)
            speed_k = float(speed_k)
            horses.append((start_k, speed_k))

    	max_res = solve(horses, dest_k)
    	print 'Case #%d: %s' % (i + 1, max_res)
    	outfile.write('Case #%d: %s\n' % (i + 1, max_res))
