if __name__ == '__main__':
    inf = open('A-small-attempt0.in')
    outf = open('magic.out', 'w')
    
    T = int(inf.readline())
    for t in range(1, T+1):
        BAD_MAG = False
        ANS_FND = False
        ANS = None
        
        r1 = int(inf.readline())
        for x in range(1, 5):
            if x == r1:
                nums1 = inf.readline().split()
                #nums1 = map(int, nums1)
                #nums1.sort()
            else:
                inf.readline()

        r2 = int(inf.readline())
        for x in range(1, 5):
            if x == r2:
                nums2 = inf.readline().split()
                #nums2 = map(int, nums2)
                #nums2.sort()
            else:
                inf.readline()
        
        for i in range(4):
            for j in range(4):
                if BAD_MAG:
                    break
                if nums1[i] == nums2[j]:
                    if ANS_FND:
                        BAD_MAG = True
                        ANS_FND = False
                        break
                    else:
                        ANS_FND = True
                        ANS = nums1[i]
        
        if BAD_MAG:
            outf.write('Case #%d: Bad magician!\n' % t)
        elif ANS_FND:
            outf.write('Case #%d: %s\n' % (t, ANS))
        else:
            outf.write('Case #%d: Volunteer cheated!\n' % t)
    
    inf.close()
    outf.close()
    
