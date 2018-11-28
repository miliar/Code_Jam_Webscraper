#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<queue>
#include<map>
using namespace std;
typedef long long ll;
ll e[110];
double s[110];
ll dis[110][110];
double time[110][110];
int u[110], v[110];

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int cnt;
    cin >> cnt;
    for(int c = 1; c <= cnt; ++c)
    {
        int n, q;
        cin >> n >>q;
        for(int i = 0; i < n; ++i)
            cin >> e[i] >> s[i];
        for(int i = 0; i < n; ++i)
        {
            for(int j = 0; j < n; ++j)
            {
                cin >> dis[i][j];
                time[i][j] = -1;
            }
            dis[i][i] = 0;
            time[i][i] = 0;
        }
        for(int i = 0; i < q; ++i)
            cin >> u[i] >> v[i];
        for(int k = 0; k < n; ++k)
            for(int i = 0; i < n; ++i)
                for(int j = 0; j < n; ++j)
                {
                    if(dis[i][k] != -1 && dis[k][j] != -1 && dis[i][k] + dis[k][j] <= e[i])
                        if(time[i][j] == -1 || (dis[i][k] + dis[k][j]) / s[i] < time[i][j])
                        {
                            dis[i][j] = dis[i][k] + dis[k][j];
                            time[i][j] = dis[i][j] / s[i];
                        }
                }
        for(int k = 0; k < n; ++k)
            for(int i = 0; i < n; ++i)
                for(int j = 0; j < n; ++j)
                {
                    if(time[i][k] != -1 && time[k][j] != -1)
                    {
                        if(time[i][j] == -1)
                            time[i][j] = time[i][k] + time[k][j];
                        else
                            time[i][j] = min(time[i][j], time[i][k] + time[k][j]);
                    }
                }
        printf("Case #%d:", c);
        for(int i = 0; i < q; ++i)
            printf(" %.7lf", time[u[i] - 1][v[i] - 1]);
        printf("\n");
    }
    return 0;
}
