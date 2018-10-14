import sys

def flip(arr, start_idx, k):
    for i in range(start_idx, k+start_idx):
        if(arr[i] == '-'):
            arr[i] = '+'
        else:
            arr[i] = '-'
    return arr        

def pancake_flipper(inputStr, k):
    arr = list(inputStr)
    count = 0
    for i in range(0, len(arr)-k+1):
        if(arr[i] == '-'):
            count += 1
            flip(arr, i, k)
    if '-' in arr:
        return "IMPOSSIBLE"
    return count        
            

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    for i in range(1, len(lines)):
        inputStr, k = lines[i].split(' ')
        print "Case #{}: {}".format(i, pancake_flipper(inputStr, int(k)))

