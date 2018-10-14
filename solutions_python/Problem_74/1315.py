def bot(seq):
   stack = seq.strip().replace("B ","B")
   stack = stack.replace("O ","O").split()
   ostack = [x for x in stack if x[0]=='O']
   bstack = [x for x in stack if x[0]=='B']
   

   o_ctr = b_ctr = 1 # Initialize the robots
   steps = 0
   while len(stack):
       #Orange robot
       flag = True 
       if len(ostack):
           if int(ostack[0][1:]) == o_ctr and stack[0][0] == "O":
               stack.pop(0)
               ostack.pop(0)
               flag = False
           elif int(ostack[0][1:]) > o_ctr:
               o_ctr+=1
           elif int(ostack[0][1:]) < o_ctr:
               o_ctr-=1
       #Blue robot
       if len(bstack):      
           if flag and int(bstack[0][1:]) == b_ctr and stack[0][0] == "B":
               stack.pop(0)
               bstack.pop(0)
           elif int(bstack[0][1:]) > b_ctr:
               b_ctr+=1
           elif int(bstack[0][1:]) < b_ctr:
               b_ctr-=1
           
       steps+=1

   return steps


if __name__ == "__main__":
    f = open("bot.in")
    g = open("bot.o","w")
    for n,line in enumerate(f.readlines()[1:]):
        g.write("Case #%d: %d\n" %(n+1, bot(line[2:])))

