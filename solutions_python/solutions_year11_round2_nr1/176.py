# -*- coding: utf-8 -*-
def ans(line):
  num = int(line.strip())
  st =[];
  dic ={};
  pl =0;
  winP=[]
  lossP=[]
  plaP = []
  for i in range(num):
    line = sys.stdin.readline()
    ind=0;
    temp =[]
    op =[]
    w=0;
    l = 0;
    p =0;
    for c in line:
      if c=='0':
	op.append(ind);
	temp.append(0)
	l+=1
	p+=1
      elif c=='1':
	op.append(ind);
	temp.append(1);
	w+=1
	p+=1
      else:
	temp.append('-')
      ind+=1
    dic[pl]=op;
    winP.append(w)
    plaP.append(p)
    lossP.append(l)
    st.append(temp)
    pl+=1;
  #print 'st'
  #print st;
  #print 'dic'
  #print dic
  #print 'winP'
  #print winP
  #print 'losP'
  #print lossP
  #print 'plaP'
  #print plaP
  
  wp=[]
  for i in range(num):
    wp.append(winP[i]/float(plaP[i]))
  
  owp = []
  for i in range(num):
    temp =0.0;
    n = 0.0;
    for j in dic[i]:
      temp += (winP[j]-st[j][i])/float(plaP[j]-1)
      n+=1.0
    owp.append(temp/n);
  oowp = []
  for i in range(num):
    temp =0.0;
    n = 0.0;
    for j in dic[i]:
      temp += owp[j];
      n+=1.0
    oowp.append(temp/n);
  #print "\n\nwp"
  #print wp
  #print "\nowp"
  #print owp
  #print "\noowp"
  #print oowp
  #print "\n\n\n"
  
  for i in range(num):
    print 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]
  
  
  

if __name__=="__main__":
  import sys
  line=sys.stdin.readline()
  M=int(line.strip())
  for caseI in range(1,M+1):
    print "Case #"+str(caseI)+": "
    ans(sys.stdin.readline());
    #line=sys.stdin.readline()
    