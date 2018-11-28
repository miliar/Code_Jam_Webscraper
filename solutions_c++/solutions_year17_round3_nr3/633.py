#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
#include <numeric>
#include <functional>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		printf("Case #%d: ", t + 1);
		int N, K;
		cin >> N >> K;
		double U;
		cin >> U;
		vector<double> P(N);
		for (int i = 0; i < N; i++) cin >> P[i];
		sort(P.begin(), P.end());
		P.push_back(HUGE_VAL);
		for (int i = 1; i <= N; i++) {
			double s = accumulate(P.begin(), P.begin() + i, 0.0);
			double ave = (s + U) / i;
			if (ave > P[i]) {
				continue;
			}
			for (int j = 0; j < i; j++) {
				P[j] = ave;
			}
			break;
		}
		double prd = 1.0;
		for (int i = 0; i < N; i++) {
			prd *= P[i];
		}
		printf("%.10f\n", prd);
	}
	return 0;
}
