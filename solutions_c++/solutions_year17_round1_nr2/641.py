#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for(int i=0; i<int(n); ++i)
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()
typedef long long ll;


int TC;
int debugcase = 5;

void solve() {
	int N, P;
	cin >> N >> P;
	vector<int> R(N);
	rep(i, N) cin >> R[i];
	vector<int> Q[55];
	rep(i, N) {
		Q[i].assign(P, 0);
		rep(j, P) cin >> Q[i][j];
		sort(all(Q[i]));
	}
	vector<int> points;
	int Low[55][55];
	int High[55][55];
	rep(i, N) {
		rep(j, P) {
			int q = Q[i][j];
			int high = q * 10 / R[i] / 9;
			int low = (q * 10 + R[i]*11-1) / (R[i] * 11);
			points.push_back(low);
			points.push_back(high);
			Low[i][j] = low;
			High[i][j] = high;
		}
	}
	sort(all(points));
	points.erase(unique(all(points)), points.end());
	int curs[55] = {};
	int ans = 0;
	for(int k=0; k<sz(points); k++) {
		assert(0 <= k && k < sz(points));
		int p = points[k];
		bool done = false;
		bool ok = true;
		rep(i, N) {
			while (curs[i] < P && p > High[i][curs[i]]) {
				curs[i] += 1;
			}
			if (curs[i] >= P) done = true;
		}
		/*
		if (TC==debugcase) {
			cout << "---" << endl;
			cout << p << endl;
			rep(i, N) {
				cout << curs[i] << " ";
			}
			cout << endl;
		}
		*/
		if (done) break;
		rep(i, N) {
			assert(curs[i] < P);
			if (!(Low[i][curs[i]] <= p && p <= High[i][curs[i]])) {
				ok = false;
				break;
			}
		}
		if (!ok) continue;

		ans += 1;
		rep(i, N) curs[i] += 1;
		k--;
	}
	cout << ans << endl;
}
int main() {
	int T; cin >> T;
	for(TC=1; TC<=T; TC++) {
		cout << "Case #" << TC << ": ";
		solve();
	}
}

