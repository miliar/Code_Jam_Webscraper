f = open("A-large.in")
o = open("outputAL.txt","w")
no_of_cases = f.readline()

def check_inc(num):
    no = list(str(num))
    for i in range(len(no)-1):
        if no[i]>no[i+1]:
            return int(''.join(no[i+1:]))+1
    return 0

def B():
    for i in range(int(no_of_cases)):
        number = int(f.readline())
        no = 1
        while no:
            no = check_inc(number)
            number -= no
        o.write("Case #"+str(i+1)+": "+str(number)+"\n")
    
def A():
    for i in range(int(no_of_cases)):
        input = f.readline()
        s,k = input.split()
        s = list(s)
        k = int(k)
        bin = [0 if x=='-' else 1 for x in s]
        count = 0
        for j in range(len(bin)-k+1):
            if not bin[j]:
                for x in range(k):
                    bin[j+x] ^= 1
                    count+=1
        if len(set(bin)) == 1 and set(bin)=={1}:
            o.write("Case #"+str(i+1)+": "+str(count//k)+"\n")
        else:
            o.write("Case #"+str(i+1)+": IMPOSSIBLE\n")

A()