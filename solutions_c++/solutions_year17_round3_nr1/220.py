#include <iostream>
#include <stdio.h>
#include <string>
#include <memory.h>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <time.h>
#include <assert.h>
#include <cmath>
#include <stack>
#include <string.h>
#include <sstream>
#include <algorithm>
using namespace std;
typedef long long ll;
const int N = 1000;
int n, k;
pair<int, int> v[N];
double dp[N][N+1];
const double PI = acos(-1.0);
double cir(pair<int, int> v) {
	return 2 * PI*v.first*v.second;
}
double area(pair<int, int> v) {
	return PI*v.first*v.first;
}
double calc(int i, int k) {
	if (!k)
		return 0;
	if (i == n)
		return -1e18;
	double &ret = dp[i][k];
	if (ret == ret)
		return ret;
	ret = calc(i + 1, k);
	ret = max(ret, calc(i + 1, k - 1) + cir(v[i]));
	return ret;
}
int main()
{
	//freopen("src.txt", "r", stdin);
	freopen("C:/Users/ASUS/Downloads/A-large.in", "r", stdin);
	freopen("C:/Users/ASUS/Downloads/A-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; ++T) {
		printf("Case #%d:", T);
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; ++i)
			scanf("%d%d", &v[i].first, &v[i].second);
		sort(v, v + n);
		reverse(v, v + n);
		memset(dp, -1, sizeof(dp));
		double res = 0;
		for (int i = 0; i < n; ++i)
			res = max(res, area(v[i]) + cir(v[i]) + calc(i + 1, k - 1));
		printf(" %.9lf\n", res);
	}
	return 0;
}