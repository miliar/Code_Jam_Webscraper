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

int T;
string s;

void solve(int t) {
	bool loop = true;
	while (loop) {
		loop = false;
		rep(i, (int)s.size()-1) {
			if (s[i] <= s[i+1]) continue;
			s[i]--;
			REP(j, i+1, s.size()) s[j] = '9';
			loop = true;
			break;
		}
	}
	string ans = "";
	rep(i, s.size()) {
		if ("" == ans && '0' == s[i]) continue;
		ans += s[i];
	}
	printf("Case #%d: %s\n", t, ans.c_str());
}

int main() {
	cin >> T;
	rep(i, T) {
		cin >> s;
		solve(i + 1);
	}
	return 0;
}


