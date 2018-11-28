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
const ll oo = 1LL<<50;
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


void solve(int P) {
    int N, Q;
    scanf("%d%d", &N, &Q);
    ll E[N], S[N];
    ll D[N][N];
    for (int i = 0; i < N; ++i)
        scanf("%lld%lld", E+i, S+i);
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            scanf("%lld", D[i]+j);
            if (D[i][j] == -1)
                D[i][j] = oo;
        }
        D[i][i] = 0;
    }
    for (int k = 0; k < N; ++k)
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                D[i][j] = min(D[i][j], D[i][k] + D[k][j]);

	printf("Case #%d:", P);
    double mintime[N];
    while (Q--) {
        int u, v;
        scanf("%d%d", &u, &v);
        --u; --v;
        set<int> curr;
        for (int i = 0; i < N; ++i)
            mintime[i] = oo;
        mintime[v] = 0;
        curr.insert(v);
        while (true) {
            bool done = true;
            for (auto j: curr) {
                for (int i = 0; i < N; ++i) {
                    if (D[i][j] > E[i]) continue;
                    double t = 1.0*D[i][j]/S[i] + mintime[j];
                    if (t < mintime[i] - 1e-9) {
                        mintime[i] = t;
                        curr.insert(i);
                        done = false;
                    }
                }
                curr.erase(j);
            }
            if (done) break;
        }
        printf(" %.9lf", mintime[u]);
    }
    printf("\n");
}

int main(void) {
	init();
	for (int i = 1; i <= CASES; ++i) solve(i);
	return 0;
}
