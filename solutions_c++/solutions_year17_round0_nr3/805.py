#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll;

int tcn;
ll n, k;

int main(){
	freopen("Cl.in", "r", stdin);
	freopen("Cl.out", "w", stdout);
    scanf("%d", &tcn); for(int tc = 1; tc <= tcn; tc++){
		scanf("%lld%lld", &n, &k);
		printf("Case #%d: ", tc);
		map<ll, ll> mp;
		mp[-n] = 1;
		while(true){
			pll t = *mp.begin();
			mp.erase(mp.begin());
			ll x1 = -t.first / 2;
			ll x2 = (-t.first - 1) / 2;
			ll y = t.second;
			if(k <= y){ printf("%lld %lld\n", x1, x2); break; }
            mp[-x1] += y;
            mp[-x2] += y;
            k -= y;
		}
    }
}
