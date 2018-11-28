from sys import stdin
import logging as log

log.basicConfig(level=log.DEBUG, format='%(levelname)s:%(pathname)s:%(lineno)s: %(message)s')


def count_up(max_shy, shy_counts):
    standing = 0
    total_extras = 0

    for level in range(max_shy + 1):
        members = shy_counts[level]
        log.debug('Checking level %d / %d: %d standing, %d at this level', level, max_shy, standing, members)

        if standing >= level:
            # everyone at this level stands up
            standing += members
            log.debug('%d people stand up', members)
        else:
            # need more people at some lower level than this
            missing = level - standing
            log.debug('Adding %d people for level %d to stand up', missing, level)
            total_extras += missing
            standing += members + missing
            log.debug('%d people stand up', members)

    return total_extras

def parse_input(solver):
    num_cases = int(stdin.readline())

    log.debug('Solving %d cases in total', num_cases)

    for case in range(1, num_cases + 1):
        max_shy_str, shy_counts_str = stdin.readline().rstrip().split(' ')
        log.debug('max: %s counts: %s', repr(max_shy_str), repr(shy_counts_str))

        max_shy = int(max_shy_str)
        shy_counts = [int(c) for c in shy_counts_str]

        log.debug('Solving case %d...', case)

        result = solver(max_shy, shy_counts)
        print 'Case #%d: %s' % (case, result)


if __name__ == '__main__':
    parse_input(count_up)
