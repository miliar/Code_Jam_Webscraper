'''
Created on 2009/9/3

@author: Cody
'''

filename = "C-small-attempt0"
fin = open(filename + ".in", "r")
fout = open(filename + ".out", "w")

N = int(fin.readline())

welcome = ['w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m']
global count
def findout(pat,wel):
    global count
    if wel == []:
        count += 1
    else:
        if pat != "" and pat[0] == wel[0]:
            findout(pat[1:],wel[1:])
        if len(pat) > 0:
            findout(pat[1:],wel)                

for i in range(N):
    count = 0
    pattern =  fin.readline()[:-1]
    print pattern    
    findout(pattern,welcome)
    count = count % 10000
    if count < 10:
        count = "000"+str(count)
    elif count <100:
        count = "00"+str(count)
    elif count <1000:
        count = "0"+str(count)
    
    fout.write("Case #"+str(i+1)+": "+str(count)+'\n')
