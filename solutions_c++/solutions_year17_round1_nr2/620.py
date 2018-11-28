#include <stdio.h>
#include <algorithm>
#include <math.h>
#define INF 0x3fffffff

int t;
int n, p;
int r[60], q[60][60];
int loc[60];

int main()
{
    freopen("/Users/IohcEjnim/Desktop/TEMP/B-large.in", "r", stdin);
    freopen("/Users/IohcEjnim/Desktop/TEMP/result.out", "w", stdout);
    int tn, i, j;
    int v, minv, minp, maxv, maxp, ans;
    scanf("%d", &t);
    for (tn = 1; tn <= t; tn++)
    {
        scanf("%d %d", &n, &p);
        for (i = 1; i <= n; i++)
            scanf("%d", &r[i]);
        for (i = 1; i <= n; i++)
            for (j = 1; j <= p; j++)
                scanf("%d", &q[i][j]);
        
        for (i = 1; i <= n; i++)
            std :: sort(q[i]+1, q[i]+p+1);
        for (i = 1; i <= n; i++)
            loc[i] = 1;
        
        ans = 0;
        while (1)
        {
            minv = 0; maxv = INF;
            for (i = 1; i <= n; i++)
            {
                v = (int)(ceil((double)q[i][loc[i]]*10/r[i]/11-0.00000001)+0.1);
                if (v > minv)
                {
                    minv = v;
                    minp = i;
                }
                v = (int)(floor((double)q[i][loc[i]]*10/r[i]/9+0.00000001)+0.1);
                if (v < maxv)
                {
                    maxv = v;
                    maxp = i;
                }
            }
            
            if (minv > maxv)
            {
                if (loc[maxp] == p) break;
                loc[maxp]++;
                continue;
            }
            ans++;
            for (i = 1; i <= n; i++)
            {
                if (loc[i] == p) break;
                loc[i]++;
            }
            if (i != n+1) break;
        }
        
        printf("Case #%d: ", tn);
        printf("%d\n", ans);
    }
}