#include "bits\stdc++.h"
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
	int N, P, G[1000];
	cin >> N >> P;
	REP(i, N)cin >> G[i];
	int lo[10000] = {}; int ans;
	REP(i, N)lo[G[i] % P] ++;
	if (P <= 3) {
		if (lo[1] > lo[2]) {
			ans = lo[0] + lo[2] + (lo[1] - lo[2] - 1) / P + 1;
		}
		else if (lo[1] == lo[2]) {
			ans = lo[0] + lo[2];
		}
		else {
			ans = lo[0] + lo[1] + (lo[2] - lo[1] - 1) / P + 1;
		}
	}
	else {
		ans = lo[0] + lo[2] / 2;
		if (lo[1] > lo[3]) {
			ans += lo[3];
			ans += (lo[1] - lo[3] - 1 + (lo[2] % 2 == 1 ? 2 : 0)) / 4 + 1;
		}
		else if (lo[1] < lo[3]) {
			ans += lo[1];
			ans += (lo[3] - lo[1] - 1 + (lo[2] % 2 == 1 ? 2 : 0)) / 4 + 1;
		}
		else {
			ans += lo[1] + (lo[2] % 2 == 1 ? 1 : 0);
		}
	}
	cout << ans;
}

int main() {
	int T; cin >> T;
	FOR(i, 1, T + 1) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
}