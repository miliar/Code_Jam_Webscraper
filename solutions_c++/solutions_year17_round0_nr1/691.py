#include<iostream>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<fstream>
using namespace std;
char s[1010];
int k, a[1010], flg[1010], n;
int solve()
{
    int i, sum = 0, cnt = 0;
    memset(flg, 0, sizeof(flg));
    for(i=0;i<n-k+1;i++)
    {
        if(i-k>=0)
            sum -= flg[i-k];
        if(a[i] == 0 && sum%2 == 0)
        {
            flg[i] = 1;
            sum += flg[i];
            cnt++;
        }
        else if(a[i] == 1 && sum % 2 == 1)
        {
            flg[i] = 1;
            sum += flg[i];
            cnt++;
        }
    }
    for(i;i<n;i++)
    {
        if(i-k>=0)
            sum -= flg[i-k];
        if(sum % 2 == 0 && a[i] == 0)   return -1;
        else if(sum % 2 == 1 && a[i] == 1)  return -1;
    }
    return cnt;
}
int main()
{
    freopen("G:\\A.in", "r", stdin);
    freopen("G:\\A.out", "w", stdout);
    int T;
    scanf("%d",&T);
    for(int ica=1;ica<=T;ica++)
    {
        scanf(" %s %d",s, &k);
        n = strlen(s);
        for(int i=0;i<n;i++)
            a[i] = s[i] == '+' ? 1 : 0;
        int ans = solve();
        if(ans == -1)
            printf("Case #%d: IMPOSSIBLE\n", ica);
        else
            printf("Case #%d: %d\n", ica, ans);
    }
}