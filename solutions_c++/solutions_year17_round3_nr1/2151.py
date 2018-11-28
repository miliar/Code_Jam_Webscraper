#include <bits/stdc++.h>
#define rep(x, to) for (int x = 0; x < (to); x++)
#define REP(x, a, to) for (int x = (a); x < (to); x++)
#define EPS (1e-14)
#define _PA(x,N) rep(i,N){cout<<x[i]<<" ";}cout<<endl;
#define _PA2(x,H,W) rep(i,(H)){rep(j,(W)){cout<<x[i][j]<<" ";}cout<<endl;}
#define M_PI 3.1415926535897932384626433832795 

using namespace std;

typedef long long ll;
typedef pair<int, int> PII;
typedef pair<ll, ll> PLL;
typedef complex<double> Complex;
typedef vector< vector<int> > Mat;

int T;
int K, N;
PII rh[1005];
int memo[1005][1005];
double dp[1005][1005];

bool compare(PII x, PII y) {
	if (x.first < y.first) {
		return true;
	} else if (x.first > y.first) {
		return false;
	} else {
		return x.second >= y.second;
	}
}

void solve(int t) {

	sort(rh, rh+N, compare);
	double ans = 0.0;
	for (int mask = 0; mask < (1<<N); mask++) {
		if (__builtin_popcount(mask) != K) continue;
		double tmp_ans = 0.0;
		int prev_r = 0;
		for (int i = 0; i < N; i++) {
			if ((mask & (1<<i)) == 0) continue;
			int r = rh[i].first;
			int h = rh[i].second;
			double cost = (M_PI * r * r) + (2 * M_PI * r * h) - (M_PI * prev_r * prev_r);
			tmp_ans += cost;
			prev_r = r;
		}
		ans = max(ans, tmp_ans);
	}

	printf("Case #%d: %.12f\n", t, ans);
}

int main() {
	cin >> T;
	rep(t, T) {
		cin >> N >> K;
		rep(i, N) {
			cin >> rh[i].first >> rh[i].second;
		}
		solve(t+1);
	}
	return 0;
}


