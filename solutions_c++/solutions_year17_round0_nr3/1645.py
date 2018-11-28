
#include <cstdio>
#include <algorithm>
#include <map>
using namespace std;

typedef long long i8;
i8 n, k;
map<i8,i8> mp;

i8 solve() {
	scanf("%lld %lld", &n,&k);
	mp.clear();
	
	mp[n]=1LL;
	while (1) {
		map<i8,i8>::reverse_iterator i=mp.rbegin();
		i8 sz=i->first, cnt=i->second;
		mp.erase(sz);
		//printf("  got sz=%lld cnt=%lld\n", sz, cnt);
	
		k -= cnt;
		if (k<=0) 
			return sz;
	
		if (sz%2) {
			mp[sz/2] += cnt*2;
		} else {
			mp[sz/2-1] += cnt;
			mp[sz/2] += cnt;
		}
	}
	return -1LL;
}

main() {
	int ccnt;
	scanf("%d", &ccnt);
	for (int cs=1; cs<=ccnt; cs++) {
		printf("Case #%d: ", cs);
		i8 last=solve();
		printf("%lld %lld\n", last/2, (last-1)/2);
	}
}
