import sys

def do_case(seats=0, runs=0, groups=[]):
    euros = 0
    while runs > 0:
        seated = 0
        g_count = 0
        while seated < seats:
            next_group = groups.pop(0)
            if next_group <= seats - seated:
                seated += next_group
                groups.append(next_group)
                g_count += 1
                if g_count == len(groups):
                    break
            else:
                groups.insert(0, next_group)
                break
        euros += seated
        runs -= 1
    return euros

try:
    filename = sys.argv[1]
except IndexError:
    print("Enter a valid input file.")
    exit()
cases = []
f_in = open(filename)
fname_parts = filename.split('.')
fname_parts[1] = 'out'
fname_out = '.'.join(fname_parts)
f_out = open(fname_out, 'w')
f_in.readline() # skip
line = f_in.readline()
count = 1
while line:
    parts = line.split()
    tc_runs = int(parts[0])
    tc_seats = int(parts[1])
    line = f_in.readline()
    parts = line.split()
    tc_groups = [int(part) for part in parts]
    f_out.write(
        "Case #%s: %s\n" % (
            count,
            do_case(
                seats=tc_seats,
                runs=tc_runs,
                groups=tc_groups)))
    count += 1
    line = f_in.readline()
f_in.close()
f_out.close()
