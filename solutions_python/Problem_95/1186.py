def main():
    list3 = []
    f = open('A-small-attempt1.in','r')
    f2 = open('output','w')
    tuple1 = ('z','q')
    str2 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
    str1 = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'
    list1 = [str1[i] for i in range(len(str1))]
    list2 = [str2[i] for i in range(len(str2))]
    list1.append('z')
    list2.append('q')
    list1.append('q')
    list2.append('z')
    i=0
    for line in f:
        if i != 0:
            list3 = []
            str3 = line.strip()
            for k in range(len(str3)):
                list3.append(list1[list2.index(str3[k])])
            #print 'Case #%d: '%i + ''.join(list3)
            f2.write('Case #%d: '%i + ''.join(list3) + '\n')
        i += 1
    f.close()
    f2.close()
if __name__ == "__main__":main()
