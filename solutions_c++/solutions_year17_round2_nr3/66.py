#include <cstdio>
#include <algorithm>

int main()
{
    int T;
    scanf("%d", &T);
    for (int tt = 1; tt <= T; tt++)
    {
        int N, Q;
        scanf("%d%d", &N, &Q);
        int E[100], S[100];
        for (int i = 0; i < N; i++)
            scanf("%d%d", E+i, S+i);
        int D[100][100];
        for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
        {
            scanf("%d", &D[i][j]);
            if (D[i][j] == -1)
                D[i][j] = 1000000001;
        }
        for (int i = 0; i < N; i++)
            D[i][i] = 0;
        for (int k = 0; k < N; k++)
        for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
        {
            D[i][j] = std::min(D[i][j], D[i][k] + D[k][j]);
        }
        double t[100][100];
        for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
        {
            t[i][j] = 1e100;
            if (E[i] >= D[i][j])
            {
                t[i][j] = 1.0 * D[i][j] / S[i];
            }
        }
        for (int k = 0; k < N; k++)
        for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
        {
            t[i][j] = std::min(t[i][j], t[i][k] + t[k][j]);
        }
        printf("Case #%d:", tt);
        for (int i = 0; i < Q; i++)
        {
            int U, V;
            scanf("%d%d", &U, &V);
            printf(" %.9f", t[U-1][V-1]);
        }
        puts("");
    }
}
