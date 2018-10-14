f = open('A-small-attempt2.in')
fout = open('out', 'w')

num_test = int(f.readline())
for i in range(num_test):
    idx_1 = int(f.readline())
    lst = [list(map(lambda x: int(x), str.split(f.readline(), ' '))) for i in range(0,4)]
    nums = set(lst[idx_1 - 1])

    idx_2 = int(f.readline())
    lst = [list(map(lambda x: int(x), str.split(f.readline(), ' '))) for i in range(0,4)]
    nums2 = set(lst[idx_2 - 1])

    res = nums.intersection(nums2)
    
    if len(res) == 1:
        fout.write("Case #%d: %d\n" % (i + 1, res.pop()))
    elif len(res) == 0:
        fout.write("Case #%d: Volunteer cheated!\n" % (i + 1))
    elif len(res) > 1:
        fout.write("Case #%d: Bad magician!\n" % (i + 1))
