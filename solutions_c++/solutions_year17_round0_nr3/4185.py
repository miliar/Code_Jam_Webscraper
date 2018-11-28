#include <cstring>
#include <cstdio>
#include <algorithm>
#include <queue>
#define pii pair<int,int>
#define fi first
#define se second

using namespace std;
typedef long long LL;

LL n, k;
priority_queue<pii> d; 

void solve(int tim) {
	printf("Case #%d: ", tim);
	scanf("%lld%lld", &n, &k);
	while (!d.empty()) d.pop();
	d.push(pii(n, 1));
	while (k) {
		pii now = d.top();
		d.pop();
		for (; !d.empty() && d.top().fi == now.fi; d.pop()) 
			now.se += d.top().se;
		LL a = (now.fi - 1) / 2;
		LL b = now.fi - 1 - a;
		if (now.se >= k) {
			printf("%lld %lld\n", b, a);
			break;
		}
		k -= now.se;
		d.push(pii(a, now.se));
		d.push(pii(b, now.se));
	}
}

int main() {
	//freopen("C.in", "r", stdin), freopen("C.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i ++) solve(i);
}