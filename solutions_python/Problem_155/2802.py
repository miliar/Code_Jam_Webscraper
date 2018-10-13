import sys
import os.path

def optimalInvitation(line):
	if line[-1] == "\n":
		line = line[:-1]

	maxShyness, audience = line.split()

	invitationsRequired = 0
	peopleInAudience = 0
	
	for p in range(int(maxShyness) + 1):
		"""if missing invitation(s)"""
		if int(audience[p]) and p > (peopleInAudience+invitationsRequired):
			invitationsRequired += p - (peopleInAudience+invitationsRequired)

		peopleInAudience += int(audience[p])

	return invitationsRequired



def main(inputFile):
	f = open(inputFile)
	output = open(os.path.splitext(sys.argv[1])[0]+".out","w")
	nbrCase = f.readline()

	for i in range(int(nbrCase)):
		answer = optimalInvitation(f.readline())
		output.write("Case #%d: %d\n" % (i+1, answer))


if __name__ == '__main__':
	main(sys.argv[1])