def proc_cards(f):
    # Read row selected
    sel = int(f.readline()) - 1
    # Read Cards
    for j in range(0, 4):
        k = f.readline()
        # We only want the row selected
        if j == sel:
            line = k
    return line.split()


def main():
    with open('A-small-attempt1.in', 'r') as f, open('output.out', 'w') as o:
        n = int(f.readline())
        for i in range(0, n):
            line1 = proc_cards(f)
            line2 = proc_cards(f)
            # Check the number that coincides in both rows
            nums = []
            for num in line1:
                if num in line2:
                    nums.append(num)
            
            if len(nums) > 1:
                res = "Case #%d: Bad magician!\n" % (i+1)
            elif len(nums) == 0:
                res = "Case #%d: Volunteer cheated!\n" % (i+1)
            else:
                res = "Case #%d: %s\n" % ((i+1), nums[0])
            o.write(res);
        f.close()



if __name__ == "__main__":
    main()