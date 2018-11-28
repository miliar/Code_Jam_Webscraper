#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <unordered_map>
#include <unordered_set>

#define pb push_back
#define mp make_pair

using big = long long;

using namespace std;

const double eps = 1e-10;
const double inf = 2e10;
double d;
int n;
using pdd = pair<double, double>;

double getT(const pdd &t1, const pdd &t2) {
	if (fabs(t1.second - t2.second) < eps) {
		return inf;
	}
	double meet = (t2.first - t1.first) / (t2.second - t1.second);
	if (meet < t1.first / t1.second && meet < t2.first / t1.second) {
		return meet;
	}
	return inf;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cas;
	scanf("%d", &cas);

	for (int cass = 1; cass <= cas; ++cass) {
		printf("Case #%d: ", cass);
		cerr << "case " << cass << endl;
		scanf("%lf%d", &d, &n);
		vector<pair<double, double>> a;
		double maxT = 0;
		for (int i = 0; i < n; ++i) {
			double x, y;
			scanf("%lf%lf", &x, &y);
			x = d - x;
			a.emplace_back(x, y);
			maxT = max(maxT, x / y);
		}
		double ans = d / maxT;
		printf("%.6f\n", ans);
	}
	fclose(stdin);
	fclose(stdout);
}

