# Author: mfazal saintfiends@gmail.com
# License: MIT

def fill(gs, es, tdb):
	if len(gs) != len(es):
		return
	for i, char in enumerate(gs):
		tdb[char.lower()] = es[i].lower()
	return True

def translate(gs, tdict):
	return ''.join([tdict[t.lower()] for t in gs])

def get_unused(tdict):
	used = sorted([value for key, value in tdict.items() if value != ' ' and value != ''])
	start = ord('a')
	end = ord('z')
	unused = [chr(i) for i in range(start, end + 1) if chr(i) not in used]
	return unused 

def load_fixtures(fixture, tdict):
	for key, value in fixture.items():
		fill(key, value, tdict)

if __name__ == '__main__':

	fixture = {
		'y qee':'a zoo',
		'ejp mysljylc kd kxveddknmc re jsicpdrysi':'our language is impossible to understand',
		'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd':'there are twenty six factorial possibilities',
		'de kr kd eoya kw aej tysr re ujdr lkgc jv':'so it is okay if you want to just give up'
	}

	translation = dict({chr(k):'' for k in range(ord('a'), ord('z') + 1) })
	translation[' '] = ' '

	load_fixtures(fixture, translation)

	# stupid
	unused = get_unused(translation)
	if unused:
		for k, v in translation.items():
			if v == '':
				translation[k] = unused.pop()
	problem = 'A'			
	attempt = 1

	f = open("%s-small-attempt%d.in"%(problem, attempt), 'r')
	f.next() #skip top line
	with open("%s-small-attempt%d.out"%(problem, attempt), 'w') as out:
		for i, line in enumerate(f):
			out.write("Case #%d: %s\n" % (i+1, translate(line.strip(), translation)))

	f.close()
