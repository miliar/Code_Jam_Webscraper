#include <bits/stdc++.h>
using namespace std;
#define INF 0x3f3f3f3f
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define endl "\n"
#define PI acos(-1)
typedef long long ll;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef pair<int,int> ii;
typedef complex<double> base;

int t;
ll n, k;
map<ll,ll> space;

int main(void){
	scanf("%d", &t);

	for(int caso = 1; caso <= t; caso++){
		space.clear();
		scanf("%lld%lld", &n, &k);
		space[n] = 1LL;

		pair<ll,ll> res;
		while(k > 0){
			auto it = space.end();
			it--;
			ll cur = it->fi, qnt = it->se;
			
			if(cur%2 == 1){
				if(cur > 1)
					space[cur/2LL] += 2LL*space[cur];
				res.fi = res.se = cur/2LL;
			}
			else{
				space[cur/2LL] += space[cur];
				if(cur > 2LL)
					space[cur/2LL-1LL] += space[cur];
				res.fi = cur/2LL;
				res.se = cur/2LL-1LL;
			}

			ll tirar = min(k, qnt);

			if(tirar == qnt){
				space.erase(cur);
			}
			else{
				it->se -= tirar;
			}

			k -= tirar;
			/*if(qnt == 1){
				space.erase(cur);
			}
			else it->se--;
			*/
		}

		printf("Case #%d: %lld %lld\n", caso, res.fi, res.se);
	}

	return 0;
}
