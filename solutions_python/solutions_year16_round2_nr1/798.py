INPUT_FILE = 'A-large.in'
OUTPUT_FILE = 'A-large_out.txt'
def fixLists(lstAlpha, lstCountDig, s, ch, dig):
	lstCountDig[dig] = lstAlpha[ord(ch) - ord('A')]
	for c in s:
		lstAlpha[ord(c) - ord('A')] -= lstCountDig[dig]
	return (lstAlpha, lstCountDig)
def solve(f_in):
	S = f.readline().strip()
	phoneNumber = ''
	lstAlpha = [0] * (ord('Z') - ord('A') + 1)
	lstCountDig = [0] * 10
	for ch in S:
		lstAlpha[ord(ch) - ord('A')] += 1
	lstAlpha, lstCountDig = fixLists(lstAlpha, lstCountDig, 'ZERO', 'Z', 0)
	lstAlpha, lstCountDig = fixLists(lstAlpha, lstCountDig, 'TWO', 'W', 2)
	lstAlpha, lstCountDig = fixLists(lstAlpha, lstCountDig, 'SIX', 'X', 6)
	lstAlpha, lstCountDig = fixLists(lstAlpha, lstCountDig, 'EIGHT', 'G', 8)
	lstAlpha, lstCountDig = fixLists(lstAlpha, lstCountDig, 'THREE', 'H', 3)
	lstAlpha, lstCountDig = fixLists(lstAlpha, lstCountDig, 'FOUR', 'U', 4)
	lstAlpha, lstCountDig = fixLists(lstAlpha, lstCountDig, 'FIVE', 'F', 5)
	lstAlpha, lstCountDig = fixLists(lstAlpha, lstCountDig, 'SEVEN', 'S', 7)
	lstAlpha, lstCountDig = fixLists(lstAlpha, lstCountDig, 'NINE', 'I', 9)
	lstAlpha, lstCountDig = fixLists(lstAlpha, lstCountDig, 'ONE', 'O', 1)
	for i in range(10):
		phoneNumber += chr(ord('0') + i) * lstCountDig[i]
	return phoneNumber

with open(INPUT_FILE, 'r') as f:
	with open(OUTPUT_FILE, 'w') as f_out:
		T = int(f.readline())
		for i in range(T):
			f_out.write('Case #%d: %s\n' % (i + 1, solve(f)))
				