
# Problem

# It's opening night at the opera, and your friend is the prima donna (the lead female singer). 
# You will not be in the audience, but you want to make sure she receives a standing ovation -- with every audience member standing up and clapping their hands for her.

# Initially, the entire audience is seated. Everyone in the audience has a shyness level. 
# An audience member with shyness level Si will wait until at least S other audience members have already stood up to clap, and if so, 
# she will immediately stand up and clap. If Si = 0, then the audience member will always stand up and clap immediately, regardless of what anyone else does. 
# For example, an audience member with Si = 2 will be seated at the beginning, but will stand up to clap later after she sees at least two other people standing 
# and clapping.

# You know the shyness level of everyone in the audience, and you are prepared to invite additional friends of the prima donna to be in the audience to 
# ensure that everyone in the crowd stands up and claps in the end. Each of these friends may have any shyness value that you wish, not necessarily the same. 
# What is the minimum number of friends that you need to invite to guarantee a standing ovation?

f = open('input.txt', 'r')


def function(case):
	cumulative = [0] + case[:]
	for i in xrange(1, len(case) + 1):
		cumulative[i] += cumulative[i-1]
	maxdiff = 0
	# print(cumulative)
	for x in xrange(1, len(cumulative)):
		# if cumulative[x] < x:
			# print(cumulative[x], cumulative[x] - 1 , x)
			if x - cumulative[x-1]  > maxdiff:
				maxdiff = x - cumulative[x-1]
	return str(maxdiff - 1)


T = int(f.readline())
for i in xrange(T):

	spl = f.readline().split(' ')
	Smax = int(spl[0])
	cases = []
	for j in range(Smax + 1):
		cases.append(int(spl[1][j]))
	print("Case #" + str(i+1) + ": " + function(cases))
