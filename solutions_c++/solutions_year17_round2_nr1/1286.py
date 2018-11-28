#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int main() {
	int tt; cin >> tt;
	for (int t = 1; t <= tt; t++) {
		int d, n;
		scanf("%d %d", &d, &n);
		double maxtime = 0;
		for (int i = 0; i < n; i++) {
			int a, b; scanf("%d %d", &a, &b);
			int dis = d-a;
			double time = dis * 1.0 / b;
			maxtime = max(maxtime, time);
		}
		printf("Case #%d: %.6lf\n", t, d / maxtime);
	}
}