#include <bits/stdc++.h>
using namespace std;
const int MAX = 110;
double D[MAX][MAX], ans[MAX], E[MAX], S[MAX], DD[MAX][MAX];
int N, Q;
priority_queue<pair<double, int> > q;
int main(){
	int t, cs = 0;
	scanf("%d", &t);
	while(t--){
		++cs;
		printf("Case #%d: ", cs);
		scanf("%d%d", &N, &Q);
		for(int i=1; i<=N; ++i){
			scanf("%lf%lf", &E[i], &S[i]);
		}
		for(int i=1; i<=N; ++i){
			for(int j=1; j<=N; ++j){
				scanf("%lf", &D[i][j]);
				if(D[i][j] == -1) D[i][j] = 10000000000000; 
			} D[i][i] = 0;
		}
		for(int k=1; k<=N; ++k){
			for(int i=1; i<=N; ++i){
				for(int j=1; j<=N; ++j){
					D[i][j] = min(D[i][j], D[i][k] + D[k][j]);
				}
			}
		}
		for(int i=1; i<=N; ++i){
			for(int j=1; j<=N; ++j){
				if(D[i][j] <= E[i]){
					DD[i][j] = D[i][j] / S[i];
				}
				else DD[i][j] = 10000000000000; 
			}
		}
		for(int k=1; k<=N; ++k){
			for(int i=1; i<=N; ++i){
				for(int j=1; j<=N; ++j){
					DD[i][j] = min(DD[i][j], DD[i][k] + DD[k][j]);
				}
			}
		}
		while(Q--){
			int X, Y; 
			scanf("%d%d", &X, &Y);
			printf("%0.8lf ", DD[X][Y]);
		}
		printf("\n");
	}	
}