#include <iostream>
#include <cstdio>
#include <queue>

using namespace std;

typedef long long ll;
typedef long double ld;

const ll INF = 1e15;
int E[1001], S[1001];

ll D[1001][1001];
ld V[1001][1001];

int N, Q;

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for (int Ti = 1; Ti <= T; Ti++) {
        scanf("%d %d", &N, &Q);

        for (int Ni = 0; Ni < N; Ni++)
            scanf("%d %d", &E[Ni], &S[Ni]);

        for (int Ni = 0; Ni < N; Ni++)
            for (int Nj = 0; Nj < N; Nj++) {
                scanf("%lld", &D[Ni][Nj]);
                if ( D[Ni][Nj] == -1 ) D[Ni][Nj] = INF;
            }

        for (int Nk = 0; Nk < N; Nk++)
            for (int Ni = 0; Ni < N; Ni++)
                for (int Nj = 0; Nj < N; Nj++)
                    D[Ni][Nj] = min(D[Ni][Nj], D[Ni][Nk]+D[Nk][Nj]);

        for (int Ni = 0; Ni < N; Ni++)
            for (int Nj = 0; Nj < N; Nj++)
                if ( D[Ni][Nj] <= E[Ni] ) V[Ni][Nj] = (ld)(D[Ni][Nj])/S[Ni];
                else V[Ni][Nj] = INF;

        for (int Nk = 0; Nk < N; Nk++)
            for (int Ni = 0; Ni < N; Ni++)
                for (int Nj = 0; Nj < N; Nj++)
                    V[Ni][Nj] = min(V[Ni][Nj], V[Ni][Nk]+V[Nk][Nj]);

        printf("Case #%d:", Ti);

        for (int Qi = 0; Qi < Q; Qi++) {
            int a, b;
            scanf("%d %d", &a, &b);
            printf(" %.9f", (double)V[a-1][b-1]);
        }

        puts("");
    }
}
