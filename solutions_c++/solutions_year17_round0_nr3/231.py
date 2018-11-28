#include <bits/stdc++.h>
using namespace std;
typedef long long lint;
typedef long double llf;
typedef pair<lint, lint> pi;

void solve(){
	map<lint, lint> mp;
	lint n, k;
	cin >> n >> k;
	mp[n]++;
	while(1){
		pi x = *--mp.end();
		mp.erase(--mp.end());
		k -= x.second;
		if(k <= 0){
			cout << (x.first) / 2 << " " << (-1 + x.first) / 2 << endl;
			return;
		}
		mp[(x.first - 1)/2] += x.second;
		mp[x.first/2] += x.second;
	}
}

int main(){
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		printf("Case #%d: ",i);
		solve();
	}
}
