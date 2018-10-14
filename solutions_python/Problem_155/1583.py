def minF(n,shy):
    ans = 0
    cuml = 0
    for i in range(n+1):
        if i<=cuml:
            cuml += int(shy[i])
        else:
            xtra = i-cuml
            cuml+=xtra+int(shy[i])
            ans+=xtra
    return(ans)
            
        
