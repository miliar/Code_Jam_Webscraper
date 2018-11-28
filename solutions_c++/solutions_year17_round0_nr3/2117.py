#include <cstdio>
#include <queue>
#include <algorithm>

using namespace std;

struct rg{
	int l, r;
	bool operator <(const rg &t) const{
		return r - l < t.r - t.l;
	}
	rg(int ll, int rr) {l = ll, r = rr;}
};

void sol() {
	long long n, k; 
	scanf("%lld%lld", &n, &k);
	/*priority_queue<rg> pq;
	pq.push(rg(0, n + 1));
	while(k--) {
		rg x = pq.top(); pq.pop();
		int m = (x.l + x.r) / 2;
		l = m - x.l - 1, r = x.r - m - 1;
		pq.push(rg(x.l, m)); pq.push(rg(m, x.r));
	}*/
	//printf("%d %d\n", max(l, r), min(l, r));
	long long addon = 0, b = n, bc = 1, bbc = 0, det = 0;
	for(int i = 0;i < 63;i++) {
		//printf("%lld %lld %lld\n", b, bc, bbc);
		long long p = 1LL << i;
		//printf("%lld %lld\n", addon, p);
		if(addon + p < k) {
			addon += p;
			b--;
			if(b % 2 == 0) 
				bc = 2 * bc + bbc;
			else 
				bbc = 2 * bbc + bc;
			b /= 2;
		} else {
			det = (addon + bbc < k)? b: b + 1;
			if(det == 0) det = 1;
			break;
		}
	}
	det--;
	printf("%lld %lld\n", max(det / 2, det - det / 2), min(det / 2, det - det / 2));
}

int main() {
	int t; scanf("%d", &t);
	for(int i = 1;i <= t;i++) printf("Case #%d: ", i), sol();
}
