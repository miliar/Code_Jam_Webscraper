#!python
import sys
import string
import operator

def keep_typing(typed, total, probs):
	ks_correct = total - typed + 1
	ks_wrong = 2*total - typed + 2 	#= (total - typed + 1) + (total + 1)
	prob_correct = reduce(operator.mul, probs)
	prob_wrong = 1.0 - prob_correct
	exp_ks = ks_correct * prob_correct + ks_wrong * prob_wrong
	return exp_ks

def delete_some(typed, total, probs, del_chars):
	ks_correct = 2*del_chars + total - typed + 1
	ks_wrong = 2*del_chars + 2*total - typed + 2
	if del_chars < typed:
		prob_correct = reduce(operator.mul, probs[:typed - del_chars])
	else:
		return del_chars + total + 1
	prob_wrong = 1.0 - prob_correct
	exp_ks = ks_correct * prob_correct + ks_wrong * prob_wrong
	#print "Del=%d, Exp=%f, corr=%f, wrong=%f" % (del_chars, exp_ks, prob_correct, prob_wrong)
	return exp_ks

def optimal_keystrokes(typed_n_total, probs):
	typed_n_total = typed_n_total.split()
	typed = int(typed_n_total[0])
	total = int(typed_n_total[1])
	probs = map(float, probs.split())
	
	score_kt = keep_typing(typed, total, probs)
	score_del = 2*total + 2
	del_chars=1
	while del_chars <= typed:
		score_del = min(score_del, delete_some(typed, total, probs, del_chars))
		del_chars += 1
	score_enter = total + 2
	
	return min(score_kt, score_del, score_enter)

def main(*args):
	if len(args) < 2:
		print "Usage:\n", args[0], " <file>\n"
		return
	file = open(args[1])
	text = file.read().split('\n')
	arr = list(text)
	#print arr
	
	cases = int(arr[0])	
	i = 1
	while i <= cases:
		print "Case #%s: %.6f" % (i, optimal_keystrokes(arr[2*i-1], arr[2*i]))
		i += 1

if __name__ == '__main__':
	#print recycle(101)
    sys.exit(main(*sys.argv))