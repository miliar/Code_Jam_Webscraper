#include <bits/stdc++.h>

using namespace std;

#define REP(i, N) for (int (i) = 0; (i) < (N); ++(i))
#define READALL(c) for (auto &e : c) { cin >> e; }
#define PRINTALL(c) for (const auto &e : c) { cout << e << "\t"; } cout << "\n";

template <typename T>
using V = vector<T>;


int N, Q;

V<int64_t> E, S;

V<V<int64_t>> D, DD;


typedef long double ld;


V<ld> DP;

ld f(int at) {
	if (at == N-1)
		return 0.0;
	if (DP[at] > -1) {
		return DP[at];
	}
	int64_t d = 0;
	ld ans = 1e18;
	for (int next = at+1; next < N; ++next) {
		d += D[next-1][next];
		if (d > E[at])
			break;
		ld t = d/ld(S[at]);
		ans = min(ans, t+f(next));
	}
	// cout << at << " " << ans << endl;
	return DP[at] = ans;
}

vector<int64_t> dijk(int from) {
	V<int> vis(N);
	V<int64_t> dists(N, 1e18);
	set<pair<int64_t, int>> Q;
	Q.emplace(0, from);
	while (!Q.empty()) {
		int64_t dist;
		int at;
		tie(dist, at) = *Q.begin();
		Q.erase(Q.begin());
		if (vis[at])
			continue;
		vis[at] = 1;
		dists[at] = dist;
		for (int c = 0; c < N; ++c) if (D[at][c] != -1) {
			if (vis[c]) {
				continue;
			}
			int64_t d = dist+D[at][c];
			Q.emplace(d, c);

		}
	}
	return dists;
}

void buildDD() {
	DD.clear();
	REP(i, N) {
		DD.push_back(dijk(i));
	}
}

ld metadijk(int from, int target) {
	V<int> vis(N);
	set<pair<ld, int>> Q;
	Q.emplace(0, from);
	while (!Q.empty()) {
		ld d;
		int at;
		tie(d, at) = *Q.begin();
		Q.erase(Q.begin());
		// cout << d << " " << at << endl;
		if (vis[at])
			continue;
		vis[at] = 1;
		if (at == target)
			return d;
		for (int c = 0; c < N; ++c) if (DD[at][c] < 1e18) {
			if (vis[c])
				continue;
			if (DD[at][c] > E[at])
				continue;
			// cout << DD[at][c] << " " << S[at] << endl;
			ld t = DD[at][c]/ld(S[at]);
			Q.emplace(d+t, c);
		}
	}
	assert(0);
}

void solve2() {
	cin >> N >> Q;
	DP.assign(N, -10);
	E.resize(N);
	S = E;
	D.assign(N, V<int64_t>(N));
	REP(i, N) {
		cin >> E[i] >> S[i];
	}
	REP(i, N) {
		REP(j, N) {
			cin >> D[i][j];
		}
	}
	buildDD();
	// for (auto v : DD) {
	// 	for (int64_t a : v) {
	// 		cout << a << " ";
	// 	}
	// 	cout << endl;
	// }
	REP(q, Q) {
		int u, v;
		cin >> u >> v;
		--u; --v;
		cout << fixed << setprecision(20);
		cout << metadijk(u, v) << " ";
	}
	cout << endl;
}

void solve() {
	cin >> N >> Q;
	DP.assign(N, -10);
	E.resize(N);
	S = E;
	D.assign(N, V<int64_t>(N));
	REP(i, N) {
		cin >> E[i] >> S[i];
	}
	REP(i, N) {
		REP(j, N) {
			cin >> D[i][j];
		}
	}
	int U, V;
	cin >> U >> V;
	--U; --V;
	assert(U == 0 && V == N-1);
	cout << fixed << setprecision(20);
	cout << f(0) << endl;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T;
	cin >> T;

	REP(tc, T) {
		cout << "Case #" << (tc+1) << ": ";
		solve2();
	}
}