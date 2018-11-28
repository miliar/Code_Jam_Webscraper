#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <utility>

using namespace std;

typedef pair<long long, long long> cyl;

const double PI = acos(-1);


long long dp[1005][1005] = {{0}};
vector<cyl> cake;
int n, k;

long long circle(cyl x) {
	return x.first * x.first;
}

long long ring(cyl x) {
	return 2 * x.first * x.second;
}

long long f(int st, int req) {
	if(st + req > n) return 1LL * 100000 * 1000000 * 100;
	if(dp[st][req] > 0) return dp[st][req];
	long long &ret = dp[st][req];
	ret = ring(cake[st]);
	if(req > 1)
		for(int i = st + 1;i + req  - 1 <= n;i++) 
			ret = max(ret, ring(cake[st]) + f(i, req - 1));
	//printf("%d %d %f\n", st, req, ret);
	return ret;
}

void sol() {
	memset(dp, -1, sizeof(dp));
	cake.clear();
	scanf("%d%d", &n, &k);
	for(int i = 0;i < n;i++) {
		long long x, y; scanf("%lld%lld", &x, &y);
		cake.push_back(cyl(x, y));
	}
	sort(cake.begin(), cake.end());
	reverse(cake.begin(), cake.end());
	long long a = 0;
	for(int i = 0;i + k <= n;i++) a = max(a, f(i, k) + circle(cake[i]));
	printf("%.12f\n", a * PI);
}

int main() {
	int t; scanf("%d", &t);
	for(int i= 1;i <= t;i++) printf("Case #%d: ", i), sol();
}
