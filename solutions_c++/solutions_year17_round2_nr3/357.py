#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 105;
const double eps = 1e-10;

int n, Q;
long long dis[N][N], E[N];
double s[N], t[N][N];

int main()
{
    int T;
    scanf("%d", &T);
    for(int Case = 1; Case <= T; ++Case)
    {
        scanf("%d%d", &n, &Q);
        for(int i = 1; i <= n; ++i) scanf("%lld%lf", &E[i], &s[i]);
        for(int i = 1; i <= n; ++i)
            for(int j = 1; j <= n; ++j)
                scanf("%lld", &dis[i][j]);
        
        for(int k = 1; k <= n; ++k)
            for(int i = 1; i <= n; ++i)
                for(int j = 1; j <= n; ++j)
                    if(i != k && j != k && dis[i][k] >= 0 && dis[k][j] >= 0)
                    {
                        long long cur = dis[i][k] + dis[k][j];
                        if(cur < dis[i][j] || dis[i][j] < 0) dis[i][j] = cur;
                    }
        /*
        for(int i = 1; i <= n; ++i)
        {
            for(int j = 1; j <= n; ++j)
                printf("%lld ", dis[i][j]);
        puts("");
        }
        */
        for(int i = 1; i <= n; ++i)
        {
            for(int j = 1; j <= n; ++j)
                if(j != i)
                {
                    if(dis[i][j] > -eps)
                    {
                        if(dis[i][j] <= E[i])
                            t[i][j] = (double)dis[i][j] / (double)s[i];
                        else
                            t[i][j] = -1;
                    }
                    else t[i][j] = -1;
                }
        }
        /*
        for(int i = 1; i <= n; ++i)
        {
            for(int j = 1; j <= n; ++j)
                printf("%.6f ", t[i][j]);
            puts("");
        }
        */
        for(int k = 1; k <= n; ++k)
            for(int i = 1; i <= n; ++i)
                for(int j = 1; j <= n; ++j)
                    if(i != k && j != k && t[i][k] > -eps && t[k][j] > -eps)
                    {
                        double cur = t[i][k] + t[k][j];
                        if(cur < t[i][j] || t[i][j] < 0) t[i][j] = cur;
                    }
        /*
        for(int i = 1; i <= n; ++i)
        {
            for(int j = 1; j <= n; ++j)
                printf("%.6f ", t[i][j]);
            puts("");
        }
        */
        printf("Case #%d: ", Case);
        for(int q = 1; q <= Q; ++q)
        {
            int x, y;
            scanf("%d%d", &x, &y);
            printf(" %.6f", t[x][y]);
        }
        puts("");
    }
    
    return 0;
}
