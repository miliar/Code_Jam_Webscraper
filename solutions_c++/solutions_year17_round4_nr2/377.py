#include <bits/stdc++.h>
using namespace std;

const int MAXN = 2000, MAXC = 2000;

int N, C, M;
int nR[MAXN], nC[MAXC];

int calc(int r)
{
    int f = 0, res = 0;
    for (int i = 0; i < N; ++i) {
        if (nR[i] > r) {
            if (nR[i]-r > f) return -1;
            f -= nR[i]-r;
            res += nR[i]-r;
        } else {
            f += r-nR[i];
        }
    }

    return res;
}

int main()
{
    int T; scanf("%d", &T);
    for (int t = 0; t < T; ++t) {
        scanf("%d%d%d", &N, &C, &M);

        fill(nR, nR+N, 0);
        fill(nC, nC+C, 0);

        for (int i = 0; i < M; ++i) {
            int P, B;
            scanf("%d%d", &P, &B);
            ++nC[B-1];
            ++nR[P-1];
        }

        for (int r = *max_element(nC, nC+C); r <= M; ++r) {
            int q = calc(r);
            if (q != -1) {
                printf("Case #%d: %d %d\n", t+1, r, q);
                break;
            }
        }

    }

    return 0;
}
