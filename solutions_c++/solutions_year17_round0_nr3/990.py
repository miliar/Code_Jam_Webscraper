#include<cstdio>
#include<map>
using namespace std;

typedef long long ll;

ll N, K;

int main() {
	#ifdef LOCAL
		freopen("inC", "r", stdin);
		freopen("outC", "w", stdout);
	#endif
	
	int Cases; scanf("%d", &Cases);
	for(int Case=1; Case<=Cases; ++Case) {
		printf("Case #%d: ", Case);
		scanf("%lld %lld", &N, &K);
		map<ll, ll> q;
		q[N] = 1;
		for(;;) {
			map<ll,ll>::iterator it = q.end(); it--;
			ll big = it->first - 1;
			ll cnt = it->second;
			q.erase(it);
			
			ll size1 = big >> 1;
			ll size2 = big - size1;
			if(q.count(size1) == 0) q[size1] = 0;
			if(q.count(size2) == 0) q[size2] = 0;
			q[size1] += cnt;
			q[size2] += cnt;
			
			if(K <= cnt) {
				printf("%lld %lld\n", size2, size1);
				break;
			}
			K -= cnt;
		}
	}
	
	return 0;
}
