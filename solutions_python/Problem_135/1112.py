def main():
    f = open("card_magic.txt", "r")
    out = open("output.txt", "w")
    line = f.readline().strip('\r\n').split(' ')[0]
    for x in xrange(1,int(line)+1):
        a = solve(f)
        ans = "Case #%s: %s\n"
        if len(a) > 1:
            ans = ans % (x, "Bad magician!")
        elif len(a) < 1:
        	ans = ans % (x, "Volunteer cheated!")
        else:
        	ans = ans % (x, a.pop())
        out.write(ans)

def solve(f):
    first_set = get_set(f)
    second_set = get_set(f)
    return first_set & second_set

def get_set(f):
    answer = int(f.readline().strip('\r\n').split(' ')[0])
    line = ""
    for l in xrange(1, 5):
        if l == answer:
            line = f.readline()
        else:
            f.readline()
    return set(line.strip('\r\n').split(' '))

if __name__ == '__main__':
    main()