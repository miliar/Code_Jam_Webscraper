import sys

before = "abcdefghijklmnopqrstuvwxyz "
after = "yhesocvxduiglbkrztnwjpfmaq "

def main():
    T = sys.stdin.readline().lstrip()
    table = {}
    for bef, aft in zip(before, after):
        table[bef] = aft
    for case in xrange(int(T)):
        line = sys.stdin.readline().rstrip()
        ans = ""
        for i in line:
            ans += table[i]
        print "Case #%d: %s" % (case+1, ans)
    
if __name__ == "__main__":
    main()