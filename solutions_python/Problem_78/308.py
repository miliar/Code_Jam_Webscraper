import os.path
import sys

debug = 0

which = sys.argv[1]
dir = os.path.dirname(__file__)
fname = os.path.join(dir, which)
assert os.path.exists(fname+".in")


def gcd(num1, num2):
    if num1 > num2:
        for i in range(1,num2+1):
            if num2 % i == 0:
                if num1 % i == 0:
                    result = i
        return result
    elif num2 > num1:
        for i in range(1,num1+1):
            if num1 % i == 0:
                if num2 % i == 0:
                    result = i
        return result
    else:
        result = num1*num2/num1
        return result


def test(maxToday, pctToday, pctTotal):
	if pctToday == pctTotal:
		if debug: print pctToday, '==', pctTotal
		return 'Possible'
	if pctTotal in (0, 100) and pctToday != pctTotal:
		if debug: print pctToday, '!=', pctTotal
		return 'Broken'
	xgcd = gcd(pctToday, 100)
	minToday = 100/xgcd
	if debug:
		ygcd = gcd(pctTotal, 100)
		ya = pctTotal/ygcd
		yb = 100/ygcd
		print '%s/100 => %s/%s (%s) => %s (max: %s) (%s/%s : %s)' % (pctToday, pctToday/xgcd, minToday, xgcd, minToday, maxToday, ya, yb, ygcd)
	return 'Possible' if maxToday >= minToday else 'Broken'


def main():
	with open(fname + '.in') as f_in:
		lines = f_in.readlines()
		assert lines
	with open(fname + '.out', 'w') as f_out:
		numTests = int(lines.pop(0))
		testCase = 0
		while testCase < numTests:
			testCase += 1
			assert lines


			# Test-specific
			line = lines.pop(0).strip()
			if debug: print line
			n, pd, pg = [int(x) for x in line.split(' ')]

			result = test(n, pd, pg)


			outline = 'Case #%s: %s' % (testCase, result)
			print outline
			f_out.write(outline + '\n')

		assert not lines or lines == ['']

main()
