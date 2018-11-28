#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;
int n, p;
int a[120];
int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int T;
	cin >> T;
	for(int ii = 1; ii <= T; ++ ii) {
		scanf("%d%d", &n, &p);
		for(int i = 1; i <= n; ++i) {
			scanf("%d", a + i);
			a[i] %= p;
		}
		sort(a + 1, a + n + 1);
		int i = 1;
		for(;i <= n && a[i] == 0; ++i);
		int ans = i - 1;
		if(p == 2) {
			ans += (n - i + 2) / 2;
		}
		else if(p == 3) {
			int sum[3] = {0, 0, 0};
			for(;i <= n; ++i)
				sum[a[i]]++;
			if(sum[1] > sum[2]) {
				ans += sum[2];
				ans += (sum[1] - sum[2] + 2) / 3;
			}
			else {
				ans += sum[1];
				ans += (sum[2] - sum[1] + 2) / 3;
			}
		}
		else {
			int sum[4] = {0, 0, 0, 0};
			for(;i <= n; ++i)
				sum[a[i]]++;
			ans += sum[2] / 2;
			sum[2] &= 1;
			ans += min(sum[1], sum[3]);
			sum[1] = max(sum[1] - sum[3], sum[3] - sum[1]);
			if(sum[2]) {
				if(sum[1] <= 2) {
					ans++;
				}
				else {
					ans += (sum[1] + 1) / 4;
				}
			}
			else ans += (sum[1] + 3) / 4;
		}
		printf("Case #%d: %d\n", ii, ans);
	}
	return 0;
}