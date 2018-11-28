#include <iostream>
#include <algorithm>
using namespace std;

#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define RFOR(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define REP(i,n) for (int i=0;i<(n);i++)
#define RREP(i,n) for (int i=(n)-1;i>=0;i--)

#define ll long long
#define ull unsigned long long

#define PI (3.141592653589794)
#define eps 1e-8
#define LINF (1ll << 40)

void solve() {

	int N, Q;
	cin >> N >> Q;

	ll E[1000], S[1000], D[1000][1000];

	REP(i, N)cin >> E[i] >> S[i];
	REP(i, N)REP(j, N) cin >> D[i][j];

	ll dist[200][200];
	REP(i, N) {
		REP(j, N) {
			dist[i][j] =(D[i][j] >= 0) ? D[i][j] : LINF;
		}
	}

	REP(k, N) {
		REP(i, N) {
			REP(j, N) {
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
			}
		}
	}

	double time[200][200];

	REP(i, N) {
		REP(j, N) {
			time[i][j] = (dist[i][j] <= E[i]) ? (1.0 * dist[i][j] / S[i]) : (double)LINF;
		}
	}

	double alltime[200][200] = {};
	REP(i, N) {
		REP(j, N) {
			alltime[i][j] = time[i][j];
		}
	}

	REP(k, N) {
		REP(i, N) {
			REP(j, N) {
				alltime[i][j] = min(alltime[i][j], alltime[i][k] + alltime[k][j]);
			}
		}
	}

	ll U[1000], V[1000];
	REP(i, Q) {
		cin >> U[i] >> V[i];
		printf(" %.9f", alltime[U[i] - 1][V[i] - 1]);
	}

}

int main() {
	int T; cin >> T;
	FOR(i, 1, T + 1) {
		cout << "Case #" << i << ":";
		solve();
		cout << endl;
	}
}