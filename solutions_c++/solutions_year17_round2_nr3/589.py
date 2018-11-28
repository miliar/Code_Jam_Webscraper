#include "iostream"
#include "cstdio"
#include "cstdlib"
#include "string.h"
#include "vector"
#include "map"
#include "algorithm"
#include "queue"

#define ll long long
#define ull unsigned long long


ll G[105][105];

int H[105][2];

double ans[105][105];

int n;
bool shouldVis[105];

void Dijkstra(int st)
{
    std::queue<int> que;
    for (int i = 1; i <= n; i++)
        ans[st][i] = 1000000000000000000;
    memset(shouldVis, 0, sizeof(shouldVis));
    ans[st][st] = 0.0;
    que.push(st);
    while (!que.empty())
    {
        int u = que.front();
        que.pop();
        shouldVis[u] = false;
        for (int i = 1; i <= n; i++)
        {
            if (G[u][i] > H[u][0]) continue;
            double tmp = 1.0 * G[u][i] / H[u][1];
            if (ans[st][i] > tmp + ans[st][u])
            {
                ans[st][i] = tmp + ans[st][u];
                if (!shouldVis[i])
                {
                    shouldVis[i] = true;
                    que.push(i);
                }
            }
        }
    }
}

int main()
{
    freopen("C-large (1).in", "r", stdin);
    freopen("output.txt", "w", stdout);
	int T, cas = 0;
	scanf("%d", &T);
	while(T--)
	{
        cas++;
        memset(G, -1, sizeof(G));
        int q;
        scanf("%d%d", &n, &q);
        for (int i = 1; i <= n; i++)
        {
            scanf("%d%d", &H[i][0], &H[i][1]);
        }
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
            {
                scanf("%lld", &G[i][j]);
                if (G[i][j] == -1) G[i][j] = 1000000000000000000;
            }
        for (int k = 1; k <= n; k++)
            for (int i = 1; i <= n; i++)
                for (int j = 1; j <= n; j++)
                    G[i][j] = std::min(G[i][j], G[i][k] + G[k][j]);
        for (int i = 1; i <= n; i++)
            Dijkstra(i);
        printf("Case #%d:", cas);
        while (q--)
        {
            int st, ed;
            scanf("%d%d", &st, &ed);
            printf(" %.12lf", ans[st][ed]);
        }
        printf("\n");
	}
	return true;
}
