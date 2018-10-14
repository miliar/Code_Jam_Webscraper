#coding:utf-8
import sys,time
from collections import defaultdict
def showlist(lst):
	for line in lst:
		print line

def foo(posword,wordls,lspos,i):
#	print lst[i]
	cost = 0
	same = []
	dicta = defaultdict(int)
	dictb = defaultdict(list)
	for word in wordls:
		prevs = 0
		same = []
		while True:
			s = word[prevs:].find(lst[i][lspos])
			if s == -1:
				break
			same.append(prevs+s) #s番目に見つかるとsが保存、そのあとs+1から再開、見つかればr+s+1番目を保存、r+s+1+1番目から再開
			prevs += s+1
		if word == posword:
			if len(same) == 0:
				cost = 1
		tsame = tuple(same)
		dicta[tsame] += 1
		dictb[tsame].append(word) #その内容をもつ文字の数と文字を保存
		if word == posword: posworddata = tsame
	newgroup = dictb[posworddata]
#	print posword,lspos,cost,newgroup
	return cost,newgroup



#fin = open("binput.txt")
fin = open("B-small-attempt1.in")
fout = open("boutput.txt","w")
cases = int(fin.readline())
for case in xrange(1,cases+1):
	ans = ("")
	N,M = map(int, fin.readline().split()) #多数の整数を読み込む
	words = [fin.readline().rstrip() for i in xrange(N)] #M行にわたるテキストを読み込む
	lst = [fin.readline().rstrip() for i in xrange(M)] #M行にわたるテキストを読み込む	
	group = defaultdict(list)
	for word in words:
		group[len(word)].append(word)


	ans = []
	for i in xrange(len(lst)):
		maxword = ""
		maxcost = -1
		for word in words:
#			print "search word",word
			lspos = cost = 0
			tmpgroup = group[len(word)]
			while True: #ある文字にかかるコストを評価
#				print "cost eval"
				if len(tmpgroup) == 1:
					break
				check = False
				while True: #検索対象文字の指定
					for w in tmpgroup: #対象グループの文字列に
						#print lspos
						if lst[i][lspos] in w:
							check = True
							break
					if check: break
					else: lspos += 1
				newcost,newgroup = foo(word,tmpgroup,lspos,i)
				cost += newcost
				tmpgroup = newgroup
				lspos += 1
			if maxcost < cost:
				maxcost = cost
				maxword = tmpgroup[0]
#			print "search finish",word,cost
		ans.append(maxword)
	
	ans = " ".join(ans)
	result = "Case #"+str(case)+": "+ans
	print result
	fout.write(result+"\n")

fin.close()
fin.close()


