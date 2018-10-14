'''
Created on 13. 4. 2012.

@author: Dracon
'''

def main():
    input2 = open('A-small-attempt0.in','r')
    output = open('A-small-attempt0.out','w')
    slova = ['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q']
    line = input2.readline()
    for i in range(0,int(line)):
        linija = input2.readline()
        output.write("Case #"+str(i+1)+": ")
        for j in linija.strip():
            if j == ' ':
                output.write(j)
            else:
                output.write(slova[ord(j)-97])
        output.write('\n')
if __name__ == '__main__':
    main()