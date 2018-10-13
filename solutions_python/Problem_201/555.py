# Problem C - Bathroom Tiles
from math import log
from math import ceil
from math import floor

def openfile(filename, separator = False):
    # Open the .in file specified by filename as a string 
    # Split it into a list (using the separator if specified)
    # Return that list    
    string = open(filename).read()
    if separator == False: return string.split()
    return string.split(separator)

input_filename = 'C-large.in'
output_filename = 'C-large-output.in'

def main(input_filename, output_filename):
    
    lis = openfile(input_filename)
    output_file = open(output_filename,'w')
    
    for i in range(1,int(lis[0])+1):
        n=int(lis[2*i-1])
        k=int(lis[2*i])
        res = split(dictionary(n,k))
        text = 'Case #{}: {} {}\n'.format(i, res[0],res[1])
        output_file.write(str(text))

# MAINNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN


def split(M):
    # Given M consecutive spaces, pick the middle space and return the spaces remaining on either side
    if M//2 == M/2: 
        return sorted([M//2-1, M//2], reverse=True)
    return sorted([M//2, M//2], reverse = True)

def brute(n,k):
    # Keep a list of spaces available to the ith person
    # note the MAX VALUE of the list when i = k
    # return split(MAX VALUE)
    n = int(n)
    k = int(k)
    spaces = [n] # seen by the 1st person
    for i in range(k-1):
        m = max(spaces)
        spaces.remove(m)
        spaces.append(split(m)[0])
        spaces.append(split(m)[1])
        while 0 in spaces: spaces.remove(0)
        spaces.sort(reverse = True)
    #print('spaces seen:', spaces)
    #print('max spaces :', max(spaces))
    #print('SL and SR  :',split(max(spaces)))
    return max(spaces)


def dictionary(n,k):    
    # A space m consists of m empty stalls between people
    # There may be n instances of the space m
    # dic = {m: n} = {m1:n1, m2:n2, m3:n3 ...}
   
    dic = {n:1} # First person sees one space of length m
    while k > 0:
        m = max(dic) # longest space seen by next person
        n = dic[m] # number of occurences of m tiles
        d = min([k,n]) # #of occurences (n) OR #of people left (k):
        k -= d # d people enter
        dic[m] -= d # d m-spaces are split up 
        if dic[m] == 0: del(dic[m]) # Remove zero entries 
        
        a = split(m)[0] # split(m) new spaces are created
        b = split(m)[1]        
        if a in dic: dic[a] += n
        else: dic[a] = n             
        if b in dic: dic[b] += n
        else: dic[b] = n
    
    return m # longest stall seen by kth person