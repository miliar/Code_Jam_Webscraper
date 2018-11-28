import fileinput

def count_not_in_place(a):
    return sum([x[0]!=x[1] for x in zip(a,sorted(a))])

def do_line(i,l):
    elements = [int(x) for x in l.split()]
    print "Case #%d: %d"%(i+1,count_not_in_place(elements))

it = fileinput.input()
num_cases = int(it.next())

for i in range(num_cases):
    num_elements = int(it.next())
    do_line(i,it.next())



               
