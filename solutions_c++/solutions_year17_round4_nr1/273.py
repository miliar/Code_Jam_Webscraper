#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair < int, int > PII;

int dp[101][101][101][101];
int il[4], n, p;

int count(int a0, int a1, int a2, int a3)
{
    if(dp[a0][a1][a2][a3] != 0) return dp[a0][a1][a2][a3];
    int res = 0;
    if(a0 > 0)
    {
        int ans = count(a0 - 1, a1, a2, a3);
        int ile = (a1 + 2 * a2 + 3 * a3) % p;
        if(ile == 0) ans++;
        res = max(res, ans);
    }
    if(a1 > 0)
    {
        int ans = count(a0, a1 - 1, a2, a3);
        int ile = (a1 - 1 + 2 * a2 + 3 * a3) % p;
        if(ile == 0) ans++;
        res = max(res, ans);
    }
    if(a2 > 0)
    {
        int ans = count(a0, a1, a2 - 1, a3);
        int ile = (a1 + 2 * (a2 - 1) + 3 * a3) % p;
        if(ile == 0) ans++;
        res = max(res, ans);
    }
    if(a3 > 0)
    {
        int ans = count(a0, a1, a2, a3 - 1);
        int ile = (a1 + 2 * a2 + 3 * (a3 - 1)) % p;
        if(ile == 0) ans++;
        res = max(res, ans);
    }
    return dp[a0][a1][a2][a3] = res;
}

int main()
{
    int te; scanf("%d", &te);
    for(int t = 1; t <= te; t++)
    {
        scanf("%d%d", &n, &p);
        il[0] = il[1] = il[2] = il[3] = 0;
        for(int i = 1; i <= n; i++)
        {
            int x; scanf("%d", &x);
            il[x % p]++;
        }
        int ans = count(il[0], il[1], il[2], il[3]);
        printf("Case #%d: ", t);
        printf("%d\n", ans);
        for(int i = 0; i <= il[0]; i++)
            for(int j = 0; j <= il[1]; j++)
                for(int k = 0; k <= il[2]; k++)
                    for(int l = 0; l <= il[3]; l++)
                        dp[i][j][k][l] = 0;
    }
    return 0;
}
