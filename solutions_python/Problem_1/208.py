#!/usr/bin/python

import sys

def handle_case(case_no, engiens, words):
	saw ={}
	answer = 0
	for w in words:
		if w not in saw.keys():
			if len(saw.keys()) == (len(engiens)-1):
				answer+=1
				saw = {}
			saw[w] = 1
	print "Case #%d: %s" % (case_no, answer)

def main():
        filename = sys.argv[1]
	fsock = open(filename, "r")
	size = int(fsock.readline())
	for case in range(1,size+1):
		engiens_no = int(fsock.readline())
		engiens= []
		for e in range(1,engiens_no+1):
			engiens.append(fsock.readline().rstrip("\n"))

		words_no = int(fsock.readline())
		words = []
		for w in range(1,words_no+1):
			words.append(fsock.readline().rstrip("\n"))
			
		handle_case(case, engiens, words)
	fsock.close()


if __name__ == "__main__":
    main()

