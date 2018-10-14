'''
Created on 2009-7-10

@author: roamer
'''

def combination(n,m,out,str1,str2):
    global total
    if(m==-1):
        return 1
    x=n
    while x>=m:
        out.append(x)
        a = str2[x]
        b = str1[len(str1) - len(out)]
        if a != b:
            out.pop()
            x-=1
            continue;
        if(combination(x-1,m-1,out,str1,str2)):
            total += 1
        out.pop()
        x-=1
    return 0

if __name__ == "__main__":


    global total
    total = 0
    out = []
    txt = "welcome to code jam"
    f = open('../datain/welcome_to_dode_jam.txt','r')
    totalcase =  int(f.readline().strip())
    i = 0
    while i < totalcase:
        real_txt = "";
        string = f.readline().strip()
        for char in string:
            if char in txt:
                real_txt += char
        a = real_txt.rfind(txt[len(txt) - 1])
        b = real_txt.find(txt[0])
        if(a < b or a == -1 or b == -1):
            total = 0
        else:
            real_txt = real_txt[b:a+1]
            combination(len(real_txt) - 1,len(txt) - 1,out,txt,real_txt)
        i += 1        
        retsult = str(total % 10000)
        total = 0
        print("Case #%d: %s" % (i,retsult.zfill(4)))
    f.close()