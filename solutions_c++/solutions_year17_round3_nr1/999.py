#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>
# define M_PI           3.14159265358979323846  /* pi */

using namespace std;

void main() {
	int tn;
	cin >> tn;

	std::cout << setprecision(6) << fixed;

	for (int t = 1; t <= tn; ++t) {
		int n, k;
		cin >> n >> k;
		// first -> r; second -> h;
		vector<pair<double, double>> cakes = vector<pair<double,double>>(n);
		for (int i = 0; i < n; i++) {
			cin >> cakes[i].first >> cakes[i].second;
		}
		sort(cakes.rbegin(), cakes.rend());

		double best = 0;
		for (int i = 0; i < n; i++) {
			// start from cake i
			double cur = cakes[i].first * cakes[i].first + 2 * cakes[i].first * cakes[i].second;
			vector<pair<double, double>> smaller;
			smaller.reserve(n);
			for (int j = 0; j < n; j++) {
				if (i != j && cakes[i].first >= cakes[j].first) {
					smaller.push_back(cakes[j]);
				}
			}
			sort(smaller.begin(), smaller.end(), [](pair<double, double> a, pair<double, double> b) {
				return a.first * a.second > b.first * b.second;
			});
			if (smaller.size() < k - 1) {
				continue;
			}

			for (int j = 0; j < k - 1; j++) {
				cur += 2 * smaller[j].first * smaller[j].second;
			}

			if (cur > best) {
				best = cur;
			}
		}

		cout << "Case #" << t << ": " << best * M_PI << endl;
		//printf(" %0.6lf", dist[v]);
	}
}