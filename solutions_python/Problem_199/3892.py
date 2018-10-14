def flip(c):
    if c == '+':
        return '-'
    else:
        return '+'
def checkFlipped(arr):
    for i in arr:
        if i != '+':
            return False
    return True

def flipFromLeft(arr, k):
    flips = 0
    i = 0
    while i <= (len(arr) - k):
        if arr[i] != '+':
            for j in range(k):
                arr[i+j] = flip(arr[i+j])
            flips = flips + 1
        i = i + 1
    print arr
    if checkFlipped(arr):
        return flips
    else:
        return "IMPOSSIBLE"

def solution(content):
    cases = int(content[0])
    f = open("output_pancake.txt", "w")

    for case in range(cases):
        line = content[case+1]
        tokens = line.split(" ")
        s = list(tokens[0])
        k = int(tokens[1])
        ans = flipFromLeft(s,k)
        f.write("Case #" + str(case+1) + ": " + str(ans) + "\n")
    f.close()

        
def main():
    fname = "test_pancake.txt"
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    solution(content)

main()