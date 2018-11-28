fyl=raw_input("input filename:")
inp=open(fyl,"r+")
text=inp.readlines()
inp.close()
case=int(text[0])
case=case

def main(ln):
    
    count=0
    for x in range(0,4):
     num_x=0
     num_o=0
     num_t=0
     for y in range(0,4):
      if ln[x][y]=='X':
       num_x+=1
      elif ln[x][y]=='O':
       num_o+=1
      elif ln[x][y]=='T':
       num_t+=1

     if num_x==4:
      return "X won"
      count+=1
      break
     if num_o==4:
      return "O won"
      count+=1
      break
     if num_x==3 and num_t==1:
      return "X won"
      count+=1
      break
     if num_o==3 and num_t==1:
      return "O won"
      count+=1
      break

    for y in range(0,4):
     num_x=0
     num_o=0
     num_t=0
     for x in range(0,4):
      if ln[x][y]=='X':
       num_x+=1
      elif ln[x][y]=='O':
       num_o+=1
      elif ln[x][y]=='T':
       num_t+=1
     if num_x==4:
      return "X won"
      count+=1
      break
     if num_o==4:
      return "O won"
      count+=1
      break
     if num_x==3 and num_t==1:
      return "X won"
      count+=1
      break
     if num_o==3 and num_t==1:
      return "O won"
      count+=1
      break
    num_x=0
    num_o=0
    num_t=0
    for x in range(0,4):
     for y in range(0,4):
      if x==y:
       if ln[x][y]=='X':
        num_x+=1
       elif ln[x][y]=='O':
        num_o+=1
       elif ln[x][y]=='T':
        num_t+=1
    if num_x==4:
      return "X won"
      count+=1
      
    if num_o==4:
      return "O won"
      count+=1
      
    if num_x==3 and num_t==1:
      return "X won"
      count+=1
      
    if num_o==3 and num_t==1:
      return "O won"
      count+=1
      
    diag=[]
    diag.append(ln[0][3])
    diag.append(ln[1][2])
    diag.append(ln[2][1])
    diag.append(ln[3][0])   
    num_x,num_t,num_o=0,0,0
    for x in diag:
     
      
       if x=='X':
        num_x+=1
       elif x=='O':
        num_o+=1
       elif x=='T':
        num_t+=1
    if num_x==4:
      return "X won"
      count+=1
      
    if num_o==4:
      return "O won"
      count+=1
      
    if num_x==3 and num_t==1:
      return "X won"
      count+=1
      
    if num_o==3 and num_t==1:
      return "O won"
      count+=1
   
      

    if count==0:
     for x in range(0,4):
      for y in range(0,4):
       if ln[x][y]==".":
        return "Game has not completed"
        count=+1
        break
     if count==0:
       return "Draw"
    
 
def data(l1,l2,l3,l4,x):
    l1=l1.strip()
    l2=l2.strip()
    l3=l3.strip()
    l4=l4.strip()
    lin1=list(l1)
    lin2=list(l2)
    lin3=list(l3)
    lin4=list(l4)
    ln=[lin1,lin2,lin3,lin4]
    value=main(ln)
    out=open("result.txt","a+")
    out.writelines("Case #%d: %s \n" %(x,value))     
    out.close()
   
for x in range(0,case):
    l1=text[4*x+1+x]
    l2=text[4*x+2+x]
    l3=text[4*x+3+x]
    l4=text[4*x+4+x]
    data(l1,l2,l3,l4,x+1)


