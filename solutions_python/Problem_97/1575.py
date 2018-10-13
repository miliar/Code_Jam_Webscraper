'''
Created on Apr 14, 2012

@author: I067729
'''
def recycle_numbers():
    fRead = open('C-small-attempt0.in', 'rU')
    fWrite = open('solution3_small.txt', 'w')
    i = 0
    for line in fRead:
        if i == 0:
            n = int(line)
            i =  i + 1
        else: 
            ctr = 0
            listString  = line.split()
                
            a, b = listString[0], listString[1]
            j = int(a)
            while j <= int(b):
                num = str(j)
                length = len(a)
                combinationslist = []
                if length == 2:
                    new_string = num[1] + num[0]
                    combinationslist = [int(new_string)]
                elif length == 3:
                    new_string1 = num[2] + num[0] + num[1]
                    new_string2 = num[1] + num[2] + num[0]
                    combinationslist = [int(new_string1), int(new_string2)] 
                
                for combn in combinationslist:
                    if len(str(combn)) == len(num) and combn > int(num) and combn <= int(b) and combn != int(num):
                        ctr = ctr + 1
                j = j + 1
            resString = "Case #%d: %s" % (i,ctr) + "\n"
            fWrite.write(resString)
            i = i + 1
   
if __name__ == "__main__" : recycle_numbers() 