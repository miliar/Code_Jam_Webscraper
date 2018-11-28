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
    int N, P;
    scanf("%d%d", &N, &P);
    fprintf(stderr, "%d %d\n", N, P);
    int f[P] = {};
    for (int i = 0; i < N; ++i) {
        int G;
        scanf("%d", &G);
        ++f[G % P];
    }
    int ans = f[0], x;
    switch (P) {
    case 2:
        ans += (f[1]+1)/2;
        break;
    case 3:
        x = min(f[1], f[2]);
        ans += x;
        f[1] -= x;
        f[2] -= x;
        ans += (f[1]+f[2]+2)/3;
        break;
    case 4:
        x = min(f[1], f[3]);
        ans += x;
        f[1] -= x;
        f[3] -= x;
        x = f[2]/2;
        ans += x;
        f[2] -= 2*x;
        ans += (f[1]+f[3]+2*f[2] + 3) / 4;
        break;
    default:
        assert(0);
    }
    printf("Case #%d: %d\n", CC, ans);
}

int main(void) {
    init();
    for (int i = 1; i <= CASES; ++i) solve(i);
    return 0;
}
