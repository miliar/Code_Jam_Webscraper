def foo(x):
       _,s = x.split()

       f = 0
       i = 1
       a = int(s[0])
       for si in s[1:]:
           if i > a:
               f = f + i - a
               a = i + int(si)
           else:
               a += int(si)
           i += 1

       return f

def main():
    for c in range(1,input()+1):
        print "Case #%d:"%c,foo(raw_input())

if __name__ == '__main__':
    main()
