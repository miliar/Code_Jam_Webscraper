def calcGuests(max, vals):
    guests = 0;
    invite = 0;
    index = 0;

    for char in vals:
        tmpGuests = int(char)

        if guests >= index and tmpGuests != 0:
            guests = guests + tmpGuests
        elif index > guests and tmpGuests != 0:
            invite = invite + (index-guests)
            guests = guests + invite + tmpGuests

        index = index + 1

    print(int(invite))

def main():
    filename = input()
    txt = open(filename)
    num = txt.readline()
    num = num.split()
    test = int(num[0])
    i = 1
    while (i < test+1):
        params = txt.readline()
        nums = params.split()
        print("Case #%d: " %i, end = "")
        calcGuests(nums[0],nums[1])
        i = i + 1

if __name__ == '__main__':
    main()
