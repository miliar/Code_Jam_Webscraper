#include <bits/stdc++.h>
using namespace std;

const double EPS = 1e-9;
const int LIMIT = 500;

int main() {
	int t;
	scanf ("%d", &t);
	
	for (int tc = 1; tc <= t; tc++) {
		int d, n;
		scanf ("%d %d", &d, &n);
		
		vector <double> totalTime(n);
		vector < pair <int, int> > horses(n);
		
		for (int i = 0; i < n; i++) {
			int k, s;
			scanf ("%d %d", &k, &s);
			horses[i] = make_pair (k, s);
			totalTime[i] = 1.0 * (d - k) / s;
		}
		
		for (int i = 1; i < n; i++)
			totalTime[i] = max (totalTime[i - 1], totalTime[i]);
		
		double l = 0, r = 1e14;
		
		for (int search = 0; search < LIMIT; search++) {
			// simulate
			double mid = (l + r) / 2;
			bool can = true;
			//cerr << "MID: " << mid << endl;
			for (int i = 0; i < n; i++) {
				if (1.0 * d / mid < 1.0 * (d - horses[i].first) / horses[i].second) {
					can = false;
					break;
				}
				
				double time = horses[i].first / (mid - horses[i].second);
				//cerr << i << " " << time << " " << mid * time << " " << (mid * time < EPS + d) << endl;
				if (time < 0) continue;
				if (mid * time < EPS + d) {
					can = false;
					break;
				}
			}
			
			if (!can) {
				r = mid;
			} else l = mid;
		}
		
		printf ("Case #%d: %.15lf\n", tc, r);
	}
	
	return 0;
}