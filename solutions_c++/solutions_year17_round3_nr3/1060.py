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

	for (auto c = 1; c <= t; c++) {
		int N, K;
		std::cin >> N >> K;

		double u;

		std::cin >> u;

		std::vector<double> prob(N);

		for (auto p = 0; p < N; p++) {
			std::cin >> prob[p];
		}

		sort(prob.begin(), prob.end());

		prob.push_back(1.0);

		int i = 1;

		while (u > 0 && i <= N) {
			
			auto toAdd = std::min(u, i * (prob[i] - prob[i - 1]));

			u -= toAdd;

			for (auto j = 0; j < i; j++) {
				prob[j] += toAdd / i;
			}
				
			i++;
		}

		double ret = 1.0;

		for (i = 0; i < N; i++) {
			ret *= prob[i];
		}

		printf("Case #%d: %lf\n", c, ret);

		//std::cout << "Case #" << i << ": " <<  << ret << "\n";
	}

	getchar();

	return 0;

}