def caltime(taskd, taskb):
      time=0
      complete=0
      leng=len(taskd)
      o=1
      b=1
      while complete<leng:
            if taskd[0]=='O':
                  #check o
                  if int(taskb[0])==o:
                        complete+=1
                        del taskd[0]
                        del taskb[0]
                  elif int(taskb[0])>o:
                        o+=1
                  elif int(taskb[0])<o:
                        o-=1
                  #check b
                  try:
                        bi = taskd.index('B')
                        if int(taskb[bi])==b:
                              pass
                        elif int(taskb[bi])>b:
                              b+=1
                        elif int(taskb[bi])<b:
                              b-=1
                  except:
                        pass
            elif taskd[0]=='B':
                  #check b
                  if int(taskb[0])==b:
                        complete+=1
                        del taskd[0]
                        del taskb[0]
                  elif int(taskb[0])>b:
                        b+=1
                  elif int(taskb[0])<b:
                        b-=1
                  #check o
                  try:
                        oi = taskd.index('O')
                        if int(taskb[oi])==o:
                              pass
                        elif int(taskb[oi])>o:
                              o+=1
                        elif int(taskb[oi])<o:
                              o-=1
                  except:
                        pass
            time+=1
      #completed all task
      return time

#main
i=open('large.in', 'r')
o=open('large.out', 'w')
loop=int(i.readline())
time=[]
for n in range(loop):
        taskr=i.readline()
        tasks=taskr.split(' ')
        taskds=[]
        taskbs=[]
        nn=1
        while nn<len(tasks):
                taskd=tasks[nn]
                taskb=tasks[nn+1]
                taskds.append(taskd)
                taskbs.append(taskb)
                nn+=2
        t = caltime(taskds, taskbs)
        time.append(t)
#display
ans=''
for n in range(len(time)):
      ans+='Case #'+str(n+1)+': '+str(time[n])+'\n'
      o.write('Case #'+str(n+1)+': '+str(time[n])+'\n')
print ans
o.write(ans)
