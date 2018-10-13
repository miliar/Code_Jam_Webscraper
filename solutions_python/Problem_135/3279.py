def read_square(f):
    square = []
    for i in range(4):
        square.append([ int(x) for x in f.readline().split(' ') ])
    return square

with open('data.in', 'r') as f:
    test_cases = int(f.readline())
    for i in range(test_cases):
        num1 = int(f.readline())-1
        nums1 = read_square(f)
        num2 = int(f.readline())-1
        nums2 = read_square(f)
        res = list(set(nums1[num1]).intersection(set(nums2[num2])))
        if len(res) == 1:
            print("Case #" + str(i+1) + ": " + str(res[0]))
        elif len(res) == 0:
            print("Case #" + str(i+1) + ": Volunteer cheated!")
        else:
            print("Case #" + str(i+1) + ": Bad magician!")
