#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(ll i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(ll i = (a); i >= (b); --i)
#define RI(i,n) FOR(i,1,(n))
#define REP(i,n) FOR(i,0,(n)-1)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
#define mp make_pair
#define pb push_back
#define st first
#define nd second
#define sz(w) (ll) w.size()
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<ll,ll> pii;
typedef pair<pii, ll> para;
const ll inf = 1e18 + 7;
const ll maxN = 1e3 + 5;

int n, q, u, v, t;
ll horse[maxN], dist[maxN][maxN], speed[maxN];
ll pref[maxN];
ld dp[maxN][maxN];

int main() {
	ios_base::sync_with_stdio(0);
	cin>>t;
	RI(x, t) {
		cin>>n>>q;
		RI(i, n)
			cin>>horse[i]>>speed[i];
		RI(i, n) {
			RI(j, n) {
				cin>>dist[i][j];
				if (dist[i][j] == -1) dist[i][j] = inf;
			}
		}

		RI(k, n)
			RI(i, n)
				RI(j, n)
					dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);

		RI(i, n)
			RI(j, n)
				if (horse[i] >= dist[i][j])
					dp[i][j] = ((ld)dist[i][j] / speed[i]);
				else dp[i][j] = inf;

		RI(k, n)
			RI(i, n)
				RI(j, n)
					dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
		cout<<"Case #"<<x<<": ";
		REP(_, q) {
			cin>>u>>v;
			cout<<fixed<<setprecision(9)<<dp[u][v]<<" ";
		}
		cout<<endl;
	}
	return 0;
}
