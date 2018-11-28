
def is_tidy(number):
    s = str(number)

    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False

    return True

if __name__ == "__main__":
    T = int(input())

    for i in range(1,T+1):
        N = int(input())
        number = N

        while not is_tidy(number):
            N_list = []
            for s in str(number):
                N_list.append(int(s))

            for j in range(len(N_list)-1):
                #print(N_list)
                if N_list[j] > N_list[j+1]:
                    N_list[j] -= 1
                    for k in range(len(N_list)-j-1):
                        N_list[j+k+1] = 9

            number = int("".join([ str(n) for n in N_list ]))

        print("Case #%i: %i" % (i, number))
