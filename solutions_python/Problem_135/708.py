import sys
buf=[]
def scans():
    global buf
    while 1:
        while len(buf) <= 0:
            buf=input().replace('\n',' ').split(' ')
        o=buf.pop(0)
        if o!='':
            break
    return o
def scan():
    return int(scans())

sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')
for t in range(1,1+scan()):
	a = scan()-1
	a = [{scan() for i in range(4)} for i in range(4)][a]
	b = scan()-1
	b = [{scan() for i in range(4)} for i in range(4)][b]
	ins=a&b
	header = 'Case #%d: ' % t
	if len(ins)==1:
		print(header + str(ins.pop()))
	elif len(ins)>1:
		print(header + 'Bad magician!')
	else:
		print(header + 'Volunteer cheated!')