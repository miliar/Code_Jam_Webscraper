import sys
import os



def check_len(line):

    
    n = len(line)  - 1 
    counter = n
    while counter > 0 :
	if int(line[counter]) < int(line[counter-1]):
           c_imo = line[counter-1]
           if c_imo != 0:
            
              line[counter-1] = int(c_imo) - 1
              # fill the rest to 99999 - from i to length set to 9999
              for j in range(counter,len(line),1):
                  line[j] = int('9')
           else:
              print " error"
        counter -=  1 
        line[counter] = int(line[counter])  
    line[counter] = int(line[counter])       
    return line 
     
          

def main(args=None):
    
    target = open("/home/siyer/code_jam/result.txt", 'w')
    target.truncate()
    f = open("/home/siyer/code_jam/input.txt")
    next(f)
    cnt= 0
    for line in f:
        cnt = cnt + 1
        linestr = line.strip()
        content =  [] 
        if linestr:
           content.extend([(x) for x in linestr])
           counter = check_len(content)
        str1 = ''.join(str(e) for e in counter)
        result = str1.lstrip("0")
        target.write( "Case #"+ str(cnt) + ": "+ result) 
        target.write("\n")
   
    target.close()

if __name__ == "__main__":
    sys.exit(main())

