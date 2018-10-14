import sys
#f=open('input');
f=sys.stdin;
g=sys.stdout;

def fSort(x):
    y=[];
    for i in range(len(x)):y.append([x[i],-1*i])
    y.sort(None,None,True);i=[];
    for [t1,t2] in y: i.append(t2*-1)
    return i
    
x=f.readline();N=int(x.strip());
for iN in range(1,N+1):
  x=f.readline().strip(); tatime=float(x)/60;
  x=f.readline().split();mA=int(x[0]);mB=int(x[1]);
  Event=[];Time=[];
  for i in range(mA+mB):
    x=f.readline().split();
    t=x[0]; t1=t.split(':'); time1=float(t1[0])+float(t1[1])/60;
    t=x[1]; t1=t.split(':'); time2=float(t1[0])+float(t1[1])/60;
    if i<mA:tEvent1='A';tEvent2='B';
    else:tEvent1='B';tEvent2='A';
    Event.append(tEvent1+'-');Time.append(time1);
    Event.append(tEvent2+'+');Time.append(time2);
    
  #sort
  I=fSort(Time);I.reverse();tE=[];tT=[];
  for i in I:
    tE.append(Event[i]);
    tT.append(Time[i]);
  Event=tE; Time=tT;
  
  #stimulate
  TrainA=[]; TrainB=[];
  nStartA=0; nStartB=0;
  for i in range(len(Time)):
    event=Event[i];time=Time[i];
    if event=='A-' or event=='B-':
      if event[0]=='A':Train=TrainA;
      else: Train=TrainB;
      #decide whether have ready train
      isFind=False;nStart=0;
      for i in range(len(Train)):
        if Train[i]+tatime<=time:isFind=True;break;
      if isFind: del Train[i];
      else:nStart+=1;
      if event[0]=='A':nStartA+=nStart;
      else: nStartB+=nStart;
    elif event=='A+'or event=='B+':
      if event[0]=='A':TrainA.append(time)
      else:TrainB.append(time)
        
  #output
  g.write('Case #%d: %d %d\n'%(iN,nStartA,nStartB));
f.close();g.close();
        
        
    
    
  
 
  
    
  
    
