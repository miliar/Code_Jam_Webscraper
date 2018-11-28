#include <bits/stdc++.h>
using namespace std;
#define ULL unsigned long long
#define LL long long
#define rep(i,n) for(int i = 0; i < n; ++i)
#define Rep(i,n) for(int i = 1; i <= n; ++i)

const int INF = 0x3f3f3f3f;

int main()
{
	int t, cas = 0;
	cin >> t;
	while(cas++ < t) {
		LL n, k;
		cin >> n >> k;
		map<LL, LL> mp;
		mp[n] = 1;
		LL a, b;
		while(k) {
			auto it = mp.rbegin();
			a = it->first;
			b = a / 2;
			a = a - b - 1;
			if(it->second >= k) {
				k = 0;
			}
			else {
				k -= it->second;
				mp[a] += it->second;
				mp[b] += it->second;
				mp.erase(it->first);
			}
		}
		printf("Case #%d: %lld %lld\n", cas, b, a);
	}
	return 0;
}

