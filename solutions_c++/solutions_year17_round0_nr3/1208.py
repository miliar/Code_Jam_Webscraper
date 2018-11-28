#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;

#define INF 1000000000 // 1 billion, safer than 2B for Floyd Warshall’s
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define REP(i, n) for(int i=0;i<(n);i++)
#define FOR(i, a, b) for(int i=(a);i<=(b);i++)
#define FORD(i, a, b) for(int i=(a);i>=(b);i--)

inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

struct Pair{ll a, b;};

Pair solve(long long N, ll K) {
	// cout << N << K << endl;
	// if (K > (N / 2) + 1) return Pair{0, 0};
	if (K == 1) {
		return Pair {(N-1)/2, N/2};
	}	
	if (N % 2 == 1) {
		return solve (N / 2, K / 2);
	} else { // N even
		if (K % 2 == 0) {
			return solve (N / 2, K / 2);
		} else {
			return solve ((N-1) / 2, K / 2);
		}
	}
}
int main() {
    ios::sync_with_stdio(false);
    int T;
    long long N, K;
    cin >> T;
    int cas = 1;
    while (T-- > 0) {
    	cin >> N >> K;
    	cout << "Case #" << cas++ << ": ";
    	Pair p = solve(N, K);
    	cout << p.b << ' ' << p.a << endl;
    }
    return 0;
}