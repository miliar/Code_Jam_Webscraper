import re

if __name__=="__main__":
     f = open("output.txt","w")
     s=[]
     l, d, n = [int(x) for x in raw_input().split(" ")]
     for i in range(0, d):
	     s.append(raw_input())
     for i in range(1,n+1):
	     count = 0
	     rege = re.compile(raw_input().replace('(','[').replace(')',']'))
	     for j in range(0,d):
		     if re.findall(rege, s[j], re.M)!=[]:
			     count=count+1
	     f.write("Case #%i: %s\n" % (i, count))
     f.close()
			     






	

 
     
