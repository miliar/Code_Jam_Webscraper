//Author: Stefan Toman

#include <iostream>
#include <vector>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		int n, c, m;
		cin >> n >> c >> m;
		vector<int> p(m), b(m);
		vector<int> rides(c, 0), sold(n + 1, 0);
		for(int j = 0; j < m; j++) {
			cin >> p[j] >> b[j];
			rides[b[j]-1]++;
			sold[p[j]]++;
		}
		int maxr = rides[0];
		for(int j = 0; j < c; j++) if(maxr < rides[j]) maxr = rides[j];
		int y = maxr, tsum = 0;
		for(int j = 1; j <= n; j++) {
			tsum += sold[j];
			y = max(y, 1 + (tsum - 1)/j);
		}
		int z = 0;
		for(int j = 1; j <= n; j++) {
			z += max(0, sold[j] - y);
		}

		cout << "Case #" << i << ": " << y << " " << z << endl;
	}
	return 0;
}

