#include <bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#ifdef _DEBUG_
	#define debug(...) printf(__VA_ARGS__)
#else
	#define debug(...) (void)0
#endif
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;

typedef pair<ll, ll> PLL;

int main() {
	int all_kase;
	scanf("%d",&all_kase);
	for(int num_kase=1;num_kase<=all_kase;num_kase++) {
		ll N, K, lst = -1;
		cin >> N >> K;
		map<ll, ll> mp;
		mp[N] = 1;
		while(K > 0) {
			auto p = mp.end();
			p--;
			lst = p -> F;
			ll num = p -> S;
			mp.erase(p);
			K -= num;
			mp[lst / 2] += num;
			mp[(lst - 1) / 2] += num;
		}
		assert(lst > 0);
		printf("Case #%d: %lld %lld\n",num_kase, lst / 2, (lst - 1) / 2);
	}
	return 0;
}
