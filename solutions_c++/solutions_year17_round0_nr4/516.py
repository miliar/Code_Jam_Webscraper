#include <cstdio>
#include <algorithm>

using namespace std;

typedef pair<int, int> ii;
typedef pair<char, ii> chii;

const int MAXN = 1e3 + 5;

int TC, tc;
int N, R, a, b;
char c;
char M[MAXN][MAXN];
int K;
chii v[MAXN * 4];

int main() {
    freopen("i.in", "r", stdin);
    freopen("o.out", "w", stdout);
    scanf("%d", &TC);
    while(TC--) {
        scanf("%d%d", &N, &R);

        for(int i = 1; i <= N; i++)
            for(int j = 1; j <= N; j++)
                M[i][j] = '.';
        for(int i = 1; i <= N; i++)
            M[i][N + 1] = 0;
        K = 0;

        for(int i = 0; i < R; i++) {
            scanf("\n%c%d%d", &c, &a, &b);
            M[a][b] = c;
        }

        int ch = 1;
        for(int i = 1; i <= N; i++)
            if(M[1][i] == 'x' || M[1][i] == 'o')
                ch = i;
        if(M[1][ch] != 'o') {
            v[K++] = chii('o', ii(1, ch));
            M[1][ch] = 'o';
        }

        for(int i = 1; i <= N; i++)
            if(M[1][i] == '.') {
                v[K++] = chii('+', ii(1, i));
                M[1][i] = '+';
            }

        if(N >= 2) {
            int u = 2;
            ch++;
            if(ch == N + 1) ch = 1;
            while(u < N) {
                v[K++] = chii('x', ii(u, ch));
                M[u][ch] = 'x';
                u++;
                ch++;
                if(ch == N + 1) ch = 1;
            }

            for(int i = 2; i < N; i++)
                if(i != ch) {
                    v[K++] = chii('+', ii(N, i));
                    M[N][i] = '+';
                } else {
                    v[K++] = chii('o', ii(N, i));
                    M[N][i] = 'o';
                }
            if(ch == 1 || ch == N) {
                v[K++] = chii('x', ii(N, ch));
                M[N][ch] = 'x';
            }
        }
        printf("Case #%d: %d %d\n", ++tc, N == 1 ? 2 : 3 * N - 2, K);
        for(int i = 0; i < K; i++)
            printf("%c %d %d\n", v[i].first, v[i].second.first, v[i].second.second);
    }
}
