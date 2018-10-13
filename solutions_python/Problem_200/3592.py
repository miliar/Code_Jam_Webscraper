import sys
sys.setrecursionlimit(1500000)

def read():
    with open('B-large.in', 'r') as content_file:
        content = content_file.read()
        return content.split('\n')

a=read()
def makeTidy(n):
    str_n=str(n)
    str_len=len(str_n)
    counter=str_len-1
    back_counter=1
    while True:
        if istidy(str_n):
            return n
        n=n-(int(str_n[counter])+1)*back_counter
        back_counter*=10
        str_n=str(n)
        counter-=1
    
def istidy(n):
    n=str(n)
    for i in range(len(n)-1):
        if n[i]<=n[i+1]:
            continue
        return False
    return True
    
with open("answer_2_large.out", "w") as myfile:
    T=int(a[0])
    counter=0
    for case in range(1,T+1):
        counter+=1
        myfile.write("Case #{}: {}".format(counter,makeTidy(int(a[case]))))
        if counter<T:
            myfile.write("\n")
    print "Done"