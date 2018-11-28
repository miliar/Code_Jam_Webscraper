#include <bits/stdc++.h>
using namespace std;

const int N = 1002;
int t, n, k;
pair<double, double> p[N];
double dp[N][N];
const double PI = acos(-1);


double go(int i, int j){
	if(i == n){
		if(j == k) return 0;
		else return -1000000000000000.0;
	}
	if(dp[i][j] != -1) return dp[i][j];
	
	double r1 = go(i+1, j);
	double r2 = go(i+1, j+1) + 2.0*PI*p[i].first*p[i].second;
	if(j == 0) r2 += PI*p[i].first*p[i].first;
	
	return dp[i][j] = max(r1, r2);
}

bool cmp(pair<double, double> a, pair<double, double> b){
	if(a.first == b.first){
		return a.second > b.second;
	}
	return a.first > b.first;
}

int main(void){
	scanf("%d", &t);
	
	for(int caso = 1; caso <= t; caso++){
		scanf("%d%d", &n, &k);
	
		for(int i = 0; i < n;i++){
			scanf("%lf%lf", &p[i].first, &p[i].second);
		}
		
		sort(p, p+n, cmp);
	
		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++){
				dp[i][j] = -1;
			}
		}
		
		double res = go(0,0);
		
		printf("Case #%d: %lf\n", caso, res);
	}

	return 0;
}
