import sys

from string import maketrans   # Required to call maketrans function.

def main(raw_data):
    letter_dict = {}
    samples = (
        ('y qee', 'a zoo'),
        ('ejp mysljylc kd kxveddknmc re jsicpdrysi','our language is impossible to understand'),
        ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd','there are twenty six factorial possibilities'),
        ('de kr kd eoya kw aej tysr re ujdr lkgc jv','so it is okay if you want to just give up'),
        ('z','q'),
    )

    for source, output in samples:
        for i,char in enumerate(source):
            letter_dict[char] = output[i]
            
    intab = ''
    outtab = ''
    for key, value in letter_dict.items():
        intab += key
        outtab += value
    trantab = maketrans(intab, outtab)

    data = []
    for line in raw_data:
        data.append(line)
        
    T = data.pop(0)
    for i in range(int(T)):
        print "Case #%s: %s" %(i+1, data[i].translate(trantab))
        
        
if __name__ == "__main__":
    main(sys.stdin)
