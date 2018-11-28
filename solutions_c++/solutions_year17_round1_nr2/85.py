#include <bits/stdc++.h>
using namespace std;

const int MAXN = 50, MAXP = 50, MAXV = 1050;

int N, P;
int R[MAXN];
pair<int, int> Q[MAXN][MAXP];

bool mark[MAXV];
int F[MAXV][MAXV], C[MAXV][MAXV];

void add_edge(int u, int v, int c1, int c2)
{
    C[u][v] = c1; C[v][u] = c2;
    F[u][v] = F[v][u] = 0;
}

bool dfs(int u, int end)
{
    mark[u] = true;
    if (u == end) return true;

    for (int v = 0; v <= end; ++v)
        if (C[u][v] > F[u][v] && !mark[v] && dfs(v, end)) {
            ++F[u][v]; --F[v][u];
            return true;
        }

    return false;
}

int main()
{
    int T; scanf("%d", &T);
    for (int t = 0; t < T; ++t) {
        scanf("%d%d", &N, &P);
        for (int i = 0; i < N; ++i)
            scanf("%d", &R[i]);

        for (int i = 0; i < N; ++i)
            for (int j = 0; j < P; ++j) {
                int tmp; scanf("%d", &tmp);
                Q[i][j] = {(10*tmp-1)/(11*R[i]) + 1, (10*tmp)/(9*R[i])};
                if (Q[i][j].first <= 0) Q[i][j].first = 1;
            }

        memset(F, 0, sizeof(F));
        memset(C, 0, sizeof(C));

        for (int j = 0; j < P; ++j)
            if (Q[0][j].first <= Q[0][j].second)
                add_edge(P*N, j, 1, 0);

        for (int j = 0; j < P; ++j)
            if (Q[N-1][j].first <= Q[N-1][j].second)
                add_edge(P*(N-1)+j, P*N+1, 1, 0);

        for (int i = 0; i < N-1; ++i)
            for (int j1 = 0; j1 < P; ++j1)
                for (int j2 = 0; j2 < P; ++j2) {
                    int L = max(Q[i][j1].first, Q[i+1][j2].first);
                    int R = min(Q[i][j1].second, Q[i+1][j2].second);

                    if (L <= R)
                        add_edge(P*i+j1, P*(i+1)+j2, 1, 0);
                }

        int answer = 0;
        while (true) {
            memset(mark, 0, sizeof(mark));
            if (!dfs(P*N, P*N+1)) break;
            ++answer;
        }

        printf("Case #%d: %d\n", t+1, answer);
    }

    return 0;
}
