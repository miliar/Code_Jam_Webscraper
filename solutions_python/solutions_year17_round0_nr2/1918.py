
# coding: utf-8

# In[32]:

def quiz(path):
    f = open(path, 'r')
    ans_file = open("C:/answer.txt",'w')
    questions = [i for i in f.readlines()]
    
    
    questions.pop(0)
    
    for i in range(len(questions)):
        num = questions[i][-2]
        
        answer = tidy(int(num))
        print(i, " ",answer)
        wr = "Case #" + str(i+1) + ": " + str(answer) + "\n"
        ans_file.write(wr)

        
    print(answer)
    
    f.close()
    ans_file.close()
    
def tidy(num):
    
    t = False
    
    n = list(str(num))
    
    while (t is False):
        
        for i in range(1,len(n)):
            if int(n[i-1]) > int(n[i]):
                n[i-1] = str(int(n[i-1]) - 1)
                n[i:] = ["9" for i in n[i:]]
                
                break
                
                
        
        i_num = "".join(n)
        
        n = list(str(int(i_num)))
        
        
        t = is_tidy(int(i_num))
        
    return int(i_num)

def is_tidy(n):
    if n < 10:
        return True
    
    n = str(n)
    
    for i in range(1, len(n)):
        if int(n[i-1]) > int(n[i]):
            return False
            
            
        
    return True


# In[33]:

quiz("C:/B-small-attempt0.in")


# In[ ]:



