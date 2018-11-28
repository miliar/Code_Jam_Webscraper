#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define debug 1

#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef pair<int, int> pii;
typedef long long lint;

const int inf = 0x7fffffff;
const int Size = 1000 * 1000 + 1;
char buffer[Size];


void init() {

}

void clear(int i) {

}

const double pi = acos(-1.);

double sq(double r, double h) {
	return h * 2 * pi * r;
}

const int size = 1001;

double dp[size][size][2];

int solution(int nTest) {
	int n, k;
	scanf("%d%d", &n, &k);
	vector<pii> v;
	For (i, 0, n) {
		int r, h;
		scanf("%d%d", &r, &h);
		v.pb(mp(r, h));
	}
	sort(all(v));
	For (i, 0, n + 1) {
		For (j, 0, k + 1) {
			dp[i][j][0] = dp[i][j][1] = 0;
		}
	}
	dp[0][1][1] = sq(v[0].first, v[0].second);
	For (i, 1, n) {
		For (j, 1, k + 1) {
			dp[i][j][0] = max(dp[i][j][0], dp[i-1][j][0]);
			dp[i][j][0] = max(dp[i][j][0], dp[i-1][j][1]);
			dp[i][j][0] = max(dp[i][j][0], dp[i][j-1][0]);

			double s = sq(v[i].first, v[i].second);
			dp[i][j][1] = max(dp[i][j][1], dp[i-1][j-1][0] + s);
			dp[i][j][1] = max(dp[i][j][1], dp[i-1][j-1][1] + s);
			dp[i][j][1] = max(dp[i][j][1], dp[i][j-1][1]);
		}
	}
	double res = 0;
	For (i, 0, n) {
		double r = v[i].first;
		double s = pi * r * r;
		res = max(res, s + dp[i][k][1]);
	}
	printf("%.8lf\n", res);






	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 999999;
	scanf("%d", &n);
	init();
	For(i, 0, n) {
		printf("Case #%d: ", i + 1);
		clear(i);
		solution(i);
	}

	return 0;
}
	
