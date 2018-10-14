import sys

in_file = open('A-large.in', 'r')
out_file = open('A-large.out', 'w')

sys.stdin = in_file
sys.stdout = out_file

for t in range(int(input())):
    s, audience = input().split()
    sum, friends = int(audience[0]), 0
    for i in range(1, int(s)+1):
        d = i - sum
        if d > 0:
            friends += d
            sum += d
        sum += int(audience[i])
    print('Case #{0}: {1}'.format(t+1, friends))

in_file.close()
out_file.close()