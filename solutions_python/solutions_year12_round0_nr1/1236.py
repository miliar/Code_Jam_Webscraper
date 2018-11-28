




class Translate(object):
	input = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
			"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
			"de kr kd eoya kw aej tysr re ujdr lkgc jv"]
	output = ["our language is impossible to understand",
			"there are twenty six factorial possibilities",
			"so it is okay if you want to just give up"]
	dictionary = {'q':'z', 'z':'q'}

	@staticmethod
	def build_hashing():
		for pidx, phrase in enumerate(Translate.input):
			for idx in range(len(phrase)):
				key = phrase[idx]
				val = Translate.output[pidx][idx]
				if key not in Translate.dictionary:
					Translate.dictionary[key] = val

	@staticmethod
	def show_mapping():
		for key in sorted(Translate.dictionary.keys()):
			print key, " ", Translate.dictionary[key]

	@staticmethod
	def solve_missing():
		print sorted(Translate.dictionary.values())

	@staticmethod
	def to_original(case):
		ans = []
		for char in case:
			ans.append(Translate.dictionary[char])
		return ans


if __name__ == '__main__':
	Translate.build_hashing()
	totalcase = int(raw_input())
	casei = 1
	while totalcase > 0:
		case = raw_input()
		ans = Translate.to_original(case)
		print "Case #%d: %s"%(casei, ''.join(ans))
		totalcase -= 1
		casei += 1

