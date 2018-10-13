#!/usr/bin/python
computed = {('',''):1}
def findTotal(text,pat):
    if len(pat)>len(text):
        return 0
    #print text,":",pat
    if computed.has_key((text,pat)):
        return computed[(text,pat)]
    if pat=='':return 1
    c = text.count(pat[0])
    if c==0:
        return 0
    toks = text.split(pat[0])
    if len(toks)>c:toks=toks[1:]
    t = 0
    for i in xrange(len(toks)):
        t+=findTotal(pat[0].join(toks[i:]),pat[1:])
    computed[(text,pat)]=t    
    return t
if __name__ == "__main__":
    import sys
    N = int(sys.stdin.readline())
    for i in xrange(N):
      text = sys.stdin.readline().strip()
      #print len(text)
      #print pat
      computed = {('',''):1}
      t = findTotal(text,"welcome to code jam")
      print "Case #%d: %04d" %(i+1,t%10000)

