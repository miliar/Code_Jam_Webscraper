#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#define maxn 1010
using namespace std;
int n, m, c;
int a[maxn], b[maxn];
int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int T;
	cin >> T;
	for(int ii = 1; ii <= T; ++ii) {
		scanf("%d%d%d", &n, &c, &m);
		for(int i = 1; i <= m; ++i) {
			int x, y;
			scanf("%d%d", &x, &y);
			a[x]++;
			b[y]++;
		}
		int l = 0;
		for(int i = 1; i <= c; ++i)
			l = max(l, b[i]);
		int r = 1000;
		int ans = 0;
		while(l < r) {
			int mid = (l + r) >> 1;
			bool flag = true;
			int sum = 0;
			ans = 0;
			for(int i = 1; i <= n; ++i) {
				sum += a[i];
				if(sum > mid * i) {
					flag = false;
					break;
				}
				if(a[i] > mid) {
					ans += a[i] - mid;
				}
			}
			if(flag) r = mid;
			else l = mid + 1;
		}
		printf("Case #%d: %d %d\n", ii, l, ans);
		memset(a, 0, sizeof a);
		memset(b, 0, sizeof b);
	}
	return 0;
}