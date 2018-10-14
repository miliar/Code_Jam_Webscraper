import sys
import random

def invite_friends(audience):
    have, invited = 0,0
    for shyness,n in enumerate(audience):
        gap = max(shyness - have - invited, 0)
        invited += gap
        have += int(n)
    return invited

def main():
    case = 1
    for line in open(sys.argv[1]).readlines()[1:]:
        smax, digits = line.split()
        friends = invite_friends(digits)
        print('Case #{}: {}'.format(case, friends))
        case +=1

main()
