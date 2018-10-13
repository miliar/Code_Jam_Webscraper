#!/usr/bin/python3

def main():
    t = int(input());

    for i in range(t):
        a,b,k = input().split();
        a = int(a); b = int(b); k=int(k);

        count = 0;
        for ai in range(a):
            for bi in range(b):
                if ai&bi < k:
#                     print(ai,'&',bi,ai&bi);
                    count += 1;
        y = count;

        print('Case #%d: %d'%(i+1,y))   #, sep='',end='' );
    return 0;

if __name__ == '__main__':
    main();
