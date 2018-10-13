def sort(lst1,lst2):
    for i in range(len(lst1)-1):
        maxidx = i
        for j in range(i+1,len(lst1)):
            if lst1[j] > lst1[maxidx]:
                maxidx = j
        lst1[i],lst1[maxidx] = lst1[maxidx],lst1[i]
        lst2[i],lst2[maxidx] = lst2[maxidx],lst2[i]

t = int(input())
outputlist = []
for i in range(t):
    color = ['R', 'O', 'Y', 'G', 'B', 'V']
    inline = input()
    inline = inline.split()
    n = int(inline[0])
    lions = 6*[0]
    for j in range(6):
        lions[j] = int(inline[j+1])

    sort(lions,color)
    stable = ''
    while (lions[0] > 0) or (lions[1] > 0) or (lions[2] >0):
        if (lions[0] == lions[1]) or (lions[2] == 0):
            if lions[0] > 0:
                stable = stable + color[0]
                lions[0] -= 1
            if lions[1] > 0:
                stable = stable + color[1]
                lions[1] -= 1
            if lions[2] > 0:
                stable = stable + color[2]
                lions[2] -= 1
        else:
            if lions[0] > 0:
                stable = stable + color[0]
                lions[0] -= 1
            if lions[1] > 0:
                stable = stable + color[1]
                lions[1] -= 1
            if lions[0] > 0:
                stable = stable + color[0]
                lions[0] -= 1
            if lions[2] > 0:
                stable = stable + color[2]
                lions[2] -= 1

    if stable[0] != stable[len(stable)-1]:
        outputlist.append('Case #' + str(i+1) + ': ' + stable)
    else:
        outputlist.append('Case #' + str(i+1) + ': IMPOSSIBLE')

for i in range(t):
    print(outputlist[i])
