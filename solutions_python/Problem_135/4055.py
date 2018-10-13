#!/usr/bin/env python
#
def main():
	f = open('in.txt', 'r')
	tries = int(f.readline())
	tried = 0
	while tried < tries:
		possible = []
		row1 = []
		row2 = []

		answer1 = int(f.readline())
		temp = []
		temp.append(f.readline().split())
		temp.append(f.readline().split())
		temp.append(f.readline().split())
		temp.append(f.readline().split())
		row1 = temp[answer1 - 1]
		temp = []
		answer2 = int(f.readline())
		temp.append(f.readline().split())
		temp.append(f.readline().split())
		temp.append(f.readline().split())
		temp.append(f.readline().split())
		row2 = temp[answer2 - 1]
		for item in row2:
			if item in row1:
				possible.append(item)
		outcome(possible, tried+1)
		if tried == tries:
			break
		else:
			tried += 1

def outcome(possible, banaan):
	if len(possible) == 0:
		print 'Case #'+str(banaan)+': Volunteer cheated!' 
	elif len(possible) == 1:
		print 'Case #'+str(banaan)+': '+possible[0]
	elif len(possible) > 1:
		print 'Case #'+str(banaan)+': Bad magician!'


if __name__ == '__main__':
	main()