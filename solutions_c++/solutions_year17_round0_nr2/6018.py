#include <bits/stdc++.h>
using namespace std;

#define MOD 1000000007
typedef long long ll;
ll n;

int main(){
//ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);

int T;
cin >> T;
for(int t = 1; t <= T; t++){
	cin >> n;
	vector<int> v;
	ll x = n;
	while(x){
		v.push_back(x % 10);
		x /= 10;
	}
	reverse(v.begin(), v.end());
	int len = v.size();
	for(int i = len - 2; i >= 0; i--){
		if(v[i + 1] < v[i]){
			for(int j = i + 1; j < len; j++){
				v[j] = 9;
			}
			v[i]--;
		}
	}
	ll ans = 0;
	for(int i = 0; i < len; i++){
		ans = 10LL * ans + v[i];
	}
	printf("Case #%d: %lld\n", t, ans);
}
return 0;
}