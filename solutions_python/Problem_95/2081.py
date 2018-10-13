def unscramble(fname):
	dictionary = {"a":"y", "b":"h", "c":"e", "d":"s", "e":"o","f":"c", "g":"v", "h":"x", "i":"d", "j":"u", "k":"i", "l":"g", "m":"l", "n":"b", "o":"k", "p":"r", "q":"z", "r":"t", "s":"n", "t":"w", "u":"j", "v":"p", "w":"f", "x":"m", "y":"a", "z":"q"}
	lines = [line.strip() for line in open(fname)]
	if( int(lines[0]) != int(len(lines)-1)  ):
		print("error: wrong text length")
	else:
		lines = lines[1:]
		outText=""
		for lineIndex in range(len(lines)):
			outLine = ""
			words = lines[lineIndex].split()
			for wordIndex in range(len(words)):
				word = words[wordIndex]
				outWord=""
				for letterIndex in range(len(word)):
					outWord=outWord+dictionary[ word[letterIndex] ]
				outLine = outLine+" "+outWord
			outLine = outLine.strip()
			outText = outText +"Case #"+str(lineIndex+1)+": "+outLine+"\n"
		outFile = open("out.txt", 'w')
		outFile.write(outText)
		outFile.close()
