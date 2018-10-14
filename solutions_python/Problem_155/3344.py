import sys

for num in range(int(sys.stdin.readline().strip())):
    max_s, s = sys.stdin.readline().split()

    people_added = 0
    num_standing = 0
    for i, c in enumerate(s):
        while num_standing < i:
            people_added+=1
            num_standing+=1
        num_standing += int(c)


    print("Case #{}: {}".format(num+1, people_added))
