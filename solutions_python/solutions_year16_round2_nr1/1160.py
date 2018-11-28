# coding=utf-8#!/usr/bin/python
import sys

def hashing(str):
	m_hash = dict()
	for i in str:
		if m_hash.has_key(i)== False:
			m_hash[i] = 1
		else:
			m_hash[i] = m_hash[i] +1
	return m_hash

def removeNumber(m_dict, str):
	for i in str:
		m_dict[i] = m_dict[i] -1

def	getDigits(string):
	m_map = hashing(string)
	ret = []
	# do Zero
	if m_map.has_key('Z'):
		while(m_map['Z'] != 0):
			removeNumber(m_map, "ZERO")
			ret.append(0)

	# do Eight, G is special to him
	if m_map.has_key('G'):
		while( m_map['G'] != 0):
			removeNumber(m_map, "EIGHT")
			ret.append(8)

	# do FOUR, U is special to him
	if m_map.has_key('U'):
		while( m_map['U'] != 0):
			removeNumber(m_map, "FOUR")
			ret.append(4)

	# do TWO,  W is special to him
	if m_map.has_key('W'):
		while(m_map['W'] != 0):
			removeNumber(m_map, "W")
			ret.append(2)

	# do Six,
	if m_map.has_key('X'):
		while(m_map['X'] != 0):
			removeNumber(m_map, "SIX")
			ret.append(6)


	# do Seven, since all S belong to SIX already been removed
	if m_map.has_key('S'):
		while(m_map['S'] != 0):
			removeNumber(m_map, "SEVEN")
			ret.append(7)

	# do FIVE, since all V belong to SEVEN already been removed
	if m_map.has_key('V'):
		while(m_map['V'] != 0):
			removeNumber(m_map, "FIVE")
			ret.append(5)

	# do THREE, since all V belong to SEVEN already been removed
	if m_map.has_key('R'):
		while(m_map['R'] != 0):
			removeNumber(m_map, "THREE")
			ret.append(3)

	# final with NINE, I is in FIVE, SIX, AND EIGHT
	if m_map.has_key('I'):
		while(m_map['I'] != 0):
			removeNumber(m_map, "NINE")
			ret.append(9)

	# final with ONE, N is in SEVEN, NINE
	if m_map.has_key('N'):
		while(m_map['N'] != 0):
			removeNumber(m_map, "ONE")
			ret.append(1)

	ret = sorted(ret)
	out = "".join(str(ele) for ele in ret)
	return out


print getDigits("ETHER")


file = open(sys.argv[1], 'r')
writeFile = open(str(sys.argv[2]), 'w')
T = int(file.readline())
for i in range(T):
	n = file.readline()
	out = getDigits(n)
	writeFile.write("Case #%i: %s\n" % (i + 1, out))

file.close()
writeFile.close()


