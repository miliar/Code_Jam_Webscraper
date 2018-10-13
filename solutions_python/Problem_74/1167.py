import math



def solve ():
      input = raw_input().replace('\n','')
      c = int(input)
      for i in xrange(c):
            result = solve_1()
            print "Case #"+str(i+1)+': '+str(result)
      
def read():
      input = raw_input().replace('\n','')
      words = input.split()[1:]
      #print words
      list =[]
      for i in xrange(0,len(words),2):
            a= words[i]
            b= int(words[i+1])
            list.append((a,b))
      return list
            
def solve_1():
      list = read()
      olist = filter (lambda x: x[0]=='O', list)
      blist = filter(lambda x : x[0]=='B',list)
      resulto = path (olist) + [['push',0]]
      resultb= path(blist)+[['push',0]]
     # print resulto
     # print resultb
      total = 0
      o=0
      b=0
      new_list=[]
      for l in list:
            if l[0]=='O':
                  if o >=len(resulto):
                        new_list.append(resultb[b:])
                        break
                  else :
                        new_list.append(resulto[o])
                        o+=1
            if l[0]=='B':
                  if b >=len(resultb):
                        new_list.append(resulto[o:])
                        break
                  else :
                        new_list.append(resultb[b])
                        b+=1
                        
      total_reduce = 0
      current ='X'
      for k in xrange(len(new_list)) :
            if new_list[k][2] != current :
                 
                  if new_list[k][1]-total_reduce <1:
                        new_list[k][1]=1
                  else :
                        new_list[k][1]-=total_reduce
                  current = new_list[k][2]
                  total_reduce = new_list[k][1]
            else :
                  total_reduce+=new_list[k][1]
                  current = new_list[k][2]
     # print new_list
      
      total =0
      for i in new_list:
            total +=i[1]
      return total
                  
            
      
      
      
def path (list):
      result =[]
      current =1
      for l in list:
            if l[1]==current :
                  result.append(  ['push',1,l[0]])
            else :
                  result.append( ['move&push',abs(current-l[1])+1 ,l[0]])
                  current = l[1]
      
      return result

solve()
