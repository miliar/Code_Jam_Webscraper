import string

gstr = ' acbedgfihkjmlonpsrutwvyxqz'
hstr = ' yehosvcdxiulgkbrntjwfpamzq'

translationtable = string.maketrans(gstr,hstr)
fn = raw_input('File Name:')
f = open(fn)
o = open('output.txt','w')

number_of_items = int(f.readline())

for i in range(number_of_items):
	gree = f.readline()
	o.write("Case #" + str(i+1) +': '+ gree.translate(translationtable))

f.close()
o.close()