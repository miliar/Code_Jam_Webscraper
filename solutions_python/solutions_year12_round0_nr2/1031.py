__author__ = 'uritwig'

output =['our language is impossible to understand',
        'there are twenty six factorial possibilities',
        'so it is okay if you want to just give up'];


def main():

    #fp = open('C-large-practice.in','r')
    fp = open('B-large.in','r')

    cases =  int(fp.readline())


    for case in range(0,cases):
        V = [int(i) for i in fp.readline().split(' ')]

        N = V[0]  #num of googlers
        S = V[1]  #suprise
        p = V[2]  #minimum

        V = V[3:] # scores

        #print 'N=%d S=%d p=%d v=%s' % (N,S,p,str(V))

        g = 0
        s = 0
        for score in V:
            score = float(score)
            j2 = (score - p)/2.

            if j2 < 0:
                continue
                
            #print j2,p
            if j2 < p - 2:
                continue
                #print '#'
            elif j2 < p - 1:
                s +=1
                #print 'S'
            else:
                g += 1

                #print 'G'


        if s > S:
            s = S

        print 'Case #%d: %d' % (case+1,s+g)









main()