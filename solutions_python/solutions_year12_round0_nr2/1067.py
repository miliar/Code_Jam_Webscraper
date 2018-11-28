

def calc(s):
 res=(0,0,0)
 if (s%3)==0:
    res=(s/3,s/3,s/3)
 elif (((s+1)%3)==0 ) or max(res)>10 or min(res)<0:
    res= ( (s+1)/3 , ((s+1)/3)-1 , ((s+1)/3))
 elif (((s+2)%3)==0)or max(res)>10 or min(res)<0:
     res= ( (s+2)/3 ,((s+2)/3)-1,((s+2)/3)-1)
 return res    

def bonus_calc(s):
  res=(0,0,0)
  if ((s+2)%3)==0 :
     res = ( (s+2)/3 ,((s+2)/3),((s+2)/3)-2)
     
  elif ((s+3)%3)==0 or max(res)>10 or min(res)<0 :
     res = ( (s+3)/3 ,((s+3)/3)-1,((s+3)/3)-2)
     
  elif ((s+4)%3)==0 or max(res)>10 or min(res)<0:
     res= ( (s+4)/3 ,((s+4)/3)-2,((s+4)/3)-2)
     
  if max(res)>10 or min(res)<0:
     res=(0,0,0)
        
  return res
     
def judge(num,bonus,p):
  j=dict()
  resnum=0
  for i in range(len(num)):
	s=calc(num[i])
	j[i]=s

  for i in range(len(num)):
     if not (max(j[i])>=p):
	s=bonus_calc(int(num[i]))
	if (not (s==(0,0,0))) and (bonus>0) and (max(s)>=p):
		bonus=bonus-1
		j[i]=s
  		
  for i in range(len(num)):
	s=bonus_calc(int(num[i]))
	if (not (s==(0,0,0))) and (bonus>0):
		bonus=bonus-1
		j[i]=s		
  		
  for i in j.values():
   if max(i)>=p:
       resnum=resnum+1
  return resnum

def main():
  inputfile=open("input.txt","r+")
  totnum=int(inputfile.readline())
  for i in range(1,totnum+1):
    raid_arr=inputfile.readline().strip().split()
    bonus=int(raid_arr[1])
    p=int(raid_arr[2])
    num=raid_arr[3:]
          
    for j in range(len(num)):
      num[j]=int(num[j])
     
    print "Case #"+str(i)+": "+str(judge(num,bonus,p))

if __name__=="__main__" :
 main()
