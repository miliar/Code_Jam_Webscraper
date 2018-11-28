#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <map>
#include <string>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <bitset>
using namespace std;

typedef long long LL;
#define pb push_back

int N;
double D, K[1010], S[1010];

int main () {
	int T;
	scanf("%d", &T);
	for(int tt = 1; tt <= T; ++tt){
		// cout << tt<<" xx" <<endl;
		cin >> D >> N;
		for(int i = 0; i < N; ++i){
			scanf("%lf%lf", &K[i], &S[i]);
			// printf("%.0f %.0f\n", K[i], S[i]);
		}
		double ans = 1e9, big = 0;
		for(int i = 0; i < N; ++i){
			double c = (D-K[i])/S[i];
			if(c > big) big = c;
		}
		ans = D/big;
		// double L = 0, R = 10e9+1, M;
		// int cnt = 2000;
		// while(cnt--){
		// 	M = (L+R)/2.0;
		// 	int ok = 0;
		// 	double cost = D/M;
		// 	for(int i = 0; i < N; ++i){
		// 		double cc = (D-K[i])/S[i];
		// 		if(cost < cc){
		// 			ok = 1; break;
		// 		} 
		// 	}
		// 	if(ok){
		// 		R = M;
		// 	}
		// 	else L = M;
		// 	// cout << ok <<endl;
		// 	// printf("%.7f %.7f %.7f\n", L, R, (R-L));
		// }
		printf("Case #%d: %.7f\n", tt,ans);
	}
}