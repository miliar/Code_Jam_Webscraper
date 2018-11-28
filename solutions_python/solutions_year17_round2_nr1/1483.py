
def main():
    # read number of tests
    ntests = int(input())

    for t in range(0, ntests):
        # read destination and number horses
        dest, nhorses = [int(s) for s in input().split(" ")]

        maxt = 0.0

        #read rows
        for horse in range(nhorses):
            pos, speed = [float(s) for s in input().split(" ")]
            # calculate time to dest

            time = (dest - pos)/speed

            if time > maxt:
                maxt = time

        annietime = dest/maxt

        print("Case #{}: {}".format(t+1, annietime))

if __name__ == '__main__':
    main()
