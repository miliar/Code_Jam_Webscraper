#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(){
	freopen("input.in","r",stdin);
	freopen("output-final.out","w+",stdout);

	int T; cin >> T;
	int cnt = 1;

	while (T--){
		ll n,k; cin >> n >> k;
		ll a = 0;
		ll b = n + 1;

		while (k != 1){
			ll sel = a + (b - a)/2;
			if ( k % 2 == 1){
				b = sel;
			}else{
				a = sel;
			}
			k = k / 2;
		}
		//printf("%lld %lld \n",a,b);
		ll sel = a + (b-a)/2;

		ll left  = sel - a - 1;
		ll right = b - sel - 1;

		printf("Case #%d: %lld %lld\n",cnt++, max(right,left),min(right,left));
	}
}