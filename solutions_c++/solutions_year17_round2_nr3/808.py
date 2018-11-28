#include <bits/stdc++.h>

using namespace std;

#define INF 1e15
#define MAXN 103
#define MAXQ 103

struct state {
	int crt, prv;
	double t;

	state(int crt, int prv, double t) : crt(crt), prv(prv), t(t) {}
};

struct Comp {
	bool operator()(const state &a, const state &b) const {
		return a.t < b.t;
	}
};

int N, Q;
int E[MAXN], S[MAXN];
long long minD[MAXN][MAXN];
long long D[MAXN][MAXN];
int U[MAXQ], V[MAXQ];
double minTime[MAXN][MAXN];
double ans[MAXQ];

set<state, Comp> states;

double solveQ(int src, int dst) {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			minTime[i][j] = INF;
		}
	}
	minTime[src][src] = 0.0;
	states.insert(state(src, src, 0.0));

	while (!states.empty()) {
		state top = *states.begin();
		states.erase(states.begin());

		int crt = top.crt;
		int prv = top.prv;
		double t = top.t;

		if (t - 1e-6 > minTime[crt][prv]) {
			continue;
		}
		// cerr << crt << ' ' << prv << ' ' << t << endl;
		// for (int i = 0; i < N; i++) {
		// 	cerr << minD[crt][i] << endl;
		// }
		// cerr << "======\n";
		// cerr << E[prv] << endl;

		// same horse
		int horseLeft = E[prv] - minD[prv][crt];
		int horseSpeed = S[prv];
		for (int i = 0; i < N; i++) {
			if (minD[crt][i] != -1 && minD[crt][i] <= horseLeft) {
				double crtTime = (double) minD[crt][i] / horseSpeed;
				if (t + crtTime < minTime[i][prv]) {
					minTime[i][prv] = t + crtTime;
					states.insert(state(i, prv, minTime[i][prv]));
				}
			}
		}

		// change horse
		if (t < minTime[crt][crt]) {
			minTime[crt][crt] = t;
			states.insert(state(crt, crt, t));
		}
	}

	double vmin = INF;
	for (int i = 0; i < N; i++) {
		vmin = min(vmin, minTime[dst][i]);
	}
	return vmin;
}

void solve() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			minD[i][j] = D[i][j];
		}
		minD[i][i] = 0.0;
	}
	for (int k = 0; k < N; k++) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (minD[i][k] != -1 && minD[k][j] != -1) {
					if (minD[i][j] == -1 || minD[i][k] + minD[k][j] < minD[i][j]) {
						minD[i][j] = minD[i][k] + minD[k][j];
					}
				}
			}
		}
	}

	for (int i = 0; i < Q; i++) {
		ans[i] = solveQ(U[i], V[i]);
	}
}

int main() {
	assert(freopen("C.in", "r", stdin));
	assert(freopen("C.out", "w", stdout));
	cin.sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";

		cin >> N >> Q;
		for (int i = 0; i < N; i++) {
			cin >> E[i] >> S[i];
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cin >> D[i][j];
			}
		}
		for (int i = 0; i < Q; i++) {
			cin >> U[i] >> V[i];
			U[i]--; V[i]--;
		}

		solve();

		for (int i = 0; i < Q; i++) {
			if (i > 0) {
				cout << ' ';
			}
			cout << fixed << setprecision(9) << ans[i];
		}
		cout << '\n';
		
		cerr << t << endl;
	}

	return 0;
}
