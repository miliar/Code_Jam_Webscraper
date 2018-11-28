#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

#define PI 3.141592653589

int next() {int x; cin >> x; return x;}

int main() {

	int tests = next();
	for (int test = 1; test <= tests; test++) {
		int n = next();
		int k = next();

		vector<pair<double, int>> cake;
		for (int i = 0; i < n; i++) {
			int r = next();
			int h = next();
			cake.emplace_back(2 * PI * r * h, r);
		}

		sort(cake.begin(), cake.end());
		reverse(cake.begin(), cake.end());
		
		double sq = 0;
		for (int i = 0; i < k; i++) sq += cake[i].first;
		int maxr = 0;
		for (int i = 0; i < k; i++) maxr = max(maxr, cake[i].second);

		sq += PI * maxr * maxr;

		double maxsq = sq;

		double minf = cake[0].first;
		for (int i = 0; i < k; i++) minf = min(minf, cake[i].first);

		for (int i = k; i < n; i++) if (cake[i].second > maxr) {
			double newsq = sq;
			newsq -= PI * maxr * maxr;
			newsq += PI * cake[i].second * cake[i].second;
			newsq -= minf;
			newsq += cake[i].first;

			if (newsq > maxsq) maxsq = newsq;
		}                  

		printf("Case #%d: %10.10f\n", test, maxsq);
	}
}