#include <bits/stdc++.h>
using namespace std;
char g[105][105];
int emp[105];
int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int cas, C = 1;
    scanf("%d", &cas);
    while(cas--)
    {
        int n, m;
        scanf("%d %d", &n, &m);
        for(int i = 0; i < n; i++)
        {
            scanf("%s", g[i]);
        }
        memset(emp, 0 ,sizeof(emp));
        for(int i = 0; i < n; i++)
        {
            int f = 0;
            while(g[i][f] == '?')
                f++;
            if(f == m)
            {
                emp[i] = 1;
            }
            else
            {
                for(int j = 0; j < f; j++)
                    g[i][j] = g[i][f];
                char tmp = g[i][f];
                for(int j = f + 1; j < m; j++)
                {
                    if(g[i][j] == '?')
                        g[i][j] = tmp;
                    else
                        tmp = g[i][j];
                }
            }
        }
        int e = 0;
        while(emp[e] == 1)
            e++;
        int tmp = e;
        for(int i = 0; i < e; i++)
            strcpy(g[i], g[e]);
        for(int i = e + 1; i < n; i++)
        {
            if(emp[i] == 1)
                strcpy(g[i], g[tmp]);
            else
                tmp = i;
        }
        printf("Case #%d:\n", C++);
        for(int i = 0; i < n; i++)
            puts(g[i]);
    }
    return 0;
}
