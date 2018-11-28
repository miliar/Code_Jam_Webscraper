#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdio>
#include <cassert>
using namespace std;

#define REP(i, n) for (int i = 0; i < (int)(n); i++)

void openFiles() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	//freopen("test.out", "wt", stdout);
#endif
}

const double PI = acos(-1.0);
typedef pair<double, double> pdd;

double area(double r, double h) {
	return 2 * PI * r * h;
}

void solve() {
	int n, k; scanf("%d %d ", &n, &k);
	vector<pdd> v(n);
	REP(i, n) scanf("%lf %lf ", &v[i].first, &v[i].second);
	sort(v.rbegin(), v.rend());

	double bestArea = 0.0;
	for (int i = 0; i <= n - k; i++) {
		vector<double> areas(n - i);		
		for (int j = i + 1; j < n; j++) {
			areas[j - i] = area(v[j].first, v[j].second);
		}
		double ar = 0.0;
		ar += PI * v[i].first * v[i].first;
		ar += area(v[i].first, v[i].second);

		sort(areas.rbegin(), areas.rend());		
		REP(j, k - 1) ar += areas[j];
		bestArea = max(bestArea, ar);
	}

	printf("%.10lf\n", bestArea);
}

int main() {
    openFiles();
    int n; scanf("%d ", &n);
    for (int i = 0; i < n; i++) {
            printf("Case #%d: ", i + 1);
            solve();
    }
    return 0;
}
