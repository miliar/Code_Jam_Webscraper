#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <iomanip>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>
#include <list>


using namespace std;

const double E = 1e-6;

int main() {
#ifdef _DEBUG
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";

		int n, k;
		cin >> n >> k;
		double u;
		cin >> u;

		vector<double> p;
		for (int i = 0; i < n; i++) {
			double pp;
			cin >> pp;
			p.push_back(pp);
		}
		p.push_back(1.0);

		sort(p.begin(), p.end());

		int acc = 0;
		double pp = 0;
		for (int i = 0; i < n && u > E; i++) {
			acc++;
			pp = p[i];
			double dp = p[i + 1] - pp;
			double dpu = dp * acc;

			if (dpu < u) {
				pp += dp;
				u -= dp * acc;
			}
			else {
				pp += u / acc;
				u = -E;
			}
		}

		double res = 1.0;
		for (int i = 0; i < acc; i++) {
			res *= pp;
		}

		for (int i = acc; i < n; i++) {
			res *= p[i];
		}

		cout << fixed << setprecision(9) << res << endl;
	}

	return 0;
}