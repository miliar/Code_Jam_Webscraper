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

int N, M;
int lmate[250], rmate[250], adj[250][250];

bool augment(int d1, vector<int> &vis) {
    vis[d1] = true;
    for (int d2 = 1; d2 < 2*N; ++d2)
        if (adj[d1][d2] && (!rmate[d2] || (!vis[rmate[d2]] && augment(rmate[d2], vis)))) {
            lmate[d1] = d2;
            rmate[d2] = d1;
            return true;
        }
    return false;
}

void solve(int P) {
    memset(lmate, 0, sizeof(lmate));
    memset(rmate, 0, sizeof(lmate));
    memset(adj, 0, sizeof(adj));

    scanf("%d%d", &N, &M);

    int rtaken[200] = {}, ctaken[200] = {}, d1taken[300] = {}, d2taken[300] = {};
    char cur[200][200] = {};
    int add[200][200] = {};

    for (int i = 0; i < M; ++i) {
        char sym[10]; int R, C;
        scanf("%s%d%d", sym, &R, &C);
        if (*sym != '+') rtaken[R] = ctaken[C] = true;
        if (*sym != 'x') {
            d1taken[R+C] = d2taken[N-R+C] = true;
            lmate[R+C] = N-R+C;
            rmate[N-R+C] = R+C;
        }
        cur[R][C] = *sym;
    }
    for (int i = 1; i <= N; ++i)
        if (!rtaken[i])
            for (int j = 1; j <= N; ++j)
                if (!ctaken[j]) {
                    ++add[i][j];
                    rtaken[i] = ctaken[j] = true;
                    break;
                }

    for (int d1 = 2; d1 <= 2*N; ++d1)
        if (!d1taken[d1])
            for (int d2 = 1; d2 < 2*N; ++d2) {
                if (!d2taken[d2] && (d1 + d2 - N) % 2 == 0) {
                    int R, C;
                    C = (d1 + d2 - N)/2;
                    R = (d1 - d2 + N)/2;
                    if (1 <= C && C <= N && 1 <= R && R <= N) {
                        adj[d1][d2] = true;
                        if (lmate[d1] == 0) {
                            vector<int> vis(2*N+1);
                            augment(d1, vis);
                        }
                    }
                }
            }

    int score = N;
    for (int d1 = 2; d1 <= 2*N; ++d1)
        if (lmate[d1]) {
            ++score;
            if (!d1taken[d1]) {
                int R, C;
                C = (d1 + lmate[d1] - N)/2;
                R = (d1 - lmate[d1] + N)/2;
                add[R][C] += 2;
            }
        }
    int adds = 0;
    for (int R = 1; R <= N; ++R)
        for (int C = 1; C <= N; ++C)
            adds += !!add[R][C];

	printf("Case #%d: %d %d\n", P, score, adds);
    for (int R = 1; R <= N; ++R)
        for (int C = 1; C <= N; ++C)
            if (add[R][C]) {
                if (cur[R][C] || add[R][C] == 3)
                    printf("o %d %d\n", R, C);
                else
                    printf("%c %d %d\n", " x+"[add[R][C]], R, C);

            }
}

int main(void) {
	init();
	for (int i = 1; i <= CASES; ++i) solve(i);
	return 0;
}
