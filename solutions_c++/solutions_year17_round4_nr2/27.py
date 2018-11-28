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

void solve(){
	int n,c,m;
	cin >> n >> c >> m;
	vector<vi> ls(c);
	vi cnt(n+1);
	rep(_,0,m){
		int p,b;
		cin >> p >> b;
		ls[b-1].push_back(p);
		cnt[p]++;
	}
	int ans = 0;
	trav(v, ls) ans = max(ans, sz(v));
	int sum = 0;
	rep(i,1,n+1){
		sum += cnt[i];
		ans = max(ans, 1+(sum-1)/i);
	}
	int z = 0;
	trav(x, cnt) z += max(0, x-ans);
	cout << ans << ' ' << z << endl;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	int n;
	cin >> n;
	rep(t,1,n+1){
		cout << "Case #" << t << ": ";
		solve();
	}
}