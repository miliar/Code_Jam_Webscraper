#include <bits/stdc++.h>

#define ll long long
using namespace std;

const int MAXN = 200005;
const int MOD = 1000000007;

ll n,k,fans;

void fun(ll e,ll o,ll l,ll v,ll h){
	if(v >= k){
		if(h&1){
			if(v-e >= k) fans = h;
			else fans = h-1;
		}
		else{
			if(v-o >= k) fans = h;
			else fans = h-1;
		}
		return ;
	}
	++l;
	ll f = 0;
	if(h&1){
		if((h/2)&1) f = 1;
	}
	else{
		if(((h-1)/2) & 1) f = 1;
	}
	fun(o*(1-f)*2+e,o*f*2+e,l, v + (1ll << l),h/2);
}

int main(){
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for(int tc = 1; tc <= T; tc++){
		cout << "Case #" << tc << ": ";
		cin >> n >> k;
		ll x;
		for(ll i=61;i>=0;i--){
			if((1ll << 61) & n){
				x = i; break;
			}
		}
		fun((n%2 == 0),n&1,0,1,n);
		fans--;
		cout << (fans - fans/2) << ' ' << fans / 2 << '\n';
	}
	return 0;
}

