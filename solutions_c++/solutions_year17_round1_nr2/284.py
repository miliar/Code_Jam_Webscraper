// Bipartite matching
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;

/* #define debug printf */
#define debug(...)
typedef unsigned long long ull;
typedef pair<int, int> pii;

int N, P;

int R[50];
int Q[50][50];

vector<pii> S[50];

bool empty(pii a) {
    return a.first > a.second;
}

pii merge(pii a, pii b) {
    if (empty(a)) return a;
    if (empty(b)) return b;
    return {max(a.first, b.first), min(a.second, b.second)};
}

void solve(int T) {
    scanf("%d%d", &N, &P);
    for (int j = 0; j < N; j++)
        scanf("%d", &R[j]);
    for (int i = 0; i < N; i++)
        for (int j = 0; j < P; j++)
            scanf("%d", &Q[i][j]);

    for (int i = 0; i < N; i++) {
        S[i].clear();
        for (int j = 0; j < P; j++) {
            int kl = ceil(Q[i][j] * 1.0 / R[i] / 1.1 - 1e-9);
            int ku = floor(Q[i][j] * 1.0 / R[i] / 0.9 + 1e-9);
            debug("R: %d Q: %d Range: [%d, %d]\n", R[i], Q[i][j], kl, ku);
            if (kl > ku)
                continue;
            S[i].push_back({kl, ku});
        }
        sort(S[i].begin(), S[i].end());
    }

    int total = 0;

    int at[50] = {0};

    bool done = false;

    for (int i = 0; i < N; i++)
        if (!S[i].size())
            done = true;

    while (!done) {
        int minu = S[0][at[0]].second;
        pii seg = S[0][at[0]];
        for (int i = 1; i < N; i++) {
            pii sego = seg; (void) sego;
            seg = merge(seg, S[i][at[i]]);
            debug("[%d %d] * [%d %d] = [%d %d]\n", sego.first, sego.second, S[i][at[i]].first, S[i][at[i]].second, seg.first, seg.second);
            minu = min(minu, S[i][at[i]].second);
        }
        if (!empty(seg)) {
            total += 1;
            for (int i = 0; i < N; i++) {
                debug("Using %d/%d\n", i, at[i]);
                if (++at[i] == (int) S[i].size())
                    done = true;
            }
        } else {
            for (int i = 0; i < N; i++) {
                if (S[i][at[i]].second == minu) {
                    debug("Discarding %d/%d\n", i, at[i]);
                    if (++at[i] == (int) S[i].size())
                        done = true;
                }
            }
        }
    }

    printf("Case #%d: %d\n", T, total);
}

int main() {
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; t++)
        solve(t);
    return 0;
}
