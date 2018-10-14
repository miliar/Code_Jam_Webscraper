
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
    
size = 1;
name = "dancing"
size_text = ['small', 'large', 'example']
f = open('%s_%s.in' % (name, size_text[size]), 'rb')
fo = open('%s_%s.out' % (name, size_text[size]), 'wb')



T = read_int(f)
for i in xrange(1, T + 1):
    G = read_int_list(f)
    N = G.pop(0)
    S = G.pop(0)
    P = G.pop(0)
    total = 0
    surprising = 0

    # Count those that make it normally
    for j in xrange(0, N):
        R = G[j-total]/3 + min(1, G[j-total]%3)
        if (R >= P):
            G.pop(j-total)
            total += 1

    # Count those that make it with a surprising case
    for j in xrange(0, len(G)):
        if (surprising == S):
            break
        U = P+2*max(0, P-2)
        if (G[j] >= U):
            total += 1
            surprising += 1

    output = "Case #%d: %d\n" % (i, total)
    fo.write(output)
                
f.close()
fo.close()