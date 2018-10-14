
def do(nums1, nums2, output):
    #print("called with: ", nums1, nums2)
    
    if len(nums1) < 2 or len(nums2) < 2:
        return output;
    
    while len(nums1) > 1 and len(nums2) > 1 and nums1[1] == nums2[1]:
        output += min(nums1[0], nums2[0])
        tmp = min(nums1[0], nums2[0])
        nums1[0] -= tmp
        nums2[0] -= tmp
        # print("output is ", output)
        if (nums1[0] == 0):
            #print("pop1 ", nums1)
            nums1.pop(0)
            nums1.pop(0)
        if (nums2[0] == 0):
            #print("pop2 ", nums2)
            nums2.pop(0)
            nums2.pop(0)
        #print("while", nums1, nums2, "output", output)
        
    leftgone1 = nums1[2:]
    rightgone1 = nums2[2:]
    leftgone2 = nums1[2:]
    rightgone2 = nums2[2:]
    nums2a = nums2[:]
    nums1a = nums1[:]
    
    output = max(do(leftgone1, nums2a, output), do(nums1a, rightgone1, output), do(leftgone2, rightgone2, output));
    #print("output2 is ", output)    
    return output



def tonums(inline):
    contestantsTmp = inline.split(" ")
    contestants = []
    for i in range(0, len(contestantsTmp)):
        contestants.append(int(contestantsTmp[i]));
    return contestants

filename = "C:\\D\\codejam\\C-small-attempt0.in"
out = open(filename + ".out", "w")
f = open(filename)
number = int(f.readline())
for i in range(number):
    f.readline()
    a = ("Case #" + str(i+1) + ": " + str(do(tonums(f.readline()), tonums(f.readline()), 0)))
    print(a)
    out.write(a + "\n")