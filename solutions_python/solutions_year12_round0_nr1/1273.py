
def read_int(file_handle, eol="\n"):
    return int(file_handle.readline().rstrip(eol))

def read_str(file_handle, eol="\n"):
    return file_handle.readline().rstrip(eol)
    
def read_int_list(file_handle, eol="\n", delimiter=" "):
    return [int(i) for i in file_handle.readline().rstrip(eol).split(delimiter)]

def read_str_list(file_handle, eol="\n", delimiter=" "):
    return [s for s in file_handle.readline().rstrip(eol).split(delimiter)]
    
def read_int_dict(file_handle, eol="\n", delimiter=" "):
    pos = 0
    d = {}
    for i in file_handle.readline().rstrip(eol).split(delimiter):
        d[int(i)] = pos
        pos += 1
    return d
    
size = 0;
name = "speaking"
size_text = ['small', 'large', 'example']
f = open('%s_%s.in' % (name, size_text[size]), 'rb')
fo = open('%s_%s.out' % (name, size_text[size]), 'wb')

input  = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv"
output = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup"

char_in = {"a" : "y",
           "b" : "h",
           "c" : "e",
           "d" : "s",
           "e" : "o",
           "f" : "c",
           "g" : "v",
           "h" : "x",
           "i" : "d",
           "j" : "u",
           "k" : "i",
           "l" : "g",
           "m" : "l",
           "n" : "b",
           "o" : "k",
           "p" : "r",
           "q" : "z", #q|z
           "r" : "t",
           "s" : "n",
           "t" : "w",
           "u" : "j",
           "v" : "p",
           "w" : "f",
           "x" : "m",
           "y" : "a",
           "z" : "q", #z|q
           " " : " ",
}

for i in xrange(ord('a'), ord('z')+ 1):
    if not(chr(i) in input):
        print chr(i)
print "---"
for i in xrange(ord('a'), ord('z')+ 1):
    if not(chr(i) in output):
        print chr(i)


T = read_int(f)
for i in xrange(1, T + 1):
    S = read_str(f)
    N = ""
    for j in xrange(0, len(S)):
        N += char_in[S[j]]
        
    output = "Case #%d: %s\n" % (i, N)
    print output
    fo.write(output)
                
f.close()
fo.close()