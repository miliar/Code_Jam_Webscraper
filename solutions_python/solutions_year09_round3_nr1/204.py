charStr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def vchar(intv):
    if intv>=0 and intv<=9:
        return intv.__str__()
    else:
        return charStr[intv-10]

def minimum(str):
    dict={}
    ln = len(str)
    ostr=""
    value=2
    usedNull=False
    
    dict[str[0]] = 1
    ostr+='1'
    
    
    for i in range(1,ln):
        chr = str[i]
        if dict.has_key(chr):
            ostr+=vchar(dict[chr])
        else:
            if usedNull:
                dict[chr] = value
                ostr+=vchar(value)
                value+=1
            else:
                dict[chr] = 0
                ostr+='0'
                usedNull = True
    if value == 1:
        value=2
    return int(ostr,value)


def main():
    file = open("A-Large.in","r")
    t=int(file.readline())
    for i in range(t):
        line = file.readline().strip()
        print "Case #"+(i+1).__str__()+": "+minimum(line).__str__()
        
main()