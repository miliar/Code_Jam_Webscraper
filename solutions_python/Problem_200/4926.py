# Problem B : Tidy Numbers

T = int(input())

for i in range(1,T+1):
    N = int(input())
    for j in range(N,0,-1):
        if (len(str(j))) == 1:
            print("Case #" + str(i) + ": " + str(j))
            break
        
        # Split into digits
        digits = [int(x) for x in str(j)]

        # Check if sorted
        if digits == sorted(digits):
            print("Case #" + str(i) + ": " + str(j))
            break
        
