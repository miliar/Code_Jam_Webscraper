import sys;

t = int(sys.stdin.readline());
palins = [ 1, 4, 9, 121, 484 ]
for i in range(t):
    line = sys.stdin.readline().split();
    start = int(line[0]);
    end = int(line[1]);
    matches = [y for y in range(start,end+1) if y in palins]
    print('Case #{0}: {1}'.format(i+1, len(matches)));




