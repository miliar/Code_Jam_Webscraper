error_msg = 'IMPOSSIBLE'

def pure_unicorns(N,R,Y,B):    
    
    
    ryb = [(R,'R'),(Y,'Y'),(B,'B')]
    ryb.sort(key = lambda tup: tup[0], reverse = True)
    
    (x,xs),(y,ys),(z,zs) = ryb
    
    if x * 2 > N:
        return error_msg
    
    pure = (xs+ys+zs)*(y+z-x) + (xs+ys)*(x-z) + (xs+zs)*(x-y)
    
    return pure
    
    

def set_unicorns(unicorns):
    N,R,O,Y,G,B,V = unicorns
    
    if O == B and O + B == N:
        return 'OB'*(N//2)
    if G == R and G + R == N:
        return 'GR'*(N//2)
    if V == Y and V + Y == N:
        return 'VY'*(N//2)

    
    if (O > 0 and O > B - 1) or (G > 0 and G > R - 1) or (V > 0 and V > Y - 1):
        return error_msg
    
    pure = pure_unicorns(N-2*(O+G+V), R-G, Y-V, B-O)
    
    if pure == error_msg:
        return error_msg
    
   
    pure = pure.replace('B','B'+'OB'*O,1)
    pure = pure.replace('R','R'+'GR'*G,1)
    pure = pure.replace('Y','Y'+'VY'*V,1)
    
    return pure



T = int(input())

for t in range(1,(T+1)):
    unicorns = [int(s) for s in input().split(' ')]
    print('Case #{}: {}'.format(t, set_unicorns(unicorns)))
