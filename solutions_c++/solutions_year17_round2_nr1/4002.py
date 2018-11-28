#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

typedef pair<int, int> ii;

int main(void) {
	int t;
	scanf("%d", &t);

	// Para cada caso de teste.
	for (int tc = 1; tc <= t; tc++) {
		int n, d;
		scanf("%d %d", &d, &n);

		vector<ii> h(n);

		for (int i = 0; i < n; i++) {
			scanf("%d %d", &h[i].first, &h[i].second);
		}

		sort(h.begin(), h.end());

		double mspeed = 1.0 / 0.0;

		// Para cada cavalo i.
		for (int i = 0; i < n - 1; i++) {
			int mini_horse = -1;
			int mini_cpoint = -1;

			// Para cada cavalo j na frente de i.
			for (int j = i + 2; j < n; j++) if (h[i].second > h[j].second) {
				double crossing_time = (h[i].first - h[j].first) / (h[i].second - h[j].second);
				double crossing_point = (h[i].first + h[i].second * crossing_time);

				if (mini_horse == -1 or crossing_point < mini_cpoint) {
					mini_horse = j;
					mini_cpoint = crossing_point;
				}
			}

			if (mini_cpoint != -1 and mini_cpoint < d) {
				h[i].first = mini_cpoint;
				h[i].second = h[mini_horse].second;
			}

			double time_remaining = (d - h[i].first) / double(h[i].second);
			mspeed = min(mspeed, d / time_remaining);
		}

		// Pego o último cavalo.
		double time_remaining = (d - h.back().first) / double(h.back().second);
		mspeed = min(mspeed, d / time_remaining);

		printf("Case #%d: %.6lf\n", tc, mspeed);
	}

	return 0;
}