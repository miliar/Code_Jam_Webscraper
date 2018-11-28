from __future__ import with_statement
from optparse import OptionParser
import sys


def process(in_file, out_file):
    num_cases = int(in_file.readline())
    for case in xrange(1, num_cases+1):
        print 'Case #%d:' % case
        all_engines = []
        num_switches = 0
        num_engines = int(in_file.readline())
        for i in range(num_engines):
            all_engines.append(in_file.readline().strip())
        remaining_engines = all_engines[:]
        num_queries = int(in_file.readline())
        for i in range(num_queries):
            this_query = in_file.readline().strip()
            if this_query in remaining_engines:
                remaining_engines.remove(this_query)
            if len(remaining_engines) == 0:
                num_switches += 1
                remaining_engines = all_engines[:]
                remaining_engines.remove(this_query)
        out_file.write('Case #%d: %d\n' % (case, num_switches))


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

