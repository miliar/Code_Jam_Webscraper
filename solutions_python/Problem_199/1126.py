class PancakeFlipper(object):
    
    def flip_num(self, pan, n):        
        pan = list(map(lambda a: (a-43)//2, map(ord, pan)))
        # print(pan)
        l = len(pan)
        
        idx = 0
        cnt = 0
        while idx < l - n + 1:
            if pan[idx] == 1:                
                for ch in range(idx,idx+n):
                    pan[ch] = 1 - pan[ch]
                cnt += 1
                # print('step {:d}:'.format(cnt), end='')
                # print(pan)                
            idx += 1
        idx -= 1
        if sum(pan[idx:]) > 0:
            return 'IMPOSSIBLE'
        
        return cnt   
        
def main():
    sol = PancakeFlipper()    
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        line = input().split(' ')#[int(s) for s in input().split(" ")]
        # print(line)
        res = sol.flip_num(line[0], int(line[1]))
        print("Case #{}: {} ".format(i, res))

if __name__ == '__main__':
    main()
  
