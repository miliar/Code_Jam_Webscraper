#include<bits/stdc++.h>
using namespace std;
#define PI acos(-1)
double dp[1005][1005];
int n, k;
struct pan
{
    double rr, hh;
}ara[1005];
bool cmp(pan a, pan b)
{
    if(a.rr != b.rr)
        return a.rr > b.rr;
    return a.hh > b.hh;
}
double cnt(int i, int taken)
{
    double p;
    if(taken > k)
        return -1000000000000000LL;
    if(i == n)
        return (taken == k)? 0: -1000000000000000LL;
    if(dp[i][taken] > -.5 || dp[i][taken] < -10)
        return dp[i][taken];
    p = taken? 0: PI*ara[i].rr*ara[i].rr;
    dp[i][taken] = max(cnt(i+1, taken+1)+p+2*PI*ara[i].rr*ara[i].hh, cnt(i+1, taken));
    return dp[i][taken];
}
int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int i, j, p, q, x, y, t, tt;
    scanf("%d", &t);
    for(tt = 1; tt <= t; tt++)
    {
        scanf("%d %d", &n, &k);
        for(i = 0; i < n; i++)
            scanf("%lf %lf", &ara[i].rr, &ara[i].hh);
        sort(ara, ara+n, cmp);
        for(i = 0; i < 1005; i++)
        {
            for(j = 0; j < 1005; j++)
                dp[i][j] = -1.0;
        }
        printf("Case #%d: %.10lf\n", tt, cnt(0, 0));
    }
    return 0;
}
