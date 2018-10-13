#!/usr/bin/python2.4
def main():
	for case in range(input()):
		engines = []
		tested = []
		switch = 0
		for srcheng in range(input()):
			engines.append(raw_input())
		for query in range(input()):
			line = raw_input()
			if line not in tested:
				tested.append(line)
			if len(engines) == len(tested):
				tested = [line]
				switch += 1
		print 'Case #%s: %s' % (case + 1, switch)
main()

