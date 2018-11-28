#include <bits/stdc++.h>

using namespace std;

// Only the largest radius matters. From there select the tallest pancakes.

int main() {
    std::cout << std::fixed;
    std::cout << std::setprecision(9);
    
	int T;
	cin >> T;
	for (int ii = 0; ii < T; ++ii) {
		int N, K;
		cin >> N >> K;

		vector<vector<double>> RHA(N, vector<double>(3));
		for (int nn = 0; nn < N; ++nn) {
			cin >> RHA[nn][0] >> RHA[nn][1];
			RHA[nn][2] = 2 * M_PI * RHA[nn][0] * RHA[nn][1];
		}
		sort(RHA.begin(), RHA.end(), 
			[](const vector<double>& v1, const vector<double>& v2) { 
				return v1[2] > v2[2];
			});
		double maxR = 0., area = 0.;
		for (int jj = 0; jj < K - 1; ++jj) {
			// vertical area
			area += RHA[jj][2];
			maxR = max(maxR, RHA[jj][0]);
		}
		// horizontal area
		area += M_PI * maxR * maxR;
		double maxAreaJJ = 0.;
		for (int jj = K - 1; jj < N; ++jj) {
			double areaJJ = 0;
			if (RHA[jj][0] > maxR) areaJJ += M_PI * ((RHA[jj][0] * RHA[jj][0]) - (maxR * maxR));
			areaJJ += 2 * M_PI * RHA[jj][0] * RHA[jj][1];
			maxAreaJJ = max(maxAreaJJ, areaJJ);
		}
		area += maxAreaJJ;
		cout << "Case #" << ii + 1 << ": " << area << endl;
	}
	return 0;
}