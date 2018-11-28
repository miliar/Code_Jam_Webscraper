#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()

template<typename A, typename B> inline bool chmax(A &a, B b) { if (a<b) { a=b; return 1; } return 0; }
template<typename A, typename B> inline bool chmin(A &a, B b) { if (a>b) { a=b; return 1; } return 0; }

typedef unsigned long long ull;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<int, pii> P;

const ll INF = 1ll<<29;
const ll MOD = 1000000007;
const double EPS  = 1e-10;

int main() {
	int n;
	cin >> n;
	REP(Case, n) {
		int K;
		string S;
		
		cin >> S >> K;
		REP(i, S.size()) S[i] = S[i] == '+';
		
		int pos = K - 1;
		
		int ans = 0;
		
		while (pos < S.size()) {
			if (!S[pos - (K - 1)]) {
				ans++;
				REP(i, K) S[pos - i] ^= 1;
			}
			pos++;
		}
		
		
		bool ng = false;
		REP(i, S.size()) if (!S[i]) ng = true;
		
		printf("Case #%d: ", Case + 1);
		if (ng) puts("IMPOSSIBLE");
		else cout << ans << endl;
	}
	return 0;
}