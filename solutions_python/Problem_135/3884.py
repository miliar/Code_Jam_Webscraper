import sys

x = 0;
n = sys.stdin.readline()
n = int(n)



while (x < n):
    x = x + 1 #count
    num = 0
  
    r = sys.stdin.readline()
    r = int(r )
	
    cards = []
    cards2 = []
    
    cards.append(sys.stdin.readline().split())
    cards.append(sys.stdin.readline().split())
    cards.append(sys.stdin.readline().split())
    cards.append(sys.stdin.readline().split())
    
    r2 = sys.stdin.readline()
    r2 = int(r2)
    
    cards2.append(sys.stdin.readline().split())
    cards2.append(sys.stdin.readline().split())
    cards2.append(sys.stdin.readline().split())
    cards2.append(sys.stdin.readline().split())
    
    
    flag = 0
    card = 0
    
    for card1 in cards[r - 1]:
        for card2 in cards2[r2 - 1]:
            if (card1 == card2):
                flag = flag + 1
                card = card1
    
    
    if (flag == 1):
        print("Case #",x,": ",card, sep='')
    else:
        if (flag == 0):
            print("Case #",x,": Volunteer cheated!", sep='')
        else:
            print("Case #",x,": Bad magician!", sep='')
    
    
    