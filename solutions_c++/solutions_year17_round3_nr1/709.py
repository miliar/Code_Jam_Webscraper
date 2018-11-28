#include <iostream>
#include <cmath>
#include <queue>
#include <vector>

using namespace std;

void solve() {
	int N, K;
	cin >> N >> K;
	vector<double> hs;
	vector<double> rs;
	for (int i = 0; i < N; i++) {
		int r, h;
		cin >> r >> h;
		hs.push_back(2* 3.141592653589793238462643*r*h);
		rs.push_back(r);
	}
	double maxSyrup = 0;
	for (int i = 0; i < N; i++) {
		double maxr = rs[i];
		double maxh = hs[i];
		priority_queue<double> pq(hs.begin(), hs.end());
		bool lastused = false;
		double height = maxh;
		for (int j = 0; j < K - 1; j++) {
			double h = pq.top();
			if (!lastused && h == maxh) {
				lastused = true;
				j--;
			}
			else {
				height += h;
			}
			pq.pop();
		}
		double surface = 3.141592653589793238462643*pow(maxr, 2);
		maxSyrup = surface + height > maxSyrup ? surface + height : maxSyrup;
	}
	printf("%.9lf", maxSyrup);
}

int  main() {
	int k;
	cin >> k;
	for (int i = 0; i < k; i++) {
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
	return 0;
}