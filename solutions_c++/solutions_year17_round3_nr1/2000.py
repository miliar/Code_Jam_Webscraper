#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <cmath>

const double PIE = 3.14159265358979323846;

int main() {

	int t;
	std::cin >> t;

	for (auto i = 1; i <= t; i++) {
		int N, K;
		std::cin >> N >> K;

		struct prodMap {
			int idx;
			long long R;
			long long H;
			long long product;
		};

		struct radMap {
			int idx;
			long long R;
			long long H;
		};

		std::vector<prodMap> pMap;
		std::vector<radMap> rMap;

		for (auto p = 0; p < N; p++) {
			prodMap pm;
			radMap rm;

			std::cin >> pm.R >> pm.H;

			pm.idx = p;
			rm.idx = p;

			pm.product = pm.R * pm.H;
			rm.R = pm.R;
			rm.H = pm.H;

			pMap.push_back(pm);
			rMap.push_back(rm);
		}

		sort(pMap.begin(), pMap.end(), [](prodMap p1, prodMap p2) {
			if (p1.product > p2.product) {
				return true;
			}
			else if (p1.product == p2.product) {
				return p1.R > p2.R;
			}
			else
				return false;
		});

		sort(rMap.begin(), rMap.end(), [](radMap r1, radMap r2) {
			if (r1.R > r2.R) {
				return true;
			}
			else if (r1.R == r2.R) {
				return r1.H > r2.H;
			}
			else {
				return false;
			}
		});

		double ret = 0;

		for (auto chR = 0; chR < N; chR++) {

			double val = PIE * rMap[chR].R * rMap[chR].R;
			val += 2.0 * PIE * rMap[chR].R * rMap[chR].H;

			int chosen = 0;

			for (auto ch = 0; chosen < K - 1; ch++) {

				if (pMap[ch].idx == rMap[chR].idx) {
					continue;
				}

				chosen++;

				val += 2.0 * PIE * pMap[ch].product;
			}

			ret = std::max(ret, val);

		}

		printf("Case #%d: %lf\n", i, ret);

		//std::cout << "Case #" << i << ": " <<  << ret << "\n";
	}

	getchar();

	return 0;

}