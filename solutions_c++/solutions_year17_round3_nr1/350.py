#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

pair<int, int> a[1010];

int main() {
	int t, ca = 1;
	scanf("%d", &t);
	while (t--) {
		printf("Case #%d: ", ca++);
		int n, k;
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; i++) {
			scanf("%d%d", &a[i].first, &a[i].second);
		}
		sort(a, a + n, [](pair<int, int> p, pair<int, int> q) {
				return 1ll * p.first * p.second > 1ll * q.first * q.second;});
		long long ma = 0;
		for (int i = 0; i < n; i++) {
			long long res = 1ll * a[i].first * a[i].first + 2ll * a[i].first * a[i].second;
			int cnt = 1;
			for (int j = 0; j < n; j++) if (a[j].first <= a[i].first && i != j) {
				if (cnt == k) break;
				res += 2ll * a[j].first * a[j].second;
				cnt++;
			}
			if (res > ma && cnt == k) {
				ma = res;
			}
		}
		printf("%.10lf\n", 1.0 * ma * acos(-1));
	}
}
