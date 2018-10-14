# Graham Erickson

def doMagic(r1,r2,rows1,rows2):
  ch1=set(rows1[r1-1])
  ch2=set(rows2[r2-1])

  result = list(ch1.intersection(ch2))
  
  if len(result)==1:
    return result[0]
  elif len(result)>1:
    return "Bad magician!"
  elif len(result)<1:
    return "Volunteer cheated!"


def main():
  f=open("A-small-attempt0.in",'r')
  lines=f.readlines()
  lines=lines[1:]
  i=0
  casen=1
  while i <len(lines):
    row1=int(lines[i].strip("\n"))
    rows1=[]
    rows1.append(map(lambda x:int(x),(lines[i+1].strip("\n")).split()))
    rows1.append(map(lambda x:int(x),(lines[i+2].strip("\n")).split()))
    rows1.append(map(lambda x:int(x),(lines[i+3].strip("\n")).split()))
    rows1.append(map(lambda x:int(x),(lines[i+4].strip("\n")).split()))
   
    row2=int(lines[i+5].strip("\n"))
    rows2=[]
    rows2.append(map(lambda x:int(x),(lines[i+6].strip("\n")).split()))
    rows2.append(map(lambda x:int(x),(lines[i+7].strip("\n")).split()))
    rows2.append(map(lambda x:int(x),(lines[i+8].strip("\n")).split()))
    rows2.append(map(lambda x:int(x),(lines[i+9].strip("\n")).split()))
   
    print "Case #" + str(casen)+": "+str(doMagic(row1,row2,rows1,rows2)) 
    casen+=1
    i=i+10

if __name__=='__main__':
  main()





