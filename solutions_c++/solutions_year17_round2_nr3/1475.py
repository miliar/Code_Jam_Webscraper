#include<iostream>
#include<cstdio>
#include<algorithm>
#include<limits>


using namespace std;

const int MAX_N = 100;
const long long INF = 1e15;
const double dINF = numeric_limits<double>::infinity();

long long G[MAX_N][MAX_N];
pair<long long, double> horse[MAX_N];

double dp[MAX_N][MAX_N];

int main(void)
{
    int T;  cin >> T;

    for (int t = 1; t <= T; t ++)
    {
        int N, Q;
        scanf("%d %d", &N, &Q);

        for (int i = 0; i < N; i ++)
        {
            scanf("%lld %lf", &horse[i].first, &horse[i].second);
            fill(dp[i], dp[i] + N, dINF);
            dp[i][i] = 0;
        }

        long long v1, v2;

        for (int i = 0; i < N; i ++)
        {
            for (int j = 0; j < N; j ++)
            {
                scanf("%lld", &v1);

                if (v1 == -1)
                    G[i][j] = INF;
                else
                    G[i][j] = v1;
            }

            G[i][i] = 0;
        }

        for (int k = 0; k < N; k ++)
            for (int i = 0; i < N; i ++)
                for (int j = 0; j < N; j ++)
                    G[i][j] = min(G[i][j], G[i][k] + G[k][j]);
            

        for (int k = 0; k < N; k ++)
            for (int i = 0; i < N; i ++)
                for (int j = 0; j < N; j ++)
                    if (G[k][j] <= horse[k].first)
                        dp[i][j] = min(dp[i][j], dp[i][k] + (G[k][j] / horse[k].second));

        printf("Case #%d: ",t);
        for (int i = 0; i < Q; i ++)
        {
            scanf("%lld %lld", &v1, &v2);
            v1--, v2--;
            printf("%.7lf ", dp[v1][v2]);
        }
        printf("\n");


    }
}
