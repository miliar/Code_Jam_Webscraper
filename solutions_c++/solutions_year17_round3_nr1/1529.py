#include <cstdio>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <utility>
#define mod 1000000007
const double PI  = M_PI;
using namespace std;
struct cylinder {
	double r;
	double h;
};	
bool cylinder_sorter(cylinder const& lhs, cylinder const& rhs) {
    return lhs.r < rhs.r;
}
double area(double r, double h) {
	return ((double)2.0)*PI*(r*r + r*h);
}
double maxArea(int i, int k, int N, int K, cylinder c[], map<pair<int, int>, double> &Mem) {
	pair<int, int> p = make_pair(i, k);
	if(Mem.find(p) != Mem.end())
		return Mem[p];
	if(i == N) {
		if(k == K)
			return 0;
		else
			return -1e15;
	}
	Mem[p] = max(maxArea(i + 1, k, N, K, c, Mem), area(c[i].r, c[i].h) - (k == K - 1?1:2)*(PI*c[i].r*c[i].r) + maxArea(i + 1, k + 1, N, K, c, Mem));
	return Mem[p];
}

double dpfunc(int N, int K, cylinder c[]) {
	double dp[N + 1][K + 1];
	for(int k = 0; k < K; k++)
		dp[N][k] = -1e15;
	dp[N][K] = 0.0;
	for(int i = N - 1; i >= 0; i--) {
		for(int k = K - 1; k >= 0; k--) {
			dp[i][k] = max(dp[i + 1][k], area(c[i].r, c[i].h) - ((k == K - 1?1:2))*(PI*c[i].r*c[i].r) + dp[i + 1][k + 1]);
		}
	}
	return dp[0][0];
}
int main(int argc, char const *argv[]) {
	int T = 0;
	scanf("%d", &T);
	for(int t = 0; t < T; t++){
		double sol = 0.0;
		int N = 0, K = 0;
		scanf("%d %d", &N, &K);
		cylinder C[N];
		for(int n = 0; n < N; n++) {
			scanf("%lf %lf", &C[n].r, &C[n].h);
		}
		sort(C, C + N, cylinder_sorter);
		map<pair<int, int>, double> Mem;
		// /double sol1 = maxArea(0, 0, N, K, C, Mem);
		double sol2 = dpfunc(N, K, C);
		// if(abs(sol1 - sol2) > 1e7)
		// 	printf(":(\n");
		// // cout << sol << endl;
		printf("Case #%d: %.17lf\n", t+1, sol1);

	}
	return 0;
}