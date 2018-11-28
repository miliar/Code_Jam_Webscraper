#include <bits/stdc++.h>
using namespace std;

#define pi acos(-1)
inline double sqr(double x) {return x*x;}
const int MAX = 1010;
const double inf = 0x3f3f3f3f;
pair<int, int> a[MAX];
double memo[MAX][MAX][2];
int n, m;
bool mycomp(pair<int, int> &p1, pair<int, int> &p2) {
	if(p1.first != p2.first)return p1.first > p2.first;
	return p1.second > p2.second;
}
double pd(int idx, int k, int taken) {
	if(k == m || idx == n)return 0;
	double &res = memo[idx][k][taken];
	if(res >= 0)return res;
	res = -inf;
	if(taken) {
		res = max(res, max(pd(idx+1, k, taken) , pd(idx+1, k+1, taken) + 2*pi*a[idx].first*a[idx].second));
	}else {
		res = max(res, max(pd(idx+1, k, taken), pd(idx+1, k+1, 1) + 2*pi*a[idx].first*a[idx].second + pi*sqr(a[idx].first)));
	}
	return res;
}
double solve() {
	scanf("%d %d", &n, &m);
	for(int i = 0; i < n; ++i) {
		scanf("%d %d", &a[i].first, &a[i].second);
	}
	for(int i = 0; i <= n; ++i) {
		for(int j = 0; j <= n; ++j) {
			for(int k = 0; k < 2; ++k){
				memo[i][j][k] = -10;
			}
		}
	}
	sort(a, a+n, mycomp);
	return pd(0, 0, 0);
}
int main() {
	int tc;
	scanf("%d", &tc);
	for(int i = 1; i <= tc; ++i)printf("Case #%d: %.20lf\n", i,  solve());
}
