"""
You know the shyness level of everyone in the audience, 
Can have additional friends to ensure that everyone in the crowd claps in the end. 
Each friend have any shyness value.
Minimum number of friends that you need to invite to guarantee a standing ovation?
p1 = 2 claps when 2xS=0 claps 

string "409" mean, four audience Si = 0, nine audience members with Si = 2 (and none with Si = 1 or any other value). 
Note that there will initially always be between 0 and 9 people with each shyness level.

4
4 11111
1 09
5 110011
0 1

	
Output: minimum number of friends you must invite. 
Case #1: 0
Case #2: 1
Case #3: 2
Case #4: 0

"""
t = int(input())
for i in range(t):
	#print(i + 1)
	s = str(input())
	s = s.split(" ")
	count = int(s[1][0])
	friend_needed = 0
	for idx,n in enumerate(s[1][1:]):
		#print(idx + 1, int(n))
		#print("Count", count)
		#print(friend_needed, idx + 1)
		if friend_needed < idx + 1:
			friend_needed += 1
		friend_needed += int(n)
		"""
		if int(n) != 0:
			friend_needed = friend_needed + (idx +1 - friend_needed)
			#friend_needed += int(n)
		print(idx+1, friend_needed)
		"""
	if friend_needed - sum(map(int, list(s[1]))) >= 0:
		print('Case #%d: ' % (i+1) + str(friend_needed - sum(map(int, list(s[1])))))
	else:
		print('Case #%d: ' % (i+1) + '0')
	#print(sum(map(int, list(s[1]))) - count)
		