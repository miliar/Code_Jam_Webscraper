__author__ = 'uritwig'

output =['our language is impossible to understand',
        'there are twenty six factorial possibilities',
        'so it is okay if you want to just give up'];


def main():

    #fp = open('C-large-practice.in','r')
    fp = open('example.txt','r')

    cases =  int(fp.readline())

    map = {'z':'q','o':'e','a':'y','q':'z'}
    for case in range(0,cases):
        message = fp.readline().strip('\n')

        for i in range(0,len(message)):
            map[message[i]] = output[case][i]

    
    fp = open('A-small-attempt1.in','r')

    cases =  int(fp.readline())

    for case in range(0,cases):

        message = fp.readline().strip('\n')

        translated = ''

        for i in range(0,len(message)):
            translated += map[message[i]]


        print  "Case #%d: %s" % (case+1,translated)





main()