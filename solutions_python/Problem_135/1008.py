def getAnswer(ans1, arr1, ans2, arr2):
    variants = 0
    answer = -1
    for nr in arr1[int(ans1)-1]:
        if nr in arr2[int(ans2)-1]:
            variants += 1
            answer = nr

    if variants == 0:
        return "Volunteer cheated!"
    elif variants == 1:
        return str(answer)
    elif variants > 1:
        return "Bad magician!"

response = ""
f = open("in.txt", "r")
data = f.readlines()
f.close()

cases = int(data[0].rstrip())
for i in xrange(cases):
    ans = getAnswer(
        data[i*10+1],
        [data[i*10+2].rstrip().split(), data[i*10+3].rstrip().split(), data[i*10+4].rstrip().split(), data[i*10+5].rstrip().split()],
        data[i*10+6],
        [data[i*10+7].rstrip().split(), data[i*10+8].rstrip().split(), data[i*10+9].rstrip().split(), data[i*10+10].rstrip().split()]
    )
    response += "Case #"+str(i+1)+": "+ans+"\n"

f = open("out.txt", "w")
f.write(response)
f.close()