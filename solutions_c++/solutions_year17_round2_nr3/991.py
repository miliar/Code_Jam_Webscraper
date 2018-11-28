#include <bits/stdc++.h>
using namespace std;

const int maxN = 101;
const long long INF = 1000000000000LL;  // 10^12

long long G1[maxN][maxN];
int maxDist[maxN], vel[maxN];
long double G2[maxN][maxN];

int main()
{
    int t;
    scanf ("%d", &t);

    for (int test=1; test<=t; test++)
    {
        int n, q;
        scanf ("%d%d", &n, &q);

        for (int i=1; i<=n; i++)
            scanf ("%d%d", maxDist + i, vel + i);

        for (int i=1; i<=n; i++)
        {
            for (int j=1; j<=n; j++)
            {
                scanf ("%lld", &G1[i][j]);
                if (G1[i][j] == -1)
                    G1[i][j] = INF;
            }
        }

        for (int k=1; k<=n; k++)
            for (int i=1; i<=n; i++)
                for (int j=1; j<=n; j++)
                    G1[i][j] = min(G1[i][j], G1[i][k] + G1[k][j]);
        
        for (int i=1; i<=n; i++)
            for (int j=1; j<=n; j++)
                G2[i][j] = maxDist[i] < G1[i][j] ? INF : (long double)G1[i][j] / vel[i];

        for (int k=1; k<=n; k++)
            for (int i=1; i<=n; i++)
                for (int j=1; j<=n; j++)
                    G2[i][j] = min(G2[i][j], G2[i][k] + G2[k][j]);

        printf("Case #%d: ", test);

        while (q--)
        {
            int a, b;
            scanf ("%d%d", &a, &b);
            printf("%.8Lf ", G2[a][b]);
        }
        
        printf("\n");
    }
    
    return 0;
}