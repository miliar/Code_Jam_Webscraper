
# coding: utf-8

# In[26]:

def quiz(path):
    f = open(path, 'r')
    ans_file = open("C:/answer.txt",'w')
    questions = [i for i in f.readlines()]
    
    
    questions.pop(0)
    
    #print(questions)
    
    for i in range(len(questions)):
        ques = questions[i].split(" ")
        
        #print(num)
        
        answer1, answer2 = bathroom(int(ques[0]),int(ques[1][:-1]))
        #print(i, " ",answer)
        wr = "Case #" + str(i+1) + ": " + str(answer1) +" " +str(answer2) + "\n"
        ans_file.write(wr)

    
    f.close()
    ans_file.close()
    
def bathroom(n,k):
    
    stall = [int(n)]
    
    for i in range(int(k)-1):
        ma = max(stall)
        
        stall.remove(ma)
        
        if int(ma%2) is 1:
            stall.append((ma-1)/2)
            stall.append((ma-1)/2)
        else:
            stall.append(ma/2)
            stall.append(ma/2-1)
        
    ma = max(stall)
    
    
    if int(ma%2) is 1:
        stall_max = stall_min = (ma-1)/2
    else:
        stall_max = (ma/2)
        stall_min = (ma/2-1)
        
    return int(stall_max),int(stall_min)
        


# In[27]:

quiz("C:/C-small-1-attempt0.in")


# In[ ]:



