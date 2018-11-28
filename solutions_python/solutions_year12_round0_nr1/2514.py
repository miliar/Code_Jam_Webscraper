def build_dict():
	dic = {}

	input_data = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv"
	output_data = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup"
	for i in zip(input_data, output_data):
		dic[i[0]] = i[1]
	dic['q'] = 'z'
	dic['z'] = 'q'
	dic[' '] = ' '

	return dic

num_inputs = int(raw_input())
inputs = [raw_input() for x in range(num_inputs)]
dic = build_dict()

for item,text in enumerate(inputs):
	saida = ""
	for letra in text:
		saida += dic[letra]
	print "Case #%i: %s" % (item+1, saida)
