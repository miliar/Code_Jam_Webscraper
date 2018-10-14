"""
Chad Reynolds 4/11/14

Google Code Jam 2014
Qualifying Round
Problem A

Elapsed time from beginning to submission:  
"""
import sys

if __name__ == "__main__":

	input = sys.argv[1]
	output = sys.argv[2]

	output = open(output, "w")
	file = open(input, "r")
	num_inputs = int(file.readline())

	## problem ##
	for i in range(num_inputs):

		# process input
		ans1 = int(file.readline())
		row1 = ans1 - 1
		cards1 = []
		for j in range(4):
			cards1.append(file.readline().rstrip())	
		ans2 = int(file.readline())
		row2 = ans2 - 1
		cards2 = []
		for j in range(4):
			cards2.append(file.readline().rstrip())	
		
		# find possibles
		poss_cards1 = cards1[row1].split(" ")
		poss_cards2 = cards2[row2].split(" ")
		poss_ans = []
		
		for j in range(4):
			if poss_cards2[j] in poss_cards1:
				poss_ans.append(poss_cards2[j])	

		answer = ""
		if len(poss_ans) == 0:
			answer = "Volunteer cheated!"
		elif len(poss_ans) == 1:
			answer = poss_ans[0]
		else:
			answer = "Bad magician!"

		print(str(i) + answer)
		output.write("Case #{0}: {1}\n".format(i+1, answer))
		

	output.close()	
	file.close()
