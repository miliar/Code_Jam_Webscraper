#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
LL N, K;
int main()
{
	int T; scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas) {
		scanf("%lld%lld", &N, &K);
		map<LL, LL> count;
		count[N] = 1;
		while(K > 0) {
			auto it = count.rbegin();
			LL x = it->first;
			LL y = it->second;
			count.erase(x);
			LL a = (x - 1) / 2, b = (x - 1) - a;
			K -= y;
			if(K <= 0) {
				printf("Case #%d: %lld %lld\n", cas, max(a, b), min(a, b));
			}
			count[a] += y;
			count[b] += y;
		}
	}
	return 0;
}
