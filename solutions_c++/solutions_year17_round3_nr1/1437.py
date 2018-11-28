

// ~/BAU/ACM-ICPC/Teams/A++/BlackBurn95
// ~/sudo apt-get Accpeted

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <memory.h>
#include <limits.h>
#include <math.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const int N = 1000;
int n, k;
vector<pair<double, double> > pan;
double dp[N][N];
double PI = acos(-1);

double calc(int i, int j) {
	if (i == n) {
		if (j == k) return 0.0;
		return  -1e18;
	}

	double &r = dp[i][j];
	if (abs(r + 1) > 1e-12)
		return r;

	r = calc(i + 1, j);
	r = max(r, calc(i + 1, j + 1) + (2 * PI*pan[i].first*pan[i].second) + (j == 0 ? PI*pow(pan[i].first, 2) : 0));

	return r;
}

int main() {
	std::ios::sync_with_stdio(false);

//#ifdef LOCAL
	//freopen("input.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
//#endif

	int tc;
	scanf("%d", &tc);
	for (int c = 1; c <= tc; c++) {
		scanf("%d%d", &n, &k);

		pan.clear();

		double a, b;
		for (int i = 0; i < n; i++) {
			scanf("%lf%lf", &a, &b);
			pan.push_back(make_pair(a, b));
		}

		sort(pan.begin(), pan.end());
		reverse(pan.begin(), pan.end());

		memset(dp, -1, sizeof(dp));

		printf("Case #%d: %.8f\n", c, calc(0, 0));

	}

	return 0;
}