#include <cstdio>
#include <algorithm>
#include <vector>
#define PI 3.1415926535897932384626433832795028841971
using namespace std;

typedef long long lint;
typedef double db;
const int N = 1005;

typedef pair < lint, lint > ll;

double cir(lint r) {
	return r*r*PI;
}

double side(lint r, lint h) {
	return 2 * PI*r*h;
}

double get(ll a) {
	double ret = cir(a.first) + side(a.first,a.second);
	return ret;
}

double dp[N][N];//n개 중 k개 사용. 

void init() {
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < N; ++j)
			dp[i][j] = 0;
}
int n, k;
double go(vector < ll > &v) {
	init();
	sort(v.rbegin(), v.rend());
	dp[0][1] = get(v[0]);
	for (int i = 0; i < n - 1; ++i) {
		//i+1추가 or 추가 x
		for (int j = 0; j < n; ++j) {
			dp[i + 1][j] = max(dp[i + 1][j], dp[i][j]);
			if (j < k) {
				double next = dp[i][j] + side(v[i+1].first,v[i + 1].second);
				if (j == 0)next += cir(v[i + 1].first);
				dp[i + 1][j + 1] = max(dp[i + 1][j + 1], next);
			}
		}
	}
	return dp[v.size() - 1][k];
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i=1;i<=t;++i) {
		vector < ll > v;
		scanf("%d%d", &n,&k);
		for (int i = 0; i < n; ++i) {
			lint x, y;
			scanf("%lld%lld", &x, &y);
			v.push_back(ll(x, y));
		}
		printf("Case #%d: %.9lf\n",i, go(v));
	}
	return 0;
}