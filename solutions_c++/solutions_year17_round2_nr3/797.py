#include <algorithm>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>
#include <vector>

using namespace std;

int main() {
	int t;
	cin >> t;
	cout << setprecision(25);
	for (int testCase = 1; testCase <= t; testCase++) {
		int n, q;
		cin >> n >> q;
		vector<int> distance(n), speed(n);
		vector<int> src(q), dest(q);
		vector<vector<int>> adjMatrix(n, vector<int>(n));
		for (int i = 0; i < n; i++) {
			cin >> distance[i] >> speed[i];
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> adjMatrix[i][j];
			}
		}
		for (int i = 0; i < q; i++) {
			cin >> src[i] >> dest[i];
		}
		// Only for small tests:
		vector<long double> timeToReach(n, std::numeric_limits<long double>::infinity());
		timeToReach[0] = 0.L;
		for (int i = 0; i < n; i++) {
			long double timeInit = timeToReach[i];
			long double curSpeed = speed[i];
			int dist = 0;
			int maxDist = distance[i];
			for (int j = i + 1; j < n; j++) {
				dist += adjMatrix[j - 1][j];
				if (dist > maxDist)
					break;
				long double newTime = timeInit + dist / curSpeed;
				if (newTime < timeToReach[j])
					timeToReach[j] = newTime;
			}
		}
		cout << "Case #" << testCase << ": ";
		cout << timeToReach[n - 1] << '\n';
	}
	return 0;
}
