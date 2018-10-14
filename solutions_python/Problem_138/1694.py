import sys

input = []

def qsort(arr): 
     if len(arr) <= 1:
          return arr
     else:
          return qsort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x>=arr[0]])

def parse_file(filePath):
    with open(filePath) as f:
        T = int(f.readline())
        for i in range(T):
            N = int(f.readline())
            naomis = [float(x) for x in f.readline().split()]
            kens = [float(x) for x in f.readline().split()]
            input.append((naomis, kens))

def play_war(naomis, kens):
    kens = qsort(kens)
    naomiPts = 0
    for n, ChosenNaomi in enumerate(naomis):
        ChosenKenIdx = -1
        for j, ChosenKen in enumerate(kens):
            if ChosenKen > ChosenNaomi:
                ChosenKenIdx = j
                break
        if ChosenKenIdx == -1:
            naomiPts += 1
            kens.pop(0)
        else:
            kens.pop(ChosenKenIdx)
    return naomiPts

def play_deceitful_war(naomis, kens):
    naomis = qsort(naomis)
    kens = qsort(kens)
    naomiPts = 0
    for naomisBlock in naomis:
        peekKens = kens[-1]
        if naomisBlock > kens[0]:
            ChosenNaomi = kens[-1] + 0.000001
        elif len(kens) > 1:
            ChosenNaomi = kens[-2] + (kens[-1] - kens[-2])/2
        else:
            #if len(kens) == 1 or naomisBlock > kens[-1]:
            #ToldNaomi = naomisBlock
            ChosenNaomi = naomisBlock
    
        ChosenKenIdx = -1
        for j, ChosenKen in enumerate(kens):
            if ChosenKen > ChosenNaomi:
                ChosenKenIdx = j
                break
        if ChosenKenIdx == -1:
            naomiPts += 1
            kens.pop(0)
        else:
            kens.pop(ChosenKenIdx)
    return naomiPts
            
def main():
    parse_file(sys.argv[1])
    currTest = 1
    for naomis, kens in input:
        print('Case #%d: %d %d' % (currTest, play_deceitful_war(naomis[:], kens[:]), play_war(naomis[:], kens[:])))
        currTest += 1

if __name__ == '__main__':
    main()    
