#include <bits/stdc++.h>
using namespace std;

const int MAXN = 105;
const long long INF = 1ll << 61;

int E[MAXN], S[MAXN];
long long G[MAXN][MAXN];
double ans[MAXN][MAXN];
queue<int>q;
double d[MAXN];
double spfa(int s, int t, int n)
{
    for(int i = 1; i <= n; i++)
        d[i] = 1e100;
    q.push(s);
    d[s] = 0;
    while(!q.empty())
    {
        s = q.front();
        for(int i = 1; i <= n; i++)
        {
            double use = 1.0 * G[s][i] / S[s];
            if(G[s][i] <= E[s] && d[i] > d[s] + use)
            {
                d[i] = d[s] + use;
                q.push(i);
            }
        }
        q.pop();
    }
    return d[t];
}
int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int t;
    cin >> t;
    for(int cas = 1; cas <= t; cas++)
    {
        int n, q;
        cin >> n >> q;
        for(int i = 1; i <= n; i++)
        {
            cin >> E[i] >> S[i];
        }
        for(int i = 1; i <= n; i++)
            for(int j = 1; j <= n; j++)
                cin >> G[i][j];
        for(int i = 1; i <= n; i++)
            for(int j = 1; j <= n; j++)
                if(G[i][j] == -1)
                    G[i][j] = INF;
        for(int k = 1; k <= n; k++)
            for(int i = 1; i <= n; i++)
                for(int j = 1; j <= n; j++)
                    G[i][j] = min(G[i][j], G[i][k] + G[k][j]);
        for(int i = 1; i <= n; i++)
            for(int j = 1; j <= n; j++)
                ans[i][j] = 1e100;
        printf("Case #%d:", cas);
        while(q--)
        {
            int s, t;
            cin >> s >> t;
            printf(" %.8f", spfa(s, t, n));
        }
        printf("\n");
    }
    return 0;
}

