#coding:utf-8
import sys
def showlist(lst):
	for line in lst:
		print line

#fin = open("ainput.txt")
fin = open("A-large.in")
fout = open("aoutput.txt","w")
cases = int(fin.readline())
for case in xrange(1,cases+1):
	ans = ("")
	N = int(fin.readline().rstrip()) #１つの整数を読み込む
	text = [fin.readline().rstrip() for i in xrange(N)] #M行にわたるテキストを読み込む
	wp,owp,oowp = [],[],[]
	
	#print showlist(text)
	for i in xrange(len(text)):
		tmp = text[i].replace(".","")
		wp.append(float(tmp.count("1"))/len(tmp))
	#print wp
	for i in xrange(len(text)):
		itmp = []
		for j in xrange(len(text)): #iチームに対するj
			if i==j or text[j][i] == ".":
				#print "conti",i,j,text[j]
				continue
			tmp = list(text[j])
			#print tmp
			del tmp[i]
			#print tmp
			tmp = "".join(tmp)
			#print i,j,tmp
			itmp.append(tmp)
		#print itmp
		owptmp = []
		for j in xrange(len(itmp)):
			tmp = itmp[j].replace(".","")
			owptmp.append(float(tmp.count("1"))/len(tmp))
		#print owptmp
		owp.append(sum(owptmp)/len(owptmp))
	#print owp
	tmp = 0
	for i in xrange(N):
		cnt = 0
		tmp = 0
		for j in xrange(N):
			if text[j][i] == ".":
				#print "cont",i,j
				continue
			tmp += owp[j]
			cnt += 1
		#print tmp,cnt,tmp/cnt
		oowp.append(tmp/cnt)
	#print oowp
	
	ans = "\n"
	for i in xrange(N):
		ans += str( 0.25*wp[i] + 0.5*owp[i] + 0.25* oowp[i] )+"\n"
	ans = ans.rstrip("\n")
	result = "Case #"+str(case)+": "+ans
	print result
	fout.write(result+"\n")

fin.close()
fin.close()



