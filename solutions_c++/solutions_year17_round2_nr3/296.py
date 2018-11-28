#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define scanf nope
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

void solve() {
	int N, Q;
	cin >> N >> Q;

	vector<vector<double>> bestTime(N, vector<double>(N, 1e100));
	vector<vector<long long>> dist(N, vector<long long>(N));
	vector<long long> speed(N);
	vector<long long> reach(N);
	rep(i,0,N) {
		cin >> reach[i] >> speed[i];
	}
	rep(i,0,N) rep(j,0,N) cin >> dist[i][j];
	rep(k,0,N) rep(i,0,N) rep(j,0,N) {
		if (dist[i][k] == -1 || dist[k][j] == -1) continue;
		ll ndist = dist[i][k] + dist[k][j];
		if (dist[i][j] == -1 || dist[i][j] > ndist) dist[i][j] = ndist;
	}

	rep(i,0,N) rep(j,0,N) {
		if (dist[i][j] != -1 && reach[i] >= dist[i][j]) bestTime[i][j] = min(bestTime[i][j], double(dist[i][j]) / speed[i]);
	}
	rep(k,0,N) rep(i,0,N) rep(j,0,N) {
		double ntime = bestTime[i][k] + bestTime[k][j];
		if (bestTime[i][j] > ntime) bestTime[i][j] = ntime;
	}
	rep(i,0,Q) {
		int A, B;
		cin >> A >> B;
		--A; --B;
		cout << fixed << setprecision(10) << bestTime[A][B] << ' ';
	}
	cout << endl;
}

int main() {
	cin.sync_with_stdio(0);
	cin.exceptions(cin.failbit);

	int TC;
	cin >> TC;
	rep(i,0,TC) {
		cout << "Case #" << (i + 1) << ": ";
		solve();
	}
}
