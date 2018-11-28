#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> ii;
#define fs first
#define sc second
#define pb push_back
const int mod = 1000000007;
const int N = 400004;

void solve(){
	map<ll, ll> mp;
	ll n, k, c = 0;
	cin >> n >> k;
	mp[n] = 1;
	for(auto it = mp.rbegin(); it != mp.rend(); ++it){
		c += it->sc;
		if(c >= k){
			cout << it->fs / 2 << " " << (it->fs - 1) / 2 << "\n";
			return; 
		}
		mp[(it->fs - 1) / 2] += it->sc;
		mp[it->fs / 2] += it->sc;
	}
}

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i){
		printf("Case #%d: ", i);
		solve();
	}
}