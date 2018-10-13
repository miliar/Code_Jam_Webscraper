
# coding: utf-8

# In[7]:

def pan_cake(s, k):
    
    y = []
    
    count = 0
    
    s = list(s)
        
    for j in range(len(s) - k + 1):
        if is_happy(s[j]):
            continue
                
        else:
            s[j:j+k] = list(map(flip_pancake, list(s[j: j+k])))
            count += 1
                
    if all(map(is_happy,list(s))):
        return count
        
    else:
        return "IMPOSSIBLE"
            
            
def is_happy(pan_cake):
    if pan_cake is "+":
        return True
    
    return False
            
def flip_pancake(pan_cake):
    if is_happy(pan_cake):
        return "-"
    
    else:
        return "+"
    
def quiz(path):
    f = open(path, 'r')
    ans_file = open("C:/answer.txt",'w')
    questions = [i for i in f.readlines()]
    
    
    questions.pop(0)
    
    
    for i in range(len(questions)):
        q = questions[i].split(" ")
        answer = pan_cake(q[0], int(q[1][:-1]))
        print(i, " ",answer)
        wr = "Case #" + str(i+1) + ": " + str(answer) + "\n"
        ans_file.write(wr)
        
    print(answer)
    
    f.close()
    ans_file.close()

        
    


# In[9]:

quiz("C:\A-small-attempt1.in")


# In[ ]:



