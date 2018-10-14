import sys

start = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
end =   ['y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q']

case = open('input.txt', 'r').read()
allLines = case.split('\n')
k = 0

myfile = open('1.txt', 'wt')

for lines in allLines:



        stringList = list(lines)
        
        j = 0;
        for c in stringList:
            i = 0
            if c != ' ' :
                while end[i] != c:
                    i = i + 1
                    if (i > 25):
                        break
                if( i <26):
                    stringList[j] = start[i]
            else:
                stringList[j] = " "

            j = j+ 1

        myfile.write("Case #")
        myfile.write( str(k+1))
        myfile.write( ": ")
        for c in stringList:
            myfile.write( c)
        myfile.write('\n')
        k = k+1

myfile.close()

