# -*- coding: utf-8 -*-
if __name__=="__main__":
  global H,W
  fd=open("A-large.in","r")
  sLine=fd.readline().strip().split()
  L=int(sLine[0])
  D=int(sLine[1])
  N=int(sLine[2])
  #print "numis ",num
  fw=open("outputlarge","w")
  lang=[]
  for i in range(D):
    lang.append(fd.readline().strip())
  #count=1
  #for i in range(26):
    #for l in lang:
      #for c in l:
	#if "f"==c:
	  #count=count+1
  alp=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
  for caseI in range(N):
    inputLine=fd.readline().strip()
    #print inputLine
    word=[]
    #for i in range(len(inputLine)):
    i=0
    while i < len(inputLine):
      #print word
      c=inputLine[i]
      if c=="(":
	str1=""
	i=i+1
	c=inputLine[i]
	temp=[]
	while c!=")":
	  temp.append(c)
	  i=i+1
	  c=inputLine[i]
	word.append(temp)
      else:
	word.append([c])
      i=i+1

    matrix=[]
    for i in range(15):
      temp=[]
      for j in range(26):
	temp.append([])
      #temp=[0]*26
      matrix.append(temp)
    
    #print word
    for i in range(len(word)):
      #print matrix
      #print "started with :",word[i]
      wL=word[i]
      #print matrix
      for w in wL:
	#print "looking for:",w
	for iL in range(len(lang)):
	  l=lang[iL]
	  #print w,"  ",l[i]
	  if w==l[i]:
	    
	    if(i==0):
	      #print "in 0:",w,"  ",l[i]
	      #print matrix[i][alp.index(w+"")]
	      matrix[i][alp.index(w+"")].append(iL)
	      #print matrix[i][alp.index(w+"")]
	    else:
	      #print "in other:",w,"  ",l[i]
	      if(iL in matrix[i-1][alp.index(l[i-1])]):
		matrix[i][alp.index(w+"")].append(iL)
    sum=0
    for i in range(26):
      sum+=len(matrix[L-1][i])
    print sum
    fw.write("Case #"+str(caseI+1)+": ")
    fw.write(str(sum)+"\n")
    
    
    
    
    
	  
    