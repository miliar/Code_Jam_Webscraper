#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(k,total,inv_list):
	ans=0
	# 長さlのlist
	#    反転箇所のindexはinv_listに格納してある

	#algo
		# 左から順にみていって,最初に見つけた反転箇所を左端とする長さkの区間を反転
		# .. というのをidx:l-k までやって反転数を0にできなければimpossibleを返す
	# 反転していたら(-なら) -1, + なら1
	state = [1]*total
	for e in inv_list:
		state[e] = -1

	for i in range(total-k+1):
		if state[i]==-1:
			ans+=1
			for j in range(k):
				state[i+j] *= -1
	if -1 in state:
		return "IMPOSSIBLE"
	else:
		return str(ans)

if __name__ == "__main__":
	#print solve(3,8,[0,1,2,4,7])
	t = int(raw_input())  # read a line with a single integer
	for i in xrange(1, t + 1):
		tmp_str, raw_k = raw_input().split(" ")
		k = int(raw_k)
		l = len(tmp_str)
		inv_list = [idx for idx,ch in enumerate(tmp_str) if ch=="-"]
		print "Case #{}: {}".format(i, solve(k,l,inv_list))
