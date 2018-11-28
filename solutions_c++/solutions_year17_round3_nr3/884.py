#include <bits/stdc++.h>

using namespace std;

double P[105];

double solve(){
	int N, K;
	scanf("%d%d", &N, &K);
	double U;
	scanf("%lf", &U);
	for(int i=0;i<N;i++) scanf("%lf", &P[i]);
	
	int x = U*10000;

	for(int i=0;i<x;i++){
		int idx = 0;
		for(int j=0;j<N;j++){
			if(P[j] < P[idx]) idx = j;
		}
		P[idx] += 0.0001;
	}

	// for(int i=0;i<N;i++){
	// 	printf("%d %lf\n", i, P[i]);
	// }

	double ans = 1;
	for(int i=0;i<N;i++) ans *= P[i];

	// if(ans <= 0.000000+0.000001) ans = 0.000001;
	return ans;
}

int main(){
	int T;
	scanf("%d", &T);
	for(int t=1;t<=T;t++){
		double ans = solve();
		printf("Case #%d: ", t);
		printf("%llf", ans);
		printf("\n");
	}
}