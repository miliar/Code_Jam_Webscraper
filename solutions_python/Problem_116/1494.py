'''
Created on Apr 13, 2013

@author: Allen
'''

import os    

def check(arr):
    """Returns the status for the 4x4 array"""

    full = True
    
    result = checkWin(arr)
    
    if result is not None:
        return result
    
    for i in range(4):
        if '.' in arr[i]:
            full = False
            break
    
    if not full:
        return "Game has not completed"
    else:
        return "Draw"
    
    return "X won"

def checkWin(arr):
    """Returns the status if a player is winning"""
    
    for i in range(4):
        if line(arr[i]) is not None:
            return line(arr[i])
        if line([arr[0][i], arr[1][i], arr[2][i], arr[3][i]]) is not None:
            return line([arr[0][i], arr[1][i], arr[2][i], arr[3][i]])
    curr = line([arr[0][0], arr[1][1], arr[2][2], arr[3][3]])
    if curr is not None:
        return curr
    return line([arr[0][3], arr[1][2], arr[2][1], arr[3][0]])

def line(arr):
    """Returns which player is winning the line"""
    
    if '.' in arr:
        return None
    
    arr = arr[:]
    try:
        arr.remove('T')
    except ValueError:
        pass
    
    for i in range(len(arr) - 1):
        if arr[i] != arr[i+1]:
            return None
    
    return arr[0] + " won"

if __name__=="__main__":
    ext = 'large'
    
    cases = []
    
    with open(os.path.join(os.path.dirname(__file__), 'Tomek_' + ext + '.in')) as f:
        number = int(f.readline())
        for i in range(number):
            curr = []
            curr.append(list(f.readline().rstrip('\n')))
            curr.append(list(f.readline().rstrip('\n')))
            curr.append(list(f.readline().rstrip('\n')))
            curr.append(list(f.readline().rstrip('\n')))
            cases.append(curr)
            f.readline()
    
    output = ""
    for i in range(number):
        output += "Case #{0}: {1}\n".format(i+1, check(cases[i]))
    
    with open(os.path.join(os.path.dirname(__file__), 'Tomek_' + ext + '.out'), 'w') as f:
        f.write(output[:-1])