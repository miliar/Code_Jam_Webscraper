def game():
    num = int(raw_input())
    for i in xrange (num):
        #case i
        x1 = int(raw_input())
        nums1 = getAnswerList(x1)        
        x2 = int(raw_input())
        nums2 = getAnswerList(x2)

        sames = 0
        res = -1

        for x in nums1:
            for y in nums2:
                if x==y:
                    res = x
                    sames += 1
        if sames ==0:
            print "Case #" + str(i+1) + ": " + "Volunteer cheated!"
        elif sames == 1:
            print "Case #" + str(i+1) + ":", res
        else:
            print "Case #" + str(i+1) + ": " + "Bad magician!"
           
def readints():
    return [int(x) for x in raw_input().split(' ')]

def getAnswerList(x1):
    res = []
    for j in xrange (1,5):
            nums = readints()
            if j == x1:
                res = nums
    return res
    
            
game()
