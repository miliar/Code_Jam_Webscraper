#include <bits/stdc++.h>

#define vi vector<int>
#define vpii vector< pair<int,int> >
#define pii pair<int,int>
#define mp(x,y) make_pair(x,y)
#define all(x) (x).begin(),(x).end()
#define FOREACH(it,x) for (auto it = (x).begin(); it!=(x).end(); ++it)
#define sz(x) (int)(x).size()
#define FOR(i,n) for (ll i = 0; i < ll(n); i++)
#define ROF(i,n) for (ll i = ((ll)n-1); i >= 0; i--)
#define FOR1(i,n) for (ll i = 1; i < ll(n); i++)
#define READ(a) int a; 0 == scanf("%d", &a);
#define READV(v,n) vi v(n);FOR(_i,n){ 0 == scanf("%d", &v[_i]);}
#define WRITE(v) FOR(i,sz(v))cout<<v[i]<<" ";
#define gmin(a,b) { if (b < a) a = b; }
#define gmax(a,b) { if (b > a) a = b; }
#define pb push_back
#define ff first
#define ss second
#define oo ((1LL<<62)+((1LL<<31)-1))
const double PI = std::atan(1.0)*4;
#define cpx complex<double>
#define MOD 1000000007ll
typedef long long ll;
typedef unsigned long long ull;
using namespace std;
#define MAXN 100000

int n, c, m;
vpii tick;
int maxb;

int solve2(int k){
	vector<vi> fl(k, vi(n, 0));
	int res = 0;
	// cout<<k<<endl;
	FOR(i, sz(tick)){
		int p = tick[i].ff;
		// cout<<"."<<p<<endl;

		FOR(j, k){
			if(fl[j][p]==0){fl[j][p]=1; goto next;}
		}
		res += 1;
		FOR(j, k){
			if(fl[j][p]==2){res -= 1; break;}
		}
		p--;
		while(p>=0){
			FOR(j, k){
				if(fl[j][p]==0){fl[j][p]=2; goto next;}
			}
			p--;
		}
		if(p < 0) return -1;

		next: continue;
	}
	return res;
}

pii solve(){
	for(int i = maxb; i<=m; i++){
		auto r = solve2(i);
		if(r!=-1) return mp(i, r);
	}
}

int main(int argc, char *argv[]){
	READ(T);
	FOR(t, T){
		cin>>n>>c>>m;
		tick.clear();
		maxb = 0;
		vi v(c, 0);
		FOR(i,m){
			int p, b;
			cin>>p>>b;
			b--;p--;
			tick.pb(mp(p,b));
			v[b]++;
			gmax(maxb, v[b]);
		}
		auto res = solve();
		cout<<"Case #"<<(t+1)<<": "<<res.ff<<" "<<res.ss<<endl;

	}
	return 0;
}