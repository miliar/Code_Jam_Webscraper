__author__ = 'root'
def calculate (smax , li = None):
    li = map(int,li)
    val = zip(li, range(smax+1))
    sum =0;
    tot =0;
    ned =0
    for x in range(smax+1):

        (how , level) = val[x]
      #  print  val[x]
        if tot >=level:
            tot+=how
        else:
            ned+= level -tot
            tot+= how+level-tot

       # print tot ,ned



    return  ned
fname = 'A.in'
with open(fname) as f:
    content = f.readlines()

li = [x.strip() for x in content ]

te = int(li[0])
li.pop(0)
for x in range(te):
    [smax, shy] = li[x].split()
    ned =calculate(int(smax), list(shy))

    print 'Case #%d: %d' % (x+1,ned)

   # print  [smax, shy]
