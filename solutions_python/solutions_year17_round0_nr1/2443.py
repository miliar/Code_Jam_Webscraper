# python2
import sys
import os.path

def main():
    if os.path.exists('input.txt'):
        input = open('input.txt', 'r')
    else:
        input = sys.stdin
    #--------------------------------INPUT---------------------------------
    n = int(input.readline())
    results = []
    for z in xrange(n):
        init = list(map(str, input.readline().split()))
        s,k,counter,result = list(init[0]),int(init[1]),0,''
        
        for i in xrange(0,len(s)):
            if s[i]=='-' and i+k > len(s):
                result = 'IMPOSSIBLE'
                break
            elif s[i]=='-':
                counter +=1
                for y in xrange(i,i+k):
                    if s[y] == '+':
                        s[y] = '-'
                    else:
                        s[y] = '+'
        if result != '':
            results.append('Case #'+str(z+1)+': '+result)
        else:
            results.append('Case #'+str(z+1)+': '+str(counter))
    output = '\n'.join(map(str, results))
    #-------------------------------OUTPUT----------------------------------
    if os.path.exists('output.txt'):
        open('output.txt', 'w').writelines(str(output))
    else:
        sys.stdout.write(str(output))


if __name__ == "__main__":
    main()
