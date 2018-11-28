#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <math.h>

using namespace std;

#define pi M_PI

double dp[1001][1001];
vector<pair<double, double> > vec;
int n, k;

double f(int cur, int left){
	if(left == 0) return 0;
	if(cur == n-1) return 0;
	if(dp[cur][left] != -1) return dp[cur][left];
	double A = 2 * pi * vec[cur + 1].first * vec[cur + 1].second;
	return dp[cur][left] = max(f(cur+1, left), f(cur + 1, left-1)  + A);
}
int main(){

	int T; cin >> T;
	for(int tc = 1; tc <= T; tc++){
		 cin >> n >> k;
		vec.clear();
		double h[n], r[n];
		for(int i = 0; i < n; i++){
			cin >> r[i] >> h[i];
			vec.push_back(make_pair(r[i], h[i]));
		}
		
		sort(vec.begin(), vec.end());
		reverse(vec.begin(), vec.end());

		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				dp[i][j] = -1;
			}
		}

		double ans = 0.0;
		for(int i = 0; i < n; i++){
			double z = pi * vec[i].first * vec[i].first;
			z += 2 * pi * vec[i].first * vec[i].second;
			ans = max(f(i, k-1) + z, ans);
		}

		
		printf("Case #%d: %.7f\n", tc, ans);

	}

	return 0;
}