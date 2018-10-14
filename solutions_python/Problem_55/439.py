# Google Code Jam 2010.
# Larry Engholm, 5/8/2010

# Problem description:
# http://code.google.com/codejam/contest/dashboard?c=433101#s=p2

def test(trains, seats, groups):
    earned = 0
    for t in range(trains):
        passengers = 0
        riders = []
        while len(groups) > 0 and passengers + groups[0] <= seats:
            passengers += groups[0]
            riders.append(groups.pop(0))
        earned += passengers
        groups.extend(riders)
    return earned

def main():
    file = open('c:/Documents and Settings/Larry/My Documents/Downloads/C-small-attempt0.in')
    numTests = int(file.readline())
    for i in range(numTests):
        (trains, seats, numGroups) = map(int, file.readline().split())
        groups = map(int, file.readline().split())
        print 'Case #{0}: {1}'.format(i+1, test(trains, seats, groups))
main()
