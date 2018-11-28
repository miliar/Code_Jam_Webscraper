#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i = (a); i < int(b); ++i)
#define rrep(i,b,a) for(int i = (b); i --> int(a);)
#define trav(i,v) for(auto&i:v)
#define all(c) (c).begin(), (c).end()
#define sz(c) int((c).size())
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
int main(){
	cin.sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	rep(t,1,T+1){
		ll N,K;
		cin >> N >> K;
		map<ll,ll> M;
		M[N] = 1;
		while(K > 0){
			auto p = *--M.end();
			if(p.second >= K) break;
			K -= p.second;
			M.erase(--M.end());
			if(p.first > 1ll) M[p.first/2ll] += p.second;
			if(p.first > 2ll) M[(p.first-1)/2ll] += p.second;
		}
		ll s = M.rbegin()->first;
		cout << "Case #" << t << ": " << s/2ll << " " << (s-1)/2ll << endl;
	}
}