#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

using ll = long long;

int T;
int N, P;
int R[64];
int Q[64][64];
int l[64][64];
int r[64][64];
int idx[64];

int celldiv(int a, int b) {
    return (a + b - 1) / b;
}

int floordiv(int a, int b) {
    return a / b;
}

int main() {
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);
        scanf("%d%d", &N, &P);
        for (int i = 0; i < N; ++i)
            scanf("%d", R + i);
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < P; ++j)
                scanf("%d", Q[i] + j);
            sort(Q[i], Q[i] + P);
            for (int j = 0; j < P; ++j) {
                l[i][j] = celldiv(Q[i][j] * 10, R[i] * 11);
                r[i][j] = floordiv(Q[i][j] * 10, R[i] * 9);
            }
        }
        memset(idx, 0, sizeof(idx));
        int ans = 0;
        for (int c = 1; ;) {
            bool can = true;
            bool over = false;
            for (int i = 0; i < N; ++i) {
                while (idx[i] < P && r[i][idx[i]] < c) ++ idx[i];
                if (idx[i] == P) {
                    over = true;
                    can = false;
                    break;
                }
                if (l[i][idx[i]] > c) {
                    c = l[i][idx[i]];
                    can = false;
                    break;
                }
            }
            if (over)
                break;
            if (can) {
                ans ++;
                for (int i = 0; i < N; ++i)
                    idx[i]++;
            }
        }
        printf("%d\n", ans);
    }
    return 0;
}