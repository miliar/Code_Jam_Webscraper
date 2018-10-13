def main(num, trial, output):
    largestTidy = ''
    for x in range(1, num+1):
        strx = str(x)
        least = 0
        tidy = True
        for ch in strx:
            if int(ch)>=least:
                least = int(ch)
            else:
                tidy = False
                break
        if tidy:
            largestTidy = strx
    output.write("Case #" + str(trial) + ": " + largestTidy + "\n")

def init():
    n = int(raw_input())
    output = open("output.txt", 'w')
    for trial in range(1, n+1):
        num = int(raw_input())
        main(num, trial, output)
    output.close()    

init()
