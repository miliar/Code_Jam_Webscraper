import io

samples = {'ejp mysljylc kd kxveddknmc re jsicpdrysi':'our language is impossible to understand',
           'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd':'there are twenty six factorial possibilities',
           'de kr kd eoya kw aej tysr re ujdr lkgc jv':'so it is okay if you want to just give up'};

input = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd';
output = str();
myMap = {'y':'a','q':'z','e':'o'}

def prepare_dict(samples):
    for s,t in samples.items():
        for i in range(0,len(s)):
            if s[i] in myMap:
                assert (myMap[s[i]] == t[i])
            else:
                myMap[s[i]] = t[i]

    #if one letter is missing, fix it
    for c in range(ord('a'), ord('z')+1):
        if not chr(c) in myMap:
            for b in range(ord('a'), ord('z')+1):
                if not chr(b) in myMap.values():
                    myMap[chr(c)] = chr(b);

def translate(s):
    output = str();
    for i in range(0,len(s)):
        if s[i] in myMap:
            output+=myMap[s[i]]
        else:
            exit("Missing in list")
    return output

def main():
    fd = open( "input.txt" )
    numoflines = int(fd.readline())
    prepare_dict(samples)
    for i in range (1,numoflines+1):
        print ("Case #%d: %s"%(i,translate(fd.readline().replace("\n",""))))
    pass

if __name__ == '__main__':
    main()
