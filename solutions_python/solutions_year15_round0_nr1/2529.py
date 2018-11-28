import os

try:
	results = []
	path = raw_input("Enter path:")
	file = open(path, "r+")
	lines = file.read().splitlines()
	lines.pop(0)
	
	for line in lines:
		
		values = line.split(" ")
		s_max = int(values[0])
		s_max_string = values[1]
		friends = 0
		stand_up = 0
		for index, chr in enumerate(s_max_string):
			while True:
				if stand_up >= index :
					stand_up += int(chr)
					break
				else :
					friends += 1
					stand_up += 1
					continue
		results.append(friends)
	answer_path = os.path.split(path)[0] + "\\answer.txt"
	answer=open(answer_path, 'w+')
	
	for index,value in enumerate(results):
		case_num = (index + 1)
		case_num = str(case_num)
		string = "Case #"+ case_num + ": " + str(value) +"\n"
		answer.write(string)
	
	answer.close()
	file.close()
except Exception, e:
	print e
finally:
	file.close