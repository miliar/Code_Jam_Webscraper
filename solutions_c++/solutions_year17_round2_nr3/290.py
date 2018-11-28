#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i = a; i < (b); ++i)
#define rrep(i,a,b) for(int i = b; i --> (a);)
#define all(v) v.begin(),v.end()
#define trav(x,v) for(auto &x : v)
#define sz(v) (int)(v).size()
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long double ld;

const ld inf = 1e16;

void solve(){
	int n, q;
	cin >> n >> q;
	vector<vector<ld>> di(n, vector<ld>(n)), ti(n, vector<ld>(n, inf));
	vector<ld> es(n), ss(n);
	rep(i,0,n) cin >> es[i] >> ss[i];
	rep(i,0,n) rep(j,0,n){
		cin >> di[i][j];
		if(di[i][j]<-0.5) di[i][j] = inf;
	}
	rep(k,0,n) rep(i,0,n) rep(j,0,n) di[i][j] = min(di[i][j], di[i][k] + di[k][j]);
	rep(i,0,n) rep(j,0,n){
		if(di[i][j] <= es[i]+0.1) ti[i][j] = di[i][j]/ss[i];
	}
	rep(k,0,n) rep(i,0,n) rep(j,0,n) ti[i][j] = min(ti[i][j], ti[i][k] + ti[k][j]);
	rep(_,0,q){
		int u,v;
		cin >> u >> v;
		cout << ti[u-1][v-1] << ' ';
	}
	cout << endl;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	int n;
	cin >> n;
	cout.precision(8);
	rep(i,1,n+1){
		cout << "Case #" << i << ": ";
		solve();
	}
}