import sys
import numpy as np

def flip(pancakes, k):

    opposite=False
    fblank = pancakes.find('-')
    segflip = list( pancakes[fblank: fblank + k] )

    if len(segflip) < k:
        segflip =  list( pancakes[fblank-k : fblank])
        opposite=True
        
    if len(segflip) < k:
        return 'IMPOSSIBLE' 
    
    
    for ei, ud in enumerate(segflip):

        if ud == '-':
            segflip[ei] = '+'
        else:
            segflip[ei] = '-'

            
    new_pancakes = list(pancakes)
    if opposite:
        new_pancakes[fblank-k:fblank] = ''.join(segflip)
    else:
        new_pancakes[fblank:fblank+k] = ''.join(segflip)
    
    return ''.join(new_pancakes)
            

def pancake_flipper(pancakes, k):

    count = 0
    max_count = 10*np.ceil( len(pancakes) / float(k) )

#    print pancakes, count
            
    while '-' in pancakes:
        
        pancakes = flip(pancakes, int(k))
        count+=1
#        print pancakes, count

        if count > max_count or pancakes == 'IMPOSSIBLE':
            return 'IMPOSSIBLE'
        
    return count







def main():

    args = sys.argv[1:]
    file = args[0]
    f= open(file, 'rU')
    data = f.read().splitlines()

    file_pre_index= file.find('.in')
    file_pre = file[: file_pre_index]    
    fw= open( file_pre + '.out' , 'w')
    
    num=int(data[0])

    for i in xrange(num):
        pancakes, k = data[i+1].split()
        output = pancake_flipper( pancakes, k)
#        print 'Case #%i: %s \n' % (i+1, str(output) )
        fw.write( 'Case #%i: %s \n' % (i+1, str(output) ) )
        
    fw.close()


if __name__ == '__main__':
    main()




