#include <algorithm>
#include <iostream>
#include <functional>
#include <vector>
using namespace std;

const double M_PI = 3.141592653589793238462643383279502884197169399375105820974944592307816406286;

int main() {
	int T;
	cin >> T;
	cout.setf(std::ios_base::fixed, std::ios_base::floatfield);
	cout.precision(9);
	for (int t = 1; t <= T; t += 1) {
		int n, k;
		cin >> n >> k;
		vector<pair<double, double>> pancakes;
		pancakes.resize(n);
		for (int i = 0; i < n; i += 1) {
			cin >> pancakes[i].first >> pancakes[i].second;
		}

		sort(pancakes.begin(), pancakes.end());
		vector<double> sideArea;
		for (int i = 0; i < n; i += 1)  {
			double side = 2 * pancakes[i].first;
			side *= pancakes[i].second;
			sideArea.push_back(side);
		}
		double max = 0;
		for (int i = k-1; i < n; i += 1) {
			double exposedPart = pancakes[i].first * pancakes[i].first + sideArea[i];
			vector<double> sideAreaUpToIth;
			sideAreaUpToIth.resize(i);
			copy(sideArea.begin(), sideArea.begin() + i, sideAreaUpToIth.begin());
			sort(sideAreaUpToIth.begin(), sideAreaUpToIth.end(), greater<double>());
			for (int j = 0; j < k - 1; j += 1) {
				exposedPart += sideAreaUpToIth[j];
			}
			if (exposedPart > max) {
				max = exposedPart;
			}
		}
		double result = M_PI * max;
		cout << "Case #" << t << ": " << result << endl;
		}
	return 0;
}