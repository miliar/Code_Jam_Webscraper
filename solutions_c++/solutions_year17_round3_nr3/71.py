#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>


using namespace std;

int next() {int x; cin >> x; return x;}

int main() {

	int tests = next();
	for (int test = 1; test <= tests; test++) {
		int n = next();
		int k = next();

		double u;
		cin >> u;
		vector<double> p(n);
		for (int i = 0; i < n; i++) cin >> p[i];
		p.push_back(1);

		sort(p.begin(), p.end());

		for (int i = 0; i < n; i++) {
			if ((p[i + 1] - p[i]) * (i + 1) <= u) {
				u -= (p[i + 1] - p[i]) * (i + 1);
				for (int j = 0; j <= i; j++) p[j] = p[i + 1];
			} else {
				for (int j = 0; j <= i; j++) p[j] += u / (i + 1);
				u = 0;
				break;
			}
		}

		double answ = 1;
		for (auto pp : p) answ *= pp;

		printf("Case #%d: %10.10f\n", test, answ);
	}
}