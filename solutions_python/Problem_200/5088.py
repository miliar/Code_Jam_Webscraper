t = int(input("Enter the test case\n"))
k =0
for j in range(t):
    a = list(input())
    a = [int(i) for i in a]
    if sorted(a) == a:
        #print("\n".join(a))
        #print(str(a).strip('[]'))
        #print(''.join(map(str, a)))
        final1 = ''.join(map(str, a))
        final1 = str(int(final1))
        # print(''.join(map(str, a)))
        print('Case #' + str(j+1) + ': ' + final1)
    else:
        for k in range(len(a)-1):
            if a[k] >= a[k+1]:
                a[k] = a[k] - 1
                l = k+1
                while(l!=len(a)):
                    a[l] = 9
                    l = l+1;
                final =''.join(map(str, a))
                final = str(int(final))
                #print(''.join(map(str, a)))
                print('Case #'+str(j+1)+': '+final)
                break


