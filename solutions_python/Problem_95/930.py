in_  = 'abcdefghijklmnopqrstuvwxyz'
out_ = 'yhesocvxduiglbkrztnwjpfmaq'

T = int(raw_input())
for t in range(1, T+1):
    line = raw_input()
    print "Case #{0}: {1}".format(t, ''.join([out_[ord(ch)-ord('a')] if ch <> ' ' else ' ' for ch in line]))