def flip(s, fr, length):
    strList = list(s)
    for i in range(fr, fr + length):
        strList[i] = '+' if strList[i] == '-' else '-'

    return ''.join(strList)
def main():
    t = input()

    for j in range(int(t)):
        s,k = input().split(' ')
        k = int(k)
        counter = 0
        for i in range(len(s)-k+1):
            if (s[i] == '-'):
                s = flip(s, i, k)
                counter += 1


        imp = False

        for i in range(len(s)):
            if s[i] == '-':
                imp = True

        print("Case #{}:".format(j+1), "IMPOSSIBLE" if imp else counter)

main()