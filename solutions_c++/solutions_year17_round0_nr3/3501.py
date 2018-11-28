#include <stdio.h>
#include <queue>
#define ll long long

using namespace std;

int t,ans1,ans2,x;
int main() {
	freopen("c:\\C-small-2-attempt0.in", "r", stdin);
	freopen("c:\\output.txt", "w", stdout);
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		ll n, k;
		scanf("%lld%lld", &n, &k);
		priority_queue<int> pq;
		pq.push(n);
		for (int i = 1; i <= k; i++) {
			x=pq.top();
			pq.pop();
			ans1 = x / 2;
			if (x & 1) ans2 = x / 2;
			else ans2 = (x / 2) - 1;
			pq.push(ans1);
			pq.push(ans2);
		}
		printf("Case #%d: %d %d\n", tc, ans1, ans2);
	}
}