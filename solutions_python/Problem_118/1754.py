'''
Created on Apr 13, 2013

@author: jo
'''
from setuptools.command.egg_info import write_requirements
def read_input(path):
    f = open(path, "r")
    lines = f.readlines()
    f.close()
    return lines

def write_output(results, path):
    f = open(path, "w")
    body = ""
    for i, result in enumerate(results):
        body+="Case #%d: %s\n" % (i+1, result)
    f.write(body)
    f.close()

def is_pal(x):
    s = str(x)
    for i in range(len(s)):
        if s[i]!=s[len(s)-i-1]:
            return False
    return True
def is_square(x):
    sq = int(x**(0.5))
    return sq if x==sq**2 else -1
    
def main():
    lines = read_input("/Users/Jo/Downloads/c-small-attempt0.in")
    result = []
    for line in lines[1:]:
        i, j = line.split(" ")
        n = 0
        for x in range(int(i), int(j)+1):
            if is_pal(x):
                sq = is_square(x)
                if sq>0 and is_pal(sq):
                    n+=1
        result.append(n)
    write_output(result, "/Users/Jo/Downloads/csmall.out")
if __name__ == '__main__':
    main()