import io

def main(ca):
    n = input()
    data = raw_input().split()
    r = 0
    for i in range(n):
        if i+1 != int(data[i]):
            r += 1
    print "Case #" + str(ca) + ": " + str(r)

if __name__=="__main__":
    cas = input()
    for i in range(cas):
        main(i+1)
