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
double Time[110][110];
int u[110], v[110];


int main()
{
    int T;
    cin >> T;
    for(int cas = 1; cas <= T; ++cas)
    {
        int n, q;
        cin >> n >> q;
        for(int i = 0; i < n; ++i)
            cin >> e[i] >> s[i];
        for(int i = 0; i < n; ++i)
        {
            for(int j = 0; j < n; ++j)
            {
                cin >> dis[i][j];
                Time[i][j] = -1;
            }
            dis[i][i] = 0;
            Time[i][i] = 0;
        }
        for(int i = 0; i < q; ++i)
            cin >> u[i] >> v[i];
        for(int k = 0; k < n; ++k)
            for(int i = 0; i < n; ++i)
                for(int j = 0; j < n; ++j)
                {
                    if(dis[i][k] != -1 && dis[k][j] != -1 && dis[i][k] + dis[k][j] <= e[i])
                        if(Time[i][j] == -1 || (dis[i][k] + dis[k][j]) / s[i] < Time[i][j])
                        {
                            dis[i][j] = dis[i][k] + dis[k][j];
                            Time[i][j] = dis[i][j] / s[i];
                        }
                }
        for(int k = 0; k < n; ++k)
            for(int i = 0; i < n; ++i)
                for(int j = 0; j < n; ++j)
                {
                    if(Time[i][k] != -1 && Time[k][j] != -1)
                    {
                        if(Time[i][j] == -1)
                            Time[i][j] = Time[i][k] + Time[k][j];
                        else
                            Time[i][j] = min(Time[i][j], Time[i][k] + Time[k][j]);
                    }
                }
        printf("Case #%d:", cas);
        for(int i = 0; i < q; ++i)
            printf(" %.7lf", Time[u[i] - 1][v[i] - 1]);
        printf("\n");
    }
    return 0;
}