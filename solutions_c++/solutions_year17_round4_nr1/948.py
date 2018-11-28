#include<bits/stdc++.h>
using namespace std;
int dp[105][105][105][4], n, p;
int cnt(int ct1, int ct2, int ct3, int cumsum)
{
    int x, y;
    if(ct1+ct2+ct3 < 2)
        return 0;
    if(dp[ct1][ct2][ct3][cumsum] != -1)
        return dp[ct1][ct2][ct3][cumsum];
    x = 0;
    if(ct1)
        y = ((cumsum+1)%p == 0)? 1: 0, x = max(x, y+cnt(ct1-1, ct2, ct3, (cumsum+1)%p));
    if(ct2)
        y = ((cumsum+2)%p == 0)? 1: 0, x = max(x, y+cnt(ct1, ct2-1, ct3, (cumsum+2)%p));
    if(ct3)
        y = ((cumsum+3)%p == 0)? 1: 0, x = max(x, y+cnt(ct1, ct2, ct3-1, (cumsum+3)%p));
    dp[ct1][ct2][ct3][cumsum] = x;
    return x;
}
int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t, i, j, k, q, x, y, ct0, ct1, ct2, ct3;
    scanf("%d", &t);
    for(k = 1; k <= t; k++)
    {
        scanf("%d %d", &n, &p);
        memset(dp, -1, sizeof(dp));
        ct0 = ct1 = ct2 = ct3 = 0;
        for(i = 0; i < n; i++)
        {
            scanf("%d", &x);
            switch(x%p)
            {
                case 0:
                ct0++;
                break;
                case 1:
                ct1++;
                break;
                case 2:
                ct2++;
                break;
                case 3:
                ct3++;
                break;
            }
        }
        //printf("%d %d %d %d\n", ct0, ct1, ct2, ct3);
        ct0 += ((ct1+ct2+ct3)? 1: 0);
        ct0 += cnt(ct1, ct2, ct3, 0);
        printf("Case #%d: %d\n", k, ct0);
    }
    return 0;
}
