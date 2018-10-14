
# coding: utf-8

# In[37]:

def isTidy(N):
    if(N < 9):
        return True
    #get unit and tenth place
    unitPlace = N % 10
    tenthPlace = (N // 10) % 10
    if(tenthPlace > unitPlace):
        return False
    else:
        return isTidy(N // 10)
    
def tidyNumber(N):
    n = N
    while n >= 0:
        if isTidy(n):
            return n
        n = n -1

f = open('./data/B-small-attempt1.in')
fOut = open('./data/B-small-attempt1.out',"w+")
t = f.readline()
print(t)
t = int(t)
for i in range(t + 1):
    num = f.readline()
    try:
        num = int(num)
        fOut.write('Case #' + str((i + 1)) + ":" + str(tidyNumber(num)) + "\n")
    except:
        pass
f.close()
fOut.close()


# In[ ]:



