#include<bits/stdc++.h>
using namespace std;
int ara[3], o, g, v;
char col[] = "RYB", str[1005];
int main()
{
    //freopen("B-small-attempt1.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t, k, n, i, j, p, q, x, y;
    scanf("%d", &t);
    for(k = 1; k <= t; k++)
    {
        scanf("%d", &n);
        scanf("%d %d %d %d %d %d", &ara[0], &o, &ara[1], &g, &ara[2], &v);
        if(ara[0])
            p = 0, str[0] = col[0], ara[0]--;
        else if(ara[1])
            p = 1, str[0] = col[1], ara[1]--;
        else
            p = 2, str[0] = col[2], ara[2]--;
        q = p;
        for(i = 1; i < n; i++)
        {
            if(p != q)
                x = ara[q], y = q;
            else
                x = -1;
            for(j = 0; j < 3; j++)
            {
                if(j == p)
                    continue;
                if(ara[j] > x)
                    x = ara[j], y = j;
            }
            if(!x)
                break;
            else
                ara[y]--, str[i] = col[y], p = y;
        }
        str[i] = '\0';
        if(i == n && str[0] != str[n-1])
            printf("Case #%d: %s\n", k, str);
        else
            printf("Case #%d: IMPOSSIBLE\n", k);
    }
    return 0;
}
