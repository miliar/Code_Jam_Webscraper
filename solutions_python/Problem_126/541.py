import itertools
combis = itertools.combinations
not_vowel = lambda s : 'a' != s or 'e' != s != 'i' != s or 'o' != s or 'u' != s
has_vowel = lambda s : 'a' in s or 'e' in s or 'i' in s or 'o' in s or 'u' in s
not_has_vowel = lambda s : not('a' in s or 'e' in s or 'i' in s or 'o' in s or 'u' in s)

n_cases = int(raw_input().strip())

def substrs2(na,nn):
	min_strs = set()
	for i in range(0,len(na)-nn+1):
		ss = na[i:nn+i]
		if not_has_vowel(ss):
			min_strs.add(ss)

	min_strs_map = {}
	def has_min_str(s):
		if min_strs_map.has_key(s):
			return min_strs_map[s]

		for each in min_strs:
			if each in s:
				min_strs_map[s] = True
				return True

		min_strs_map[s] = False
		return False

	for k in range(nn,len(na)+1):
		for i in range(0,len(na)-k+1):
			s = na[i:k+i]
			if has_min_str(s):
				yield s

for i_case in range(1,n_cases+1):
	name, name_n = raw_input().strip().split(' ')
	name_n = int(name_n)
	combs = list(substrs2(name,name_n))
	print 'Case #%d: %s' % ( i_case, len(combs) )