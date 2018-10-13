import os
import sys

def get_time(line) :
    seq = line.split(" ")
    seq = seq[1:]
    orange = []
    blue = []
    for i in range(0,len(seq)-1) :
        if seq[i]=="O" :
            orange.append(int(seq[i+1]))
        elif seq[i] == "B" :
            blue.append(int(seq[i+1]))

    lor = sum(orange)
    lb = sum(blue)
  #  print lor
  #  print lb
    return max(lor,lb)
            
def get_next(index,seq,char) :
    sequence = seq[index:]
    try :
        n = sequence.index(char)
    except :
        return -1
    print sequence[n] + sequence[n+1]
    return int(sequence[n+1])

def move_to(current,target) :
    if current < target :
        current = current + 1 
    else :
        current = current -1
    return current

def main() :
    f=open("A-large.in")
    case = 1
    all_lines = f.readlines()
    all_lines = all_lines[1:]
    for line in all_lines :
        t=trial(line.split(" "))
        print "Case #"+str(case)+": "+str(t)
        case = case+1

def trial(seq) :
  #   print seq
     t = 0
     current = ""
     c_orange = 1 #position
     c_blue = 1
     index = 1
     while t < 100000 :
        # print "time" + str(t) 
         if index > len(seq)-2 :
           #  print "FINAL TIME"+str(t)
             return t

         current = seq[index] #O or B
       #  print "o/b " + str(c_orange) + str(c_blue)
         o_pushed = False 
         b_pushed = False 
#         do_push(current)
         if current=="O" :
             if can_push(c_orange, seq,index) :
                 do_push(c_orange,seq,index)
                 index=index+2
                 #t=t+1
                 o_pushed = True 

         elif current=="B" :
             if can_push(c_blue,seq,index) :
                 do_push(c_blue,seq,index)
                 index=index+2
                 #t=t+1
                 b_pushed = True 
         
         c_orange = do_move(o_pushed,c_orange, seq, index,"O")
         c_blue = do_move(b_pushed,c_blue, seq, index,"B")
         
         t=t+1

#
def can_push(c_orange,seq,index) :
  #  print "CANPUSH "+ str(c_orange) + str(seq[index+1])
    if c_orange == int(seq[index+1]) :
        return True
    return False

def do_push (c_orange , seq, index) :
   # print "Pushing"
    pass

def do_move(flag,c_orange,seq,index,string) :
   # print "DO MOVE index"+str(index)
    if flag :
        return c_orange
    try:
        next = (seq[index:].index(string))+2
    except :
        return -1
   # print "NEXT" + str(next+index-1)
    target = int(seq[next+index-1])
   # print "target "+str(target)
    if c_orange < target :
        c_orange = c_orange+1
    elif c_orange > target :
        c_orange = c_orange -1
    
    return c_orange
    
            
if __name__=="__main__" :
    main()
