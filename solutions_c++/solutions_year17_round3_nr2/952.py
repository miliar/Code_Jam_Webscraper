#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

pair<int, int> a[100], b[100];

int main() {
	int t;
	scanf("%d", &t);
	for (int _ = 1; _ <= t; _++) {
		int ac, aj;
		scanf("%d%d", &ac, &aj);
		for (int i = 0; i < ac; i++) {
			scanf("%d%d", &a[i].first, &a[i].second);
		}
		for (int i = 0; i < aj; i++) {
			scanf("%d%d", &b[i].first, &b[i].second);
		}
		sort(a, a + ac);
		sort(b, b + aj);
		int ans = 2;
		if (ac == 2) {
			if (a[1].second - a[0].first > 720 && a[1].first - a[0].second < 720) {
				ans = 4;
			}
		} else if (aj == 2) {
			if (b[1].second - b[0].first > 720 && b[1].first - b[0].second < 720) {
				ans = 4;
			}
		}
		printf("Case #%d: %d\n", _, ans);
	}
}
