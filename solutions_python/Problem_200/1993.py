f = file("tidy-eff-output.txt","w")
def create_tidy(l):
    for i in xrange(len(l)-1):
        if l[i]>l[i+1]:
            l[i]= str(int(l[i])-1)
            l[i+1:]=["9" for j in xrange(len(l)-i-1)]
            return l
    return l

def check_tidy(n):
    string = str(n)
    for i in xrange(len(string)-1):
        if string[i]>string[i+1]:
            return False
    return True

t = int(raw_input())
for _ in xrange(1,t+1):
    i = raw_input()
    temp = int("".join(create_tidy(list(str(i)))))
    while not check_tidy(temp):
        temp =  int("".join(create_tidy(list(str(temp)))))
    f.write("Case"+" #"+str(_)+": "+str(temp))
    f.write("\n")

f.close()