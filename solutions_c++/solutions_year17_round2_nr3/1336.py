#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define RI(i,n) FOR(i,1,(n))
#define REP(i,n) FOR(i,0,(n)-1)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
#define mp make_pair
#define pb push_back
#define st first
#define nd second
#define sz(w) (int) w.size()
#define getin(i,n,tab) REP(i,n) { cin >> tab[i]; }
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<ll,ll> pii;
typedef pair<string, int> para;
const long double inf = 1e18 + 7;
const int MAXN = 1e2 + 7;

long double dp[MAXN];
long long s[MAXN], e[MAXN];

long long dist[MAXN];

int main() {
	ios_base::sync_with_stdio(0);
	
	int t;
	cin >> t;
	
	int dummy;
	int n;
	
	RI(q, t) {
		cin >> n >> dummy;
		REP(i, n) {
			dp[i] = inf;
		}
		
		REP(i, n) {
			cin >> e[i] >> s[i];
		}
		
		dist[0] = 0;
		REP(i, n) {
			REP(j, n) {
				cin >> dummy;
				if (i + 1 == j) {
					dist[j] = dist[i] + dummy;
				}
			}
		}
		
		cin >> dummy;
		cin >> dummy;
		
		dp[0] = 0;
		
		for (int i = 1; i < n; i++) {
			for (int j = 0; j < i; j++) {
				if (dist[i] - dist[j] <= e[j]) {
					dp[i] = min(dp[i], dp[j] + ((long double)(dist[i] - dist[j]) / (long double)s[j]));
				}
			}
		}
		
		cout.precision(9);
		cout << fixed << "Case #" << q << ": " << dp[n - 1] << endl;
	}
}