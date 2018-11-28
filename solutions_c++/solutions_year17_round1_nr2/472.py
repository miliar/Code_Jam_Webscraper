#include <bits/stdc++.h>
using namespace std;
int w[105];
int g[105][105];
multiset <int> s[55];
int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int cas, C = 1;
    scanf("%d", &cas);
    while(cas--)
    {
        for(int i = 0; i < 55; i++)
            s[i].clear();
        int n, p;
        scanf("%d %d", &n, &p);
        for(int i = 0; i < n; i++)
            scanf("%d", &w[i]);
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < p; j++)
            {
                scanf("%d", &g[i][j]);
                s[i].insert(g[i][j]);
            }
        }
        int ans = 0;
        int l = 0;
        for(int i = 0; i < p; i++)
            for(int j = 0; j < n; j++)
                l = max(l, g[j][i] / (int)(ceil((double)w[j] * 0.9)));
        for(int i = 1; i <= l; i++)
        {
            while(1)
            {
                int flag = 0;
                for(int j = 0; j < n; j++)
                {
                    int low = (int)(ceil((double)w[j] * i * 0.9));
                    int high = (int)(floor((double)w[j] * i * 1.1));
                    set <int>::iterator it = lower_bound(s[j].begin(), s[j].end(), low);
                    if(it == s[j].end() || *it > high)
                    {
                        flag = 1;
                        break;
                    }
                }
                if(flag)
                    break;
                else
                {
                    for(int j = 0; j < n; j++)
                    {
                        int low = (int)(ceil((double)w[j] * i * 0.9));
                        int high = (int)(floor((double)w[j] * i * 1.1));
                        set <int>::iterator it = lower_bound(s[j].begin(), s[j].end(), low);
                        s[j].erase(it);
                    }
                    ans++;
                }
            }
        }
        printf("Case #%d: ", C++);
        printf("%d\n", ans);
    }
    return 0;
}
