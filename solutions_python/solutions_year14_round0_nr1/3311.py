#!/usr/bin/env python

class BadMagicianException(BaseException):
    """ Intersection too large. """

class CheatingVolunteerException(BaseException):
    """ Empty intersection. """

def solve(lines):
    choices = int(lines[0]), int(lines[5])
    rows = lines[choices[0]], lines[choices[1] + 5]
    sets = set(rows[0].split(' ')), set(rows[1].split(' '))
    intersection = sets[0] & sets[1]
    if len(intersection) == 1:
        return iter(intersection).next()
    elif len(intersection) > 0:
        raise BadMagicianException()
    else:
        raise CheatingVolunteerException()

if __name__ == '__main__':
    with open('A-small-attempt0.in') as handle:
        _ = handle.next()
        lines, case = [], 1
        for line in handle:
            lines.append(line.strip())
            if len(lines) > 9:
                try:
                    number = solve(lines)
                    print('Case #{case}: {number}'.format(case=case,
                                                          number=number))
                except BadMagicianException:
                    print('Case #{case}: Bad magician!'.format(case=case))
                except CheatingVolunteerException:
                    print('Case #{case}: Volunteer cheated!'.format(case=case))
                lines = []
                case += 1
