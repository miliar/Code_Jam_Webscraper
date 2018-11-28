#include <bits/stdc++.h>
const int INF = ~0U>>1;
using namespace std;
int D, T, N;
struct NODE{
	int K, S;
}p[1002];
int dp[1002][1002];
int main(){
	freopen("t1large.in", "r", stdin);
	freopen("t1large.out", "w", stdout);
	scanf("%d", &T);
	for(int _ = 1; _ <= T; _++){
		scanf("%d%d", &D, &N);
		for(int i = 1; i <= N; i++){
			scanf("%d%d", &p[i].K, &p[i].S);
		}
		p[N + 1].K = D;
		double ans = 1.0 * (D - p[N].K) / (p[N].S);
		for(int i = N - 1; i >= 1; i--){
			if(1.0 * (D - p[i].K) / p[i].S > ans){
				ans = 1.0 * (D - p[i].K) / p[i].S;
			}
		}
		printf("Case #%d: %.12lf\n", _, 1.0 * D / ans);
	}
return 0;
}

