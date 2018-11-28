#include<bits/stdc++.h>
using namespace std;
int nn[1005], cc[1005], ara[1005], cust[1005], n, m, c, ct;
bool cck(int x)
{
    int i, j, k;
    ct = 0;
    for(i = 1; i <= n; i++)
        ara[i] = x;
    for(i = 1; i <= m; i++)
    {
        if(ara[nn[i]])
            ara[nn[i]]--;
        else
        {
            for(j = nn[i]-1; j > 0 && ara[j] == 0; j--);
            if(!j)
                return false;
            ara[j]--, ct++;
        }
    }
    return true;
}
int main()
{
    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t, k, i, j, p, q, x, y, st, ed, mid;
    cin>>t;
    for(k = 1; k <= t; k++)
    {
        scanf("%d %d %d", &n, &c, &m);
        memset(cust, 0, sizeof(cust));
        for(i = 1; i <= m; i++)
        {
            scanf("%d %d", &nn[i], &cc[i]);
            cust[cc[i]]++;
        }
        y = 0;
        for(i = 1; i <= c; i++)
            y = max(y, cust[i]);
        st = y, ed = m;
        if(cck(st))
        {
            printf("Case #%d: %d %d\n", k, st, ct);
            continue;
        }
        while(st+1 != ed)
        {
            mid = (st+ed)>>1;
            if(cck(mid))
                ed = mid;
            else
                st = mid;
        }
        p = cck(ed);
        //printf("%d\n", p);
        printf("Case #%d: %d %d\n", k, ed, ct);
    }
    return 0;
}
