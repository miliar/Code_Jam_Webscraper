#include <bits/stdc++.h>
using namespace std;
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define FOR0(i,n) for(int i=0, _##i=(n); i<_##i; ++i)
#define FOR(i,l,r) for(int i=(l), _##i=(r); i<_##i; ++i)
#define FORD(i,l,r) for(int i=(r), _##i=(l); --i>=_##i; )
#define repi(i,a) for(__typeof((a).begin()) i=(a).begin(), _##i=(a).end(); i!=_##i; ++i)
#define dwni(i,a) for(__typeof((a).rbegin()) i=(a).rbegin(), _##i=(a).rend(); i!=_##i; ++i)
#define printCase() "Case #" << caseNum << ": "
#define pb push_back
#define mp make_pair
#define INF (int)1e9
#define EPS 1e-9
#define SYNC std::ios::sync_with_stdio(false)
#define ff first
#define ss second
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<vi> vvi;

int main() {
	const double PI = 2*acos(0.0);
	SYNC;
	int t, n, k, r[1001], h[1001];
	ii cake[1001];
	ll dp[1001][1001];
	cin >> t;
	FOR(caseNum,1,t+1) {
		cin >> n >> k;
		FOR0(i, n) cin >> r[i] >> h[i];
		FOR0(i, n) cake[i] = mp(r[i], h[i]);
		sort(cake,cake+n,greater<ii>());
		FOR0(i, n) r[i] = cake[i].ff;
		FOR0(i, n) h[i] = cake[i].ss;
		FOR(i,0,n) dp[0][i] = (ll)r[i]*(ll)r[i] + 2*(ll)r[i]*(ll)h[i];
		FOR(level,1,k) {
			FOR(i,0,n) {
				dp[level][i] = -INF;
				FOR(j,0,i) {
					if(dp[level-1][j] != -INF) dp[level][i] = max(dp[level][i], dp[level-1][j]  + 2*(ll)r[i]*(ll)h[i]); //+ ((ll)r[j]*(ll)r[j])-((ll)r[i]*(ll)r[i])
				}
			}
		}
		ll ans = *max_element(dp[k-1], dp[k-1]+n);
		cout << printCase() << fixed << setprecision(6) << PI*ans << endl;
	}
}