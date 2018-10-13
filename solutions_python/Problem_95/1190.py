table={}

def init_table():
     for i in range(ord('a'), ord('z')+1):
        table[chr(i)]=" "
        
def make_table(crypted, org):
    for i in range(0, len(crypted)-1):
        if(crypted[i] != " "):
            table[crypted[i]]=org[i]  


def print_table():
    for i in range(ord('a'), ord('z')+1):
        print(chr(i) + " " + table[chr(i)])  

def decrypt(str):
    buf=''
    for i in range(0,len(str)):
        if(str[i] != " " and str[i] != "\n"):
            buf+=table[str[i]]
        elif(str[i] == " "):
            buf+=" "

    return buf
    
init_table()

make_table("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand")
make_table("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities")
make_table("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up")
table['q']='z'
table['z']='q'
#print_table()

f = open('test.txt', 'r')
count = int(f.readline())
for i in range(count):
    str=f.readline();
    #print(str)
    print('Case #' + ascii(i+1)+": " + decrypt(str))
    
    
