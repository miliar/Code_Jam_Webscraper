#!/usr/bin/env python

import sys

def arrange_cards(n):

	cards = {1:1}
	pos = range(2, n+1)
	#print pos
	cur = 0
	
	for i in range(1,n):
	
		j = (cur + i)%len(pos)
		cards[pos[j]] = i+1
		pos.remove(pos[j])
		cur = j
		
		
	return cards
	
if __name__ == '__main__':

	inp = open(sys.argv[1])
	op = open(sys.argv[2], 'w')
	
	cases = int(inp.readline()[:-1])
	
	for i in range(1, cases+1):
		num_card = int(inp.readline()[:-1])
		cards = arrange_cards(num_card)
		ques = inp.readline()
		ques = ques.split()
		ans = []
		for j in ques[1:]:
			ans.append(str(cards[int(j)]))
		
		ans = ' '.join(ans)
		op.write('Case #%s: %s\n' % (i, ans))
		
	inp.close()
	op.close()
		
