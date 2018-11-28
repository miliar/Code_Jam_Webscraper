#include <bits/stdc++.h>
#define ll long long
using namespace std;

ll exp(ll a,ll b){
	ll f = 1;
	for (ll i=1;i<=b;i++) f*=a;
	return f;
}

int main(){
	freopen("large.in","r",stdin);
	freopen("large.out","w",stdout);
	int t,cs = 1;
	cin >> t;
	while(t--){
		ll n;
		cin >> n;
		ll a[20],c = 0;
		ll temp = n;
		while(temp){
			a[c++] = temp%10;
			temp/=10;
		}
		for (int i=0;i<c/2;i++) swap(a[i],a[c-i-1]);
		ll prev = 0,mx = 0;
		for (int i=0;i<c;i++){
			if (a[i]<prev) break;
			ll x = (n/exp(10,c-i-1));
			for (int j=0;j<c-i-1;j++){
				x = (x*10+9);
			}
			if (x<=n){
				mx = max(mx,x);
				break;
			}
			if (a[i]-1>=prev){
				ll x = (n/exp(10,c-i));
				x = (x*10+(a[i]-1));
				for (int j=0;j<c-i-1;j++){
					x = (x*10+9);
				}
				mx = max(mx,x);
			}
			prev = a[i];
		}
		printf("Case #%d: %lld\n",cs++,mx);
	}
	return 0;
}