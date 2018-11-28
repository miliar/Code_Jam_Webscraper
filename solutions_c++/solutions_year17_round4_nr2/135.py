#include <bits/stdc++.h>
using namespace std;

bool debug = false;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<pii> vpii;
typedef map<string, int> msi;
typedef set<string> ss;
typedef set<pii> spii;

const double pi = 2.0*acos(0.0);

int CASES;

void init() {
    assert(scanf("%d", &CASES) == 1);
}

int dprintf(const char *err, ...) {
    if (debug) {
        va_list pvar;
        va_start(pvar, err);
        return vfprintf(stderr, err, pvar);
    }
    return 0;
}


void solve(int CC) {
    int N, C, M;
    scanf("%d%d%d", &C, &N, &M);
    vector<int> P(M), B(M);
    vector<vi> PS(C+1, vi(N+1, 0));
    for (int i = 0; i < M; ++i) {
        scanf("%d%d", &P[i], &B[i]);
        ++PS[P[i]][B[i]];
        ++PS[P[i]][0];
    }
    vector<int> NZ(C+1);
    int lb = 0;
    for (int i = 1; i <= C; ++i) {
        NZ[i] = PS[i][0];
        for (int j = 0; j <= N; ++j) {
            PS[i][j] += PS[i-1][j];
            if (!j) {
                lb = max(lb, (PS[i][j] + i-1) / i);
            }
        }
    }
    for (int j = 1; j <= N; ++j)
        lb = max(lb, PS[C][j]);

    int tot = PS[C][0], sat = 0;
    for (int i = 1; i <= C; ++i) {
        sat += min(lb, NZ[i]);
    }

    printf("Case #%d: %d %d\n", CC, lb, tot-sat);
}

int main(void) {
    init();
    for (int i = 1; i <= CASES; ++i) solve(i);
    return 0;
}
