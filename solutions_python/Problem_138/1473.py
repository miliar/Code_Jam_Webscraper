lines = [line.strip() for line in open("c:\Users\Mingan\Downloads\D-large.in","r")]
data = []
output = open("c:\Users\Mingan\Downloads\Cookie Output.txt","w")

def clean_data(lines,data):
    for i in lines:
        data.append(list(i))
        temp = []
        temp2 = []
        if len(data[-1]) <= 3:
            temp2.append(float(''.join(data[-1])))
        else:        
            for j in data[-1]:
                if j != " ":
                    temp.append(j)
                else:
                    temp2.append(float(''.join(temp)))
                    temp = []
            temp2.append(float(''.join(temp)))
        data[-1] = temp2
    return data            

data = clean_data(lines,data)


#data = [[4.0], [1.0], [0.5], [0.6], [2.0], [0.7, 0.2], [0.8, 0.3], [3.0], [0.5, 0.1, 0.9], [0.6, 0.4, 0.3], [9.0], [0.186, 0.389, 0.907, 0.832, 0.959, 0.557, 0.3, 0.992, 0.899], [0.916, 0.728, 0.271, 0.52, 0.7, 0.521, 0.215, 0.341, 0.458]]


T = int(data[0][0])
data.remove([T])

class Player(object):
    def __init__(self):
        self.N = 0
        self.item_list = 0
        self.picked = None
        self.other_picked = None
        self.warpoints = 0
        self.decpoints = 0
        self.Ken_list = 0
        self.lie = 0
        
    def get_ready(self,N,w_items):
        self.N = N
        self.item_list = w_items
        self.picked = None
        self.other_picked = None
    
    def reset_war(self):
        self.warpoints = 0
    
    def reset_dec(self):
        self.decpoints = 0
        
    def weight(self):
        if type(self.item_list) is not float:
            self.item_list = sorted(self.item_list)
        else:
            self.item_list = [self.item_list]

    def pick_and_lie(self):        
        self.picked = None
        for i in range(len(self.item_list)):
            if self.item_list[i] > min(Ken.item_list):
                self.picked = self.item_list[i]
                break
        if self.picked == None:
            self.picked = self.item_list[0]
        #LIE telling I picked something a little bit smaller than his minimum.
        self.lie = float(max(Ken.item_list) + 0.1)
        Ken.other_picked = self.lie
                    
        self.item_list.remove(self.picked)
        self.N = self.N - 1
        
    def pick_and_tell_Naomi(self):
        self.picked = None
        self.picked = max(self.item_list)
        self.item_list.remove(self.picked)
        self.N = self.N - 1
        Ken.other_picked = self.picked

    def pick_and_tell_Ken(self):
            self.picked = None
            for i in range(len(self.item_list)):
                if self.item_list[i] > self.other_picked:
                    self.picked = self.item_list[i]
                    break
            if self.picked == None:
                self.picked = self.item_list[0]
            self.item_list.remove(self.picked)
            self.N = self.N - 1
            Naomi.other_picked = self.picked
            
    def forget(self):
        self.other_picked = None     
        
def get_list(data):
    item_list = data[0]
    data.remove(item_list)
    return data,item_list
           

def balance_picks(j):
    if float(Naomi.picked) > float(Ken.picked):
        Naomi.warpoints += 1
    else:
        Ken.warpoints += 1

def balance_picks_dec():
    if Naomi.picked > Ken.picked:
        Naomi.decpoints += 1
    else:
        Ken.decpoints += 1
        
Naomi = Player()  
Ken = Player()         
for i in range(T):
    N = int(data[0][0])
    data.remove([N])
    item_list_N = get_list(data)[1]
    Naomi.get_ready(N,item_list_N)
    item_list_K = get_list(data)[1]
    Ken.get_ready(N,item_list_K)
    Naomi.reset_war()
    Ken.reset_war()
    for j in range(N):
        Naomi.weight()
        Ken.weight()
        Naomi.pick_and_tell_Naomi()
        Ken.pick_and_tell_Ken()
        balance_picks(j)
        Naomi.forget()
        Ken.forget()
    Naomi.get_ready(N,item_list_N)
    Ken.get_ready(N,item_list_K)
    Naomi.reset_dec()
    Ken.reset_dec()
    for k in range(N):
        Naomi.weight()
        Ken.weight()
        Naomi.Ken_list = Ken.item_list
        Naomi.pick_and_lie()
        Ken.pick_and_tell_Ken()
        balance_picks_dec()
        Naomi.forget()
        Ken.forget()
    print "Case #" +str(i+1)+": "+str(Naomi.decpoints)+" "+str(Naomi.warpoints)

counter = 1
solutions = []
for i in data:
    solution = go_go(i)
    print "Case #" + str(counter) + ": " +str(solution)
    solutions.append("Case #" + str(counter) + ": " +str(solution))
    counter += 1
for i in solutions:
    a=str(i)+str("\n")
    output.write(a)
output.close()    