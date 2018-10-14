#!/usr/bin/env python

def alph(a, b):
	if ord(a) > ord(b):
		return (b, a)
	else:
		return (a, b)

def solveCase(combo, opp, invoke):
	el = []
	for inv in invoke:
		el.append(inv)
		if len(el) < 2:
			continue
		if alph(el[-1], el[-2]) in combo.keys():
			al = alph(el[-1], el[-2])
			el.pop();el.pop()
			el.append(combo[al])
		if opp.has_key(el[-1]):
			for opposer in opp[el[-1]]:
				if opposer in el:
					el = []
					break
	output = "["
	for elem in el:
		output += elem + ", "
	output = output[:-2] + "]"
	if el == []:
		output = "[]"
	return output

def main():
	T = input()

	for i in range(T):
		data = raw_input().split()
		C = int(data.pop(0))
		combo = {}
		for j in range(C):
			form = data.pop(0)
			combo[alph(form[0], form[1])] = form[2]
		D = int(data.pop(0))
		opp = {}
		for j in range(D):
			opposed = data.pop(0)
			if not opp.has_key(opposed[0]):
				opp[opposed[0]] = [opposed[1]]
			else:
				opp[opposed[0]].append(opposed[1])
			if not opp.has_key(opposed[1]):
				opp[opposed[1]] = [opposed[0]]
			else:
				opp[opposed[1]].append(opposed[0])
		N = data.pop(0)
		invoke = data.pop(0)
		print "Case #%d: %s" % (i+1, solveCase(combo, opp, invoke))

	return
main()

