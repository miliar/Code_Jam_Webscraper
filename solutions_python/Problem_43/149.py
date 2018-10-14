
import sys

inputfile="./A-large"

rp = [str(i) for i in range(10)] + [chr(i+97) for i in range(26)]
aa = rp[0]
rp[0] = rp[1]
rp[1] = aa

print rp
def main():
    
    output = Output()
    
    fd = open(inputfile + ".in", "r")
    pn = fd.readline()
    pn = int(pn.strip())
    
    
    for i in range(pn):
        line = fd.readline().strip()
        b = line
        cat = {}
        count = 0
        for s in line:
            if not cat.has_key(s):
                cat[s] = rp[count]
                count += 1
         
        aout = ""
        for s in line:
            aout += cat[s]
        
        if count == 1:
            out = int(aout, count+1)
        else:
            out = int(aout, count)
        output.record_line_case(i+1, str(out))
    

    output.out(inputfile + ".out", True)
 
def mi(s,i):
    min = 10
    min_i = None
    for j in range(len(s)):
        try:
            v = int(s[i+j])
        except IndexError:
            return min_i
        if min > v:
            min = v
            min_i = i+j
    return min_i
    
    
def next(s):
    pre = int(s[-1])
    for i in range(len(s)):
        j = -(i+2)
        try:
            d = int(s[j])
            if d < pre:
                print d,pre,j
                mini = -1
                for t in range(len(s)):
                    if s[-(t+1)] == s[-(t+2)]:
                        mini = -(t+3)
                    else:
                        break
                if s[mini] == s[j]:
                    mini -= 1
                a = s[mini]
                s[mini] = s[j]
                s[j] = a
                
                return s
            pre = d
        except IndexError:
            return nn(s)
        
def fromlist(list):
    out = ""
    for i in range(len(list)):
        out += list[i]
    return out
        
        
def tolist(s):
    list = []
    for i in range(len(s)):
        list += [s[i]]
    return list

def nn(s):
    list = []
    for i in range(len(s)):
        list += [s[i]]
    list.sort()
    
    out = ""
    for i in range(len(list)):
        out += list[i]

    for i in range(len(out)):
        if not out[i] == "0":
             out = out[i] + out[0:i] + "0" + out[i+1:]
            
            

    return out
   
    
        
            
    
            
       

def getsum(list):
    sum = 0
    for v in list:
        sum += v*v
    return sum
    
def get_next(v):
    v = str(v)
    o = []
    for i in v:
        o += [int(i)]
    return o
    
        
    
    #out.out("./test.out",False)












class Input:

        
    def get_map(self, string, h, w):
        string = string.strip("\n")
        a = string.split("\n")
        map = []
        for i in range(len(a)):
            map += [a[i].split(" ")]
        return map   
        
    
class Output:
    
    def __init__(self):
        self.output = {}
        
    def record_line_case(self, case_num, line):
        if self.output.has_key(case_num):
            self.output[case_num] += [line]
        else:
            self.output[case_num] =[line]
            
            
        
    def out(self, file_name, isFirstLine):
        case = "Case #No:"
        if isFirstLine:
            case += " "
        else:
            case += "\n"
        out = ""
        for key in self.output:
            out += case.replace("No", str(key))
            for v in self.output[key]:
                out += v + "\n"
        fd = open(file_name, "w")
        fd.write(out)
        fd.close
        





if __name__ == "__main__":
    main()