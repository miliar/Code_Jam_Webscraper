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

const char *sym = "ROYGBV";

string doit(int N, int *F) {
    for (int i = 1; i < 6; i += 2) {
        if (F[i] == N/2 && F[(i+3)%6] == N/2 && N % 2 == 0) {
            string res;
            for (int k = 0; k < N/2; ++k) {
                res += sym[i];
                res += sym[(i+3)%6];
            }
            return res;
        }
        if (F[i] && F[i] >= F[(i+3)%6]) {
            return "IMPOSSIBLE";
        }
        F[(i+3)%6] -= F[i];
        N -= 2*F[i];
    }
    string res;
    int si = 0;
    for (int i = 0; i < 6; i += 2)
        if (F[i] > F[si])
            si = i;
    if (F[si] > N/2) return "IMPOSSIBLE";
    for (int i = 0; i < N; ++i) {
        int j = -1;
        if (F[si] && i % 2 == 0)
            j = si;
        else {
            for (int k = 0; k < 6; k += 2) {
                if (F[k] && k != si && res.back() != sym[k] && (j == -1 || F[k] > F[j]))
                    j = k;
            }
        }
        assert(j != -1);
        --F[j];
        res += sym[j];
        while (F[(j+3)%6]) {
            res += sym[(j+3)%6];
            res += sym[j];
            --F[(j+3)%6];
        }
    }
    assert(res.front() != res.back());
    return res;
}

void solve(int P) {
    int N;
    int F[6];
    scanf("%d", &N);
    for (int i = 0; i < 6; ++i)
        scanf("%d", F+i);
	printf("Case #%d: %s\n", P, doit(N, F).c_str());
}

int main(void) {
	init();
	for (int i = 1; i <= CASES; ++i) solve(i);
	return 0;
}
