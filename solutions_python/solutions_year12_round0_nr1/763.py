#! /usr/bin/env python3


mapper = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}


def decrypt(msg):
	new = []
	for i in msg:
		new.append(mapper[i])
	return "".join(new)

if __name__ == '__main__':
	t = int(input())
	for i in range(t):
		m = input()
		print("Case #" + str(i+1) + ": " + decrypt(m))


