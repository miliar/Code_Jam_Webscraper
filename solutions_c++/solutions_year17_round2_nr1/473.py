#include <bits/stdc++.h>
using namespace std;

// why am I so weak

int main() {
	int _t;

	scanf("%d", &_t);

	for (int _ = 0; _ < _t; _++) {
		printf("Case #%d: ", _ + 1);

		int d, n;
		scanf("%d %d", &d, &n);

		int k[n], s[n];

		for (int i = 0; i < n; i++) {
			scanf("%d %d", &k[i], &s[i]);
		}

		vector<int> vec(n);

		for (int i = 0; i < n; i++) vec[i] = i;

		sort(vec.begin(), vec.end(), [&] (int u, int v) {
			return k[u] > k[v];
		});

		double t = 0.;

		for (auto u : vec) {
			t = max(t, 1. * (d - k[u]) / s[u]);
		}

		printf("%.10lf\n", 1. * d / t);
	}

	return 0;
}
