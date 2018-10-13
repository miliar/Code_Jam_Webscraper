#! /usr/bin/python
import sys
    
def main():
    file1=open(sys.argv[1])
    
    a=file1.readlines()
    
    cases=int(a.pop(0))
    translation={}
    

    string1="ejp mysljylc kd kxveddknmc re jsicpdrysi"
    string2="our language is impossible to understand"
    addToTranslation(translation,string1,string2)
    
    string1="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
    string2="there are twenty six factorial possibilities"
    addToTranslation(translation,string1,string2)

    string1="de kr kd eoya kw aej tysr re ujdr lkgc jv"
    string2="so it is okay if you want to just give up"
    addToTranslation(translation,string1,string2)
    translation["q"]="z"
    translation["y"]="a"
    translation["z"]="q"

    answers=[]
    
    for x in range(cases):
        answers.append(translate(translation,a.pop(0)))
    strings=[]
    for x in range(cases):
        string1="Case #"+str(x+1)

        string1+=": "+ answers[x]

        strings.append(string1)
        print answers[x]
    f=open("Output.txt","w")
    for x in strings:
        f.write(x)
    
def addToTranslation(dictionary,string1,string2):
    for x in xrange(len(string1)):
        dictionary[string1[x]]=string2[x]

def translate(dictionary,string):
    returnVal=""
    for x in string:
        try:
            returnVal+=dictionary[x]
        except:
            returnVal+=x
    return returnVal



if __name__ == "__main__":
    main()
