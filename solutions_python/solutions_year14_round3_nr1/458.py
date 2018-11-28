from fractions import gcd

def is_power2(num):
    return num != 0 and ((num & (num - 1)) == 0)

def main():

    input_file  = "A-large.in"
    output_file = "A-large.out"
    f = open(input_file, 'r')
    o = open(output_file, 'w')

    cases = int(f.readline())

    for i in range(1, cases + 1):
        P,Q = f.readline().split('/')
        P = int(P)
        Q = int (Q)

        # GCD
        g = gcd(P,Q)
        P = int(P/g)
        Q = int(Q/g)
        import math

        if P % 2 == 0 or (not is_power2(Q)):
            o.write("Case #%s: impossible\n" %(i))
            continue
        gen = int(math.log(Q, 2)) - int(math.log(P, 2))

        o.write("Case #%s: %s\n" %(i, gen))

    f.close()
    o.close()


if __name__ == '__main__':
    main()