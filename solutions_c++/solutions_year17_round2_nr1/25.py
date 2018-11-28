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


void solve(int P) {
    ll D, N;
    scanf("%lld%lld", &D, &N);
    pair<ll, ll> H[N];
    double v = 1e30;
    for (int i = 0; i < N; ++i) {
        ll K, S;
        scanf("%lld%lld", &K, &S);
        v = min(v, 1.0*D/(D-K)*S);
    }
	printf("Case #%d: %.9lf\n", P, v);
}

int main(void) {
	init();
	for (int i = 1; i <= CASES; ++i) solve(i);
	return 0;
}
