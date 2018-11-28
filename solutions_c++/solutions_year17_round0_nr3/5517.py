#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <queue>
#include <functional>
#include <memory.h>
#include <algorithm>
using namespace std;

bool check[1000002];

int main() {
	int t, n, k, ans = 0;
	char s[100];
	//freopen("C-small-1-attempt0.in", "r", stdin);
	//freopen("output.txt", "w", stdout);
	
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		priority_queue < pair<int, pair<int, int> > > pq;
		scanf("%d %d", &n, &k);

		pq.push(make_pair(n, make_pair(0, n + 1)));
		int l, r, mid;
		for (int i = 0; i < k; i++) {
			l = pq.top().second.first;
			r = pq.top().second.second;
			mid = (l + r) / 2;
			pq.pop();

			pq.push(make_pair(mid - l - 1, make_pair(l, mid)));
			pq.push(make_pair(r - mid - 1, make_pair(mid, r)));
		}
		int maxAns = max(mid - l - 1, r - mid - 1);
		int minAns = min(mid - l - 1, r - mid - 1);
		printf("Case #%d: %d %d\n", tc, maxAns, minAns);
	}
}