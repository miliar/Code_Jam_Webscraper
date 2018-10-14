def flip(arr, begin, end):
    for i in range(begin, end):
        c = ''
        if arr[i] == '+':
            c = '-'
        if arr[i] == '-':
            c = '+'
        arr[i] = c
    return arr

def main():
    T = int(input())
    for t in range(0, T):
        s,k = input().split(' ')
        s = list(s)
        k = int(k)
        imp = 1
        done = False
        i = 0
        c = 0
        length = len(s)
        while(not(done)):
            # print('s: ', s, ' i: ', i)
            if s[i] == '-':
                if (i + k ) > length:
                    imp = -1
                    break
                else:
                    s = flip(s, i, i+k)
                    i = 0
                    c += 1
            i += 1
            if i == length:
                done = True
        result = str(c) if imp == 1 else "IMPOSSIBLE"
        print("Case #" + str(t+1) + ": " + result)

if __name__ == '__main__':
  main()
