'''
Created on Apr 14, 2012

@author: I067729
'''

def convert_G_to_E():
    my_dict = {'a' : 'y', 'b' : 'h', 'c' : 'e', 'd' : 's', 'e' : 'o',
               'f' : 'c', 'g' : 'v', 'h' : 'x', 'i' : 'd', 'j' : 'u',
               'k' : 'i', 'l' : 'g', 'm' : 'l', 'n' : 'b', 'o' : 'k',
               'p' : 'r', 'q' : 'z', 'r' : 't', 's' : 'n', 't' : 'w',
               'u' : 'j', 'v' : 'p', 'w' : 'f', 'x' : 'm', 'y' : 'a', 'z' : 'q' ,' ' : ' '}
    
    i, j = 0, 0
    fRead = open('A-small-attempt0.in', 'rU')
    fWrite = open('final.txt', 'w')
    for line in fRead:
        if i == 0 :
            n = int(line)
            i = i + 1
        else :
            j = 0
            resString  = ''
            lineString = line
            length  = len(lineString)
            while j < length - 1: 
                if lineString[j] in my_dict:
                    resString = resString + my_dict.get(lineString[j])
                    j = j + 1
  
            finalString  = "Case #%d: " % i + resString + '\n'
            i = i + 1
            fWrite.write(finalString)
     
if __name__ == "__main__" : convert_G_to_E()  
