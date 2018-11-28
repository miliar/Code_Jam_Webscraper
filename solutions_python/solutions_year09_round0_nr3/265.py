import copy
import sys
statement="welcome to code jam"
def calculate(statement,text):
  store={}
  statement_size=len(statement)
  text_size=len(text)
  def count(statement_index,text_index,size):
    if not store.has_key((statement_index,text_index,size)):
      if size==0:
        return 1
      if statement_index==statement_size or text_index==text_size:
        return 0
      if statement[statement_index]==text[text_index]:
        store[(statement_index,text_index,size)]=count(statement_index+1,text_index+1,size-1)+count(statement_index,text_index+1,size)
        return store[(statement_index,text_index,size)]
      else:
        store[(statement_index,text_index+1,size)]=count(statement_index,text_index+1,size)
        return store[(statement_index,text_index+1,size)]
    else:
      return store[(statement_index,text_index,size)]
  return count(0,0,len(statement))

def get_lines(file_name=sys.argv[1]):
  fDes=open(file_name,'r')
  lines=[]
  for line in fDes.read().split('\n'):
    lines.append(line)
  lines=filter(lambda x:x,lines)
  return lines

lines=get_lines()
for i in range(int(lines[0])):
  answer=int(str(calculate(statement,lines[i+1]))[-4:])
  print "Case #"+str(i+1)+": "+'%(#)04d'%{'#':answer}
#statement_size=len(statement)
#temp0=[]
#temp1=[]
#for i in range(len(statement)+1):
#  temp0.append(0)
#  temp1.append(0)
#
#counter=0
#for i in range(len(text)):
#  temp1[0]=0
#  print temp0
#  for j in range(1,statement_size+1):
#    if text[i]==statement[j-1]:
#      temp1[j]=1+temp0[j-1]
#    else:
#      temp1[j]=max(temp0[j],temp1[j-1])
#    if temp1[j]==len(text):
#      counter+=1
#  temp0=copy.deepcopy(temp1)
#print temp1
#print counter
