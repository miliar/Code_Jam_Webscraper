from Solve import *

RICHARD = "RICHARD"
GABRIEL = "GABRIEL"

def ominousOmino(args):
    n, x, y = [int(elem) for elem in args[0].split(" ")]
    totalTiles = x * y
    nHalf = n / 2
    
    #hole
    if n > 6:
        return RICHARD
    #wrong dimensions
    if totalTiles % n != 0:
        return RICHARD
    #square x-omino
    if nHalf > x or nHalf > y:
        return RICHARD
    #straight x-omino
    if n > x and n > y:
        return RICHARD
    #too small grid
    if x <= n - 2 or y <= n - 2:
        return RICHARD
          
    return GABRIEL
    
solveF("F:\ProgramiranjeOstalo/GCJ/q2015/D-small-attempt0.in", ominousOmino, 1)