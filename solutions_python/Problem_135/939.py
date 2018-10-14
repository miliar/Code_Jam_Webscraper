inpfile =open('C:/Users/Dane/Desktop/CJ/input1.txt','r')



def firstround( lt,num ):
    return lt[num-1]

def secondround( lt,num ):
    return lt[num-1]


def main():
    list1 = [[],[],[],[]]
    list2 = [[],[],[],[]]
    
    
    
    x = int(inpfile.readline())
    right =[]
    for i in range(0,x):
        list1 = [[],[],[],[]]
        list2 = [[],[],[],[]]
        right += [0]
        line1 = int(inpfile.readline())
        for count in range(0,4):
            test = inpfile.readline()
            nums = test.split()
            for num in nums:
                list1[count] += [int(num)]
                
        line2 = int(inpfile.readline())
        for count2 in range(0,4):
            test2 = inpfile.readline()
            nums2 = test2.split()
            for num2 in nums2:
                list2[count2] += [int(num2)]
        for l1 in firstround(list1, line1):
            for l2 in secondround(list2,line2):
                if l1 == l2:
                    correct = l1
                    right[i] += 1
        
        if right[i] == 1:
            with  open('C:/Users/Dane/Desktop/CJ/output1.txt','a') as out1:
                out1.write('Case #%d: %d' % (i+1, correct))
                out1.write('\n')
            
           
        elif right[i] == 0:
            with  open('C:/Users/Dane/Desktop/CJ/output1.txt','a') as out2:
                out2.write('Case #%d: Volunteer cheated!' % (i+1))
                out2.write('\n')
            
        elif right[i] > 1:
            with  open('C:/Users/Dane/Desktop/CJ/output1.txt','a') as out3:
                out3.write('Case #%d: Bad magician!' % (i+1))
                out3.write('\n')
            
    
                
                    
        
    
main()





