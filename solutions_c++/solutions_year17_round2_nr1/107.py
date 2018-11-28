#include <bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define RFOR(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define REP(i,n) for (int i=0;i<(n);i++)
#define RREP(i,n) for (int i=(n)-1;i>=0;i--)

#define INF INT_MAX/3
#define ALL(a) (a).begin(),(a).end()
#define SET(a,c) memset(a,c,sizeof a)
#define CLR(a) memset(a,0,sizeof a)
#define ll long long
#define ull unsigned long long

#define PI (3.1415926535897932)
#define eps 1e-8

void solve() {
	int d, n;
	cin >> d >> n;
	ll k[10000], s[10000];
	REP(i, n) {
		cin >> k[i] >> s[i];
	}

	double max_arr = 0.0;
	REP(i, n) {
		max_arr = max(max_arr, (double) 1.0 * (d - k[i]) / s[i]);
	}

	printf(" %.9f", d / max_arr);
}

int main() {
	int T; cin >> T;
	FOR(i, 1, T + 1) {
		cout << "Case #" << i << ":";
		solve();
		cout << endl;
	}
}