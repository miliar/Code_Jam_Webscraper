#include <bits/stdc++.h>
#define rep(x, to) for (int x = 0; x < (to); x++)
#define REP(x, a, to) for (int x = (a); x < (to); x++)
#define EPS (1e-14)
#define _PA(x,N) rep(i,N){cout<<x[i]<<" ";}cout<<endl;
#define _PA2(x,H,W) rep(i,(H)){rep(j,(W)){cout<<x[i][j]<<" ";}cout<<endl;}

using namespace std;

typedef long long ll;
typedef pair<int, int> PII;
typedef pair<ll, ll> PLL;
typedef complex<double> Complex;
typedef vector< vector<int> > Mat;

int ans;
string S;
int T, K;

void solve(int t) {
	ans = 0;
	for (int i = 0; i <= (int)S.size() - K; i++) {
		if ('+' == S[i]) continue;
		for (int j = i; j < i+K; j++) {
			S[j] = ('+' == S[j]) ? '-' : '+';
		}
		ans++;
	}
	for (int i = 0; i < S.size(); i++) {
		if ('-' == S[i]) {
			ans = -1;
			break;
		}
	}
	if (-1 != ans) {
		printf("Case #%d: %d\n", t, ans);
	} else {
		printf("Case #%d: IMPOSSIBLE\n", t);
	}
}

int main() {
	cin >> T;
	rep(i, T) {
		cin >> S >> K;
		solve(i + 1);
	}
	return 0;
}

