# include <set>
# include <map>
# include <functional>

using namespace std;

map<long long, long long, greater<long long>> mp;

void add(long long x,long long y) {
	//printf("add %lld %lld\n",x , y);
	if(x == 0) return;
	if(!mp.count(x)) mp[x] = y;
	else mp[x] += y;
}

int main() {
	int T, cas = 0; scanf("%d", &T);
	while(T--) {
		printf("Case #%d: ", ++cas);
		long long n, k;
		scanf("%lld%lld", &n, &k);
		mp.clear();
		mp[n] = 1;
		long long ans = -1;
		while(!mp.empty()) {
			auto it = mp.begin();
			if(it->second >= k) {
				ans = it->first;
				break;
			}
			k -= it->second;
			add(it->first / 2, it->second);
			add((it->first - 1) / 2, it->second);
			mp.erase(mp.begin());
		}
		printf("%lld %lld\n", ans / 2, (ans - 1) / 2);
	}
	return 0;
}

