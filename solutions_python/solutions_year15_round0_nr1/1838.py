# Google Code Jam 2015

def numstanding(peeps):
    return currently_standing(peeps, 0)

def homies_required(peeps):
	numpeeps = sum(peeps)
	if numstanding(peeps) == numpeeps:
		return 0
	possesize = 0
	while True:
		possesize += 1
		peeps[0] += 1
		totalrequired = sum(peeps)
		standing = numstanding(peeps)
		if standing == totalrequired:
			return possesize

def currently_standing(peeps, curr_shyness):
	"""
	[1, 1]

	inputs: [0, 1], 0, 0

	"""
	curr_shyness = 1
	standingnow = peeps[0]
	while curr_shyness != len(peeps) and standingnow >= curr_shyness:
		standingnow += peeps[curr_shyness]
		curr_shyness += 1
	return standingnow

def peepstolist(string):
	assert type(string) == str
	return [int(i) for i in string]


def test_numstanding():
    assert numstanding([1]) == 1
    assert numstanding([0, 9]) == 0
    assert numstanding([0, 1]) == 0
    assert numstanding([0, 0, 1]) == 0
    assert numstanding([1, 1, 1, 1]) == 4
    assert numstanding(peepstolist("110011")) == 2
    assert numstanding(peepstolist("210011")) == 3
    assert numstanding(peepstolist("00001")) == 0
    assert numstanding(peepstolist("2401")) == 7

def test_numhomies():
	assert homies_required(peepstolist("1111")) == 0
	assert homies_required(peepstolist("09")) == 1
	assert homies_required(peepstolist("110011")) == 2
	assert homies_required(peepstolist("1")) == 0
	assert homies_required(peepstolist("2401")) == 0

def genhomies(infname):
    f = open(infname, 'r')
    lines = f.readlines()[1:]
    answer = ""
    for i in range(len(lines)):
    	theline = lines[i]
    	theint = theline.strip().split(" ")[1]
    	answer += "Case #%d: %d\n" % (int(i) + 1, homies_required(peepstolist(theint)))
    return answer


def test_e2e(fname, correctfname):
	f = open(correctfname)
	myans = genhomies(fname)
	assert myans == "".join(f.readlines())

if __name__ == "__main__":
    test_numstanding()
    test_numhomies()
    test_e2e("testin.txt", "testout.txt.gold")
    infilename = "A-large.in"
    downloadsdirectory = "/Users/robertkarl/Downloads/"
    answer = genhomies(downloadsdirectory + infilename)
    outfile = open(downloadsdirectory + "ans.txt", 'w')
    outfile.write(answer)
    outfile.close()

