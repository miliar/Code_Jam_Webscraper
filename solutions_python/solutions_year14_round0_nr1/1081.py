testcasenum = int(input())

for tc in range(testcasenum):
    row = int(input()) - 1
    nums1 = set()
    for i in range(4):
        line = input()
        if i == row:
            for n in line.split():
                nums1.add(int(n))
    row = int(input()) - 1
    nums2 = set()
    for i in range(4):
        line = input()
        if i == row:
            for n in line.split():
                nums2.add(int(n))
    result = nums1 & nums2
    res = ""
    if len(result) == 1:
        res = list(result)[0]
    elif len(result) > 1:
        res = "Bad magician!"
    else:
        res = "Volunteer cheated!"
    print("Case #{}: {}".format(tc + 1, res))
