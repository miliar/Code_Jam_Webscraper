playr = {1:"GABRIEL",0:"RICHARD"}

def winnr(X,R,C):
    if (R*C)%X != 0:
        return(0)
    elif X == 1:
        return(1)
    elif X==2:
        return(1)
    elif X==3:
        if 2<=min(R,C):
            return(1)
        else:
            return(0)
    else:
        if 3<=min(R,C):
            return(1)
        else:
            return(0)
