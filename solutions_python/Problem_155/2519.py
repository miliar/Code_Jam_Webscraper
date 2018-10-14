import fileinput

def main():

    # inputs
    T = int(raw_input())
    # input = map(int, raw_input().split())

    # arr
    S_max = T*[0]
    S_data = []
    for i in range(T):
        line = map(str, raw_input().split())
        S_max[i] = int(line[0])
        S_data.append(line[1])

    #print S_max, S_data

    # calculation
    for i in range(T):
        max = S_max[i] + 1
        data = S_data[i]

        out = 0
        count = 0
        for j in range(max):
            audience = int(data[j])
            if count < j:
                out += j - count
                audience += j - count

            count += audience
        print "Case #"+ str(i+1) + ": " + str(out)



    return 0


if __name__ == "__main__":
    main()
