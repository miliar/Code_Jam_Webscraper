
def isTydi(n):
    string = str(n)
    num = int(string[0])
    for i in range(len(string)):
        if int(string[i])<num:
            return False
        num = int(string[i])
    return True

my_file = open('/Volumes/Almacenamiento/PE/CodeJam2017-1B/B-small-attempt0.in','r')
my_out = open('/Volumes/Almacenamiento/PE/CodeJam2017-1B/20171B.out','w')

T = int(my_file.next())

for i in range(T):
    N = int(my_file.next())
    while (not isTydi(N)):
        N = N-1
    
    my_out.write('Case #'+str(i+1)+': '+str(N)+'\n')
    print 'Case #'+str(i+1)+': '+str(N)+'\n'

my_file.close()
my_out.close()