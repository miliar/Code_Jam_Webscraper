import sys

with open(sys.argv[1], "rb") as f:
	rf = open("result.txt", "wb")
	T = int(f.readline())
	if 1<=T<=100:
		for i in range(0, T):
			S = f.readline().split(' ')
			Smax = int(S[0])
			if 0<=Smax<=1000:
				result = 'Case #'+str(i+1)+': '
				friends = 0
				audience = 0
				stands = 0
				for k in range(0, Smax+1):
					Sk = int(S[1][k])
					if 1<=Sk:
						if stands<k:
							need_friends = k - stands
							friends += need_friends
							stands += need_friends
					stands += Sk
				result += str(friends)
				rf.write(result+'\n')
	rf.close()