import decimal

def getBlockIndex(num, ken_blocks):
    i = 0
    while(ken_blocks[i] < num):
        i += 1
    return i

def war_score(nomi_blocks, ken_blocks):
    ans = 0
    while(True):
        if(len(nomi_blocks) == 0):
            return ans
        if(nomi_blocks[0] > ken_blocks[-1]):
            nomi_blocks.pop(0)
            ken_blocks.pop(0)
            ans += 1
        else:
            i = getBlockIndex(nomi_blocks[0], ken_blocks)
            nomi_blocks.pop(0)
            ken_blocks.pop(i)

def perfect_win(nomi_blocks, ken_blocks):
    for i in xrange(len(nomi_blocks)):
        if(nomi_blocks[i] < ken_blocks[i]):
            return False
    return True

def deceit_score(nomi_blocks, ken_blocks):
    nomi_blocks = nomi_blocks[:]
    ken_blocks = ken_blocks[:]
    while(True):
        if(len(nomi_blocks) == 0):
            return 0
        if(perfect_win(nomi_blocks, ken_blocks)):
            return len(nomi_blocks)
        nomi_blocks.pop(0)
        ken_blocks.pop()

def main():
    input = open('input.txt', 'r')
    output = open('output.txt', 'w')

    T = int(input.readline())
    for casenum in xrange(1, T + 1):
        N = int(input.readline())
        line = input.readline().strip().split(' ')
        nomi_blocks = [decimal.Decimal(x) for x in line]
        line = input.readline().strip().split(' ')
        ken_blocks = [decimal.Decimal(x) for x in line]
        nomi_blocks.sort()
        ken_blocks.sort()

        y = deceit_score(nomi_blocks, ken_blocks)
        z = war_score(nomi_blocks, ken_blocks)

        output.write('Case #' + str(casenum) + ': ')
        output.write(str(y) + ' ' + str(z))
        output.write('\n')

    input.close()
    output.close()

main()