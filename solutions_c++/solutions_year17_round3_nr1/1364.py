#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

#define lint long long
#define INF 1000000000
#define MOD 1337377

#define PB push_back
#define MP make_pair

int T;

struct st {
	int h, r;
};

bool operator < (const st &a, const st &b) {
	return a.r > b.r;
}

st p[1005];
double d[1005][1005];

const double PI = 3.1415926535897932384;

void solve() {
	int n, k;
	scanf("%d %d", &n, &k);

	for (int i = 1; i <= n; ++i) {
		scanf("%d %d", &p[i].r, &p[i].h);
	}

	sort(p + 1, p + 1 + n);

	double ans = 0;
	for (int i = 1; i <= n; ++i) {
		double cur = PI*(double)p[i].r*(double)p[i].r + 2*PI*(double)p[i].r*(double)p[i].h;
		vector <double> mn;
		for (int j = i + 1; j <= n; ++j) {
			mn.PB((double)p[j].r*(double)p[j].h);
		}
		sort(mn.begin(), mn.end());
		if (mn.size() < k - 1) {
			break;
		}

		for (int j = (int)mn.size() - 1; j >= (int)mn.size() - (k - 1); --j) {
			cur += 2 * PI * mn[j];
		}

		ans = max(ans, cur);
	}


	printf("Case #%d: %.9f\n", ++T, ans);
}

int main() {

	int tc;

	scanf("%d", &tc);

	while (tc--) {
		solve();
	}

	return 0;
}