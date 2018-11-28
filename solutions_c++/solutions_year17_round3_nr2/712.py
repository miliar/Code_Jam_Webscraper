#include<bits/stdc++.h>
using namespace std;
int dp[1445][725][3], ara[1445], st;
int cnt(int t, int pas, int las)
{
    int i, j, k;
    if(t == 1440)
    {
        if(pas == 720)
            return (las == st)? 0: 1;
        else
            return 100000;
    }
    if(pas > 720 || t-pas > 720)
        return 100000;
    if(dp[t][pas][las] != -1)
        return dp[t][pas][las];
    if(ara[t] == -1)
        dp[t][pas][las] = min(cnt(t+1, pas+1, 0)+las, cnt(t+1, pas, 1)+!las);
    else if(ara[t] == 0)
        dp[t][pas][las] = cnt(t+1, pas+1, 0)+las;
    else
        dp[t][pas][las] = cnt(t+1, pas, 1)+!las;
    return dp[t][pas][las];
}
int main()
{
    //freopen("B-large.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t, k, i, j, p, q, x, y, ac, aj;
    scanf("%d", &t);
    for(k = 1; k <= t; k++)
    {
        scanf("%d %d", &ac, &aj);
        memset(ara, -1, sizeof(ara));
        memset(dp, -1, sizeof(dp));
        for(i = 0; i < ac; i++)
        {
            scanf("%d %d", &x, &y);
            for(p = x; p < y; p++)
                ara[p] = 1;
        }
        for(i = 0; i < aj; i++)
        {
            scanf("%d %d", &x, &y);
            for(p = x; p < y; p++)
                ara[p] = 0;
        }
        p = q = 100000;
        if(ara[0] != 1)
        {
            st = 0;
            p = cnt(1, 1, 0);
        }
        if(ara[0])
        {
            st = 1;
            memset(dp, -1, sizeof(dp));
            q = cnt(1, 0, 1);
        }
        //printf("%d %d\n", p, q);
        printf("Case #%d: %d\n", k, min(p, q));
    }
    return 0;
}
