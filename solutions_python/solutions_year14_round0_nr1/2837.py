    
def doMagic(nums1, nums2):
    card = 0
    for i in nums1:
        if i in nums2:
            if card == 0:
                card = i
            else:
                return 'Bad magician!'
    if card == 0:
        return 'Volunteer cheated!'
    else:
        return card


f = open('input.txt','r')
N = int(f.readline())
print N

fout = open('output.txt','w')

for i in range(N):
    row1 = int(f.readline())
    for j in range(4):
        if j == row1-1:
            nums1 = f.readline().strip().split(' ')
        else:
            f.readline()
    
    row2 = int(f.readline())
    
    for j in range(4):
        if j == row2-1:
            nums2 = f.readline().strip().split(' ')
        else:
            f.readline()
    
    fout.write("Case #%d: %s\n"%(i+1, doMagic(nums1, nums2)))
    
f.close()
fout.close()
    
    
    
    