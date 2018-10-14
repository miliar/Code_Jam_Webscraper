from __future__ import with_statement
from optparse import OptionParser
import sys


def time_to_minutes(in_time):
    "Convert time from HH:MM string to integer number of minutes from midnight"
    return int(in_time[:2]) * 60 + int(in_time[3:])


def process(in_file, out_file):
    num_cases = int(in_file.readline())
    for case in xrange(1, num_cases+1):
        print 'Case #%d:' % case
        demand_a = {}
        demand_b = {}
        turnaround_time = int(in_file.readline())
        num_a_runs, num_b_runs = [int(x) for x in in_file.readline().split(' ')]
        for run in range(num_a_runs):
            departure, arrival = [time_to_minutes(x) for x in in_file.readline().split(' ')]
            available = arrival + turnaround_time
            if departure not in demand_a:
                demand_a[departure] = 0
            demand_a[departure] += 1
            if available not in demand_b:
                demand_b[available] = 0
            demand_b[available] -= 1
        for run in range(num_b_runs):
            departure, arrival = [time_to_minutes(x) for x in in_file.readline().split(' ')]
            available = arrival + turnaround_time
            if departure not in demand_b:
                demand_b[departure] = 0
            demand_b[departure] += 1
            if available not in demand_a:
                demand_a[available] = 0
            demand_a[available] -= 1

        #print sorted(demand_a)
        max_demand_a, current_demand = 0, 0
        for key in sorted(demand_a):
            current_demand += demand_a[key]
            if current_demand > max_demand_a:
                max_demand_a = current_demand
        #print sorted(demand_b)
        max_demand_b, current_demand = 0, 0
        for key in sorted(demand_b):
            current_demand += demand_b[key]
            if current_demand > max_demand_b:
                max_demand_b = current_demand

        out_file.write('Case #%d: %d %d\n' % (case, max_demand_a, max_demand_b))


def main():
    parser = OptionParser(usage="""\
Triangle Trilemma

Usage: %prog [options]
""")
    parser.add_option('-i', '--input_file',
            type='string', action='store')
    parser.add_option('-o', '--output_file',
            type='string', action='store')
    opts, args = parser.parse_args()
    if not opts.input_file or not opts.output_file:
        parser.print_help()
        sys.exit(1)

    with open(opts.input_file, 'r') as i:
        with open(opts.output_file, 'w') as o:
            process(i, o)


if __name__ == '__main__':
    main()

