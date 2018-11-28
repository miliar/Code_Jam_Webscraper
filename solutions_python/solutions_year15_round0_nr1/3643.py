"""Code written using Python 2.7.6, http://www.python.org/"""

def calc(case):
    #print case

    audience = 0
    friends = 0
    for shyness, num in enumerate(case[2:]):
        #print num, 'with shyness', shyness
        num = int(num)
        if shyness > audience and num > 0:
            friends += shyness - audience
            audience += friends
        audience += num


    result = friends

    return result
	
		
		

f = open('A-small.in', 'r')
lines = f.readlines()
f.close()
c = lines[0].split()[0]
#print c
lines = [r.strip() for r in lines[1:]]
#print cases

of = open('output_a.txt', 'w')

for idx, case in enumerate(lines):
    of.write('Case #%(idx)i: %(i)i\n' % {'idx': idx + 1, 'i': calc(case)})

of.close()
