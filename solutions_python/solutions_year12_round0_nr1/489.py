mapping = list('yhesocvxduiglbkrztnwjpfmaq')

def translate(letter):
	if ord(letter) < ord('a') or ord(letter) > ord('z'):
		return letter
	return mapping[ord(letter) - ord('a')]

cases = int(raw_input())
for case in xrange(1, cases + 1):
	message = map(translate, list(raw_input()))
	print 'Case #%d: %s' % (case, ''.join(message))