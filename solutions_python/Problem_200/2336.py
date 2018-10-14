def get_tidy(n):
    f = n[0]
    s = f + ("0" * (len(n)-1))
    s = int(s)
    e = int(f * (len(n)))
    x = int(n)
    if x == e:
        return n
    if e > x:
        return(str(s-1))
    return n[0] + get_tidy(n[1:])

def main():
    t = int(raw_input())
    for index in range(t):
        n = str(raw_input())
        print "Case #"+str(index+1)+":",get_tidy(n)
main()

