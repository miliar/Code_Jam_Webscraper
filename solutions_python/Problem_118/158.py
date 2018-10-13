
fsf = None
import pgcj13_C
def generate():
    global fsf
    fsf = open("xlarge_fs.txt", "w")
    #assumes root can be only 1,0 and 
    #2 can be only at the first or in the middle
    
    for i in range(0, 2**25):
        part = bin(i)[2:]
        
        t = part + part[::-1]
        isValid(int(t))
        t = list(t)
        t[0] = "2"
        t[-1] = "2"
        isValid(int(''.join(t)))
        
        t = part + "0" + part[::-1]
        isValid(int(t))
        t = list(t)
        t[0] = "2"
        t[-1] = "2"
        isValid(int(''.join(t)))
        
        t = part + "1" + part[::-1]
        isValid(int(t))
        t = list(t)
        t[0] = "2"
        t[-1] = "2"
        isValid(int(''.join(t)))
        
        isValid(int(part + "2" + part[::-1]))
        


def isValid(num):
    global fsf
        
    fs = num**2
    if (pgcj13_C.isPalindrome(fs)):
        fsf.write(str(fs) + "\n")
    
    
def postproc():
    fsf = open("xlarge_fs.txt")
    outf = open("xlarge_fs_post.txt", "w")
    fs = []
    last = -1
    for line in fsf:
        line = line.strip()
        if len(line) > 100:
            print("!")
            continue;
        num = int(line)
        if num == 0:
            print("0")
            continue
        if last == num:
            print("d")
            continue
        fs.append(num)
        last = num
    print("sort")
    list2 = sorted(fs)
    print(len(list2))
    
    for num in list2:
        outf.write(str(num) + "\n")
    outf.close()
    
            

if __name__ == '__main__':
    #generate()
    postproc()