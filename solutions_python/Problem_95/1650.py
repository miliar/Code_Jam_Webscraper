
import sys;
import re;

filename = sys.argv[1]
lines = open(filename, 'r')

s = 0
def myreplace(i,a, b):
	f=''
	if i == a:
		f=b
	return f
	
for line in lines:
	new_line = ''
	for i in line:
		new_line += myreplace(i,'y','a')
		new_line += myreplace(i,'n','b')
		new_line += myreplace(i,'f','c')
		new_line += myreplace(i,'i','d')
		new_line += myreplace(i,'c','e')
		new_line += myreplace(i,'w','f')
		new_line += myreplace(i,'l','g')
		new_line += myreplace(i,'b','h')
		new_line += myreplace(i,'k','i')
		new_line += myreplace(i,'u','j')
		new_line += myreplace(i,'o','k')
		new_line += myreplace(i,'m','l')
		new_line += myreplace(i,'x','m')
		new_line += myreplace(i,'s','n')
		new_line += myreplace(i,'e','o')
		new_line += myreplace(i,'v','p')
		new_line += myreplace(i,'z','q')
		new_line += myreplace(i,'p','r')
		new_line += myreplace(i,'d','s')
		new_line += myreplace(i,'r','t')
		new_line += myreplace(i,'j','u')
		new_line += myreplace(i,'g','v')
		new_line += myreplace(i,'t','w')
		new_line += myreplace(i,'h','x')
		new_line += myreplace(i,'a','y')
		new_line += myreplace(i,'q','z')
		new_line += myreplace(i,' ',' ')
	if s != 0:
		print 'Case #'+ str(s)+': ' + new_line
		s = s+1
	else:
		s = s+1