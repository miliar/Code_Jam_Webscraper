infile = open('/home/suguman/Downloads/D-small-attempt2.in','r')
'''infile = open('/home/suguman/Desktop/input.txt', 'r')'''
outfile = open('/home/suguman/Desktop/output4.txt','w')

def DWar(s1, s2, size):
    if size == 0: 
        return 0
    else:
        if s1[0] > s2[size-1]:
            '''return (1 + DWar(s1[1:], s2[:size], size-1))'''
            return size
        elif s1[0] < s2[0]:
            return DWar(s1[1:], s2[:size], size-1)
        elif s1[0] > s2[0]:
            return (1 + DWar(s1[1:], s2[1:], size-1))

def War(s1, s2, size):
    if size == 0:
        return 0
    else:
        if s1[0] > s2[size-1]:
            return size
        elif s1[0] < s2[0]:
            return  War(s1[1:], s2[1:], size-1)
        else:
            i = 0
            while(s1[0]>s2[i]):
                i = i+1
            return War(s1[1:], s2[:i]+s2[i+1:], size-1)
                

x = int(infile.readline())

for i in range(x):
    size = int(infile.readline())
    l1 = infile.readline().split()
    for k in l1:
        k = float(k)
    l1 = sorted(l1)
    '''outfile.write(str(l1) + '\n')'''

    l2 = infile.readline().split()
    for k in l2:
        k = float(k)
    l2 = sorted(l2)
    '''outfile.write(str(l2) + '\n')'''

    outfile.write('Case #'+str(i+1)+': ' + str(DWar(l1, l2, size))+ ' ' + str(War(l1, l2, size))+'\n')
    
    
