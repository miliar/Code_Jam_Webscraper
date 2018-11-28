#include <bits/stdc++.h>
  
using namespace std;
  
#define rep(i,n) REP(i,0,n)
#define REP(i,s,e) for(int i=(s); i<(int)(e); i++)
#define pb push_back
#define all(r) r.begin(),r.end()
#define rall(r) r.rbegin(),r.rend()
#define fi first
#define se second
  
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
 
const int INF = 1e9;
const ll MOD = 1e9 + 7;
double EPS = 1e-8;

int main(){
	int mCase;
	scanf("%d", &mCase);
	
	for(int Case = 1; Case <= mCase; Case++){
		int n, q;
		cin >> n >> q;
		vi e(n), s(n);
		rep(i, n) cin >> e[i] >> s[i];
		vector<vi> d(n);
		rep(i, n) {
			d[i].resize(n);
			rep(j, n) cin >> d[i][j];
		}
		vi u(q), v(q);
		rep(i, q) {
			cin >> u[i] >> v[i];
		}
		vector<vl> dist(n, vl(n, 1e18));
		rep(i, n) rep(j, n) {
			if(i == j) dist[i][j] = 0LL;
			else if(d[i][j] != -1) dist[i][j] = d[i][j];
		}
		rep(k, n) rep(i, n) rep(j, n) dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
		vector<vector<double> > time(n, vector<double>(n, 1e18));
		rep(i, n) rep(j, n) {
			if(i == j) time[i][j] = 0.0;
			else if(e[i] >= dist[i][j]) time[i][j] = dist[i][j] / (double)s[i];
		}
		rep(k, n) rep(i, n) rep(j, n) {
			time[i][j] = min(time[i][j], time[i][k] + time[k][j]);
		}

		printf("Case #%d:", Case);
		rep(i, q) {
			printf(" %.15lf", time[u[i]-1][v[i]-1]);
		}
		//cout << endl;
		printf("\n");
	}
}