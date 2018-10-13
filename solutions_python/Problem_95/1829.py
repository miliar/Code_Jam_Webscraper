
def main(line):
        
        #l='yneicwlbkuomxsev?pdrjgtxyz'
    n='abcdefghijklmnopqrstuvwxyz'#falso
    l='yhesocvxduiglbkrztnwjpfmaq'#verd
    resp=""
    for i in line:
        if i==' ':
            resp+=" "
        else:
            resp+=l[ord(i)-97]
            
    return resp


if __name__ == '__main__':
	import sys
        #print sys.stdin.readline()
	N = int(sys.stdin.readline())
	for i in xrange(N):
		res = main(sys.stdin.readline().strip())
		print "Case #%d: %s" % (i + 1, res)	
