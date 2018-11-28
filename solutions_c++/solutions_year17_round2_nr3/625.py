#include <cstdio>
#include <math.h>
#include <algorithm>
#include <queue>
#include<utility>

using namespace std;

long long int t, T;
long long int N, Q;
long long int E[150], S[150];
long long int D[150][150];
long long int D2[150][150];
double D3[150][150];
double ANS[150][150];
long long int U[150], V[150];
double time[150][150];

int main() {
	long long int i, j;
	scanf("%lld", &T);
	for(t = 1; t <= T; t++) {
		scanf("%lld %lld", &N, &Q);
		for(i = 0; i < N; i++) {
			scanf("%lld %lld", &E[i], &S[i]);
		}
		for(i = 0; i < N; i++) {
			for(j = 0; j < N; j++) {
				scanf("%lld", &D[i][j]);
				D2[i][j] = -1;
				if(i == j) {
					D[i][j] = 0;
					D2[i][j] = 0;
				}
			}
		}
		for(i = 0; i < Q; i++) {
			scanf("%lld %lld", &U[i], &V[i]);
		}
		for(i = 0; i < N; i++) {
			priority_queue<pair<long long int,long long int>,vector< pair<long long int,long long int> >,greater< pair<long long int,long long int> > > pq;
			pq.push(make_pair(0, i)); 
			while(!pq.empty()) {
				long long int k = pq.top().second;
				pq.pop();
				for(j = 0; j < N; j++) {
					if(D[k][j] == -1) continue;
					if(D2[i][j] == -1 || D2[i][k] + D[k][j] < D2[i][j]) {
						D2[i][j] = D2[i][k] + D[k][j]; 
						pq.push(make_pair(D2[i][j], j));
					}
				}
			}
		}
		for(i = 0; i < N; i++) {
			for(j = 0; j < N; j++) {
				if(D2[i][j] >= 0 && D2[i][j] <= E[i]) {
					D3[i][j] = D2[i][j] * 1.0 / S[i];
				} else {
					D3[i][j] = -1;
				}
			}
		}
		for(i = 0; i < N; i++) {
			//printf("%d, %d : ", E[i], S[i]);
			for(j = 0; j < N; j++) {
				//printf("%d->%lf ", D2[i][j], D3[i][j]);
				ANS[i][j] = -1;
				if(i == j) ANS[i][j] = 0;
			}
			//printf("\n");
		}
		for(i = 0; i < N; i++) {
			priority_queue<pair<double,long long int>,vector< pair<double,long long int> >,greater< pair<double,long long int> > > pq;
			pq.push(make_pair(0, i)); 
			while(!pq.empty()) {
				long long int k = pq.top().second;
				pq.pop();
				for(j = 0; j < N; j++) {
					if(D3[k][j] < 0) continue;
					if(ANS[i][j] < 0 || ANS[i][k] + D3[k][j] < ANS[i][j]) {
						ANS[i][j] = ANS[i][k] + D3[k][j]; 
						pq.push(make_pair(ANS[i][j], j));
					}
				}
			}
		}
/*		
		for(i = 0; i < N; i++) {
			for(j = 0; j < N; j++) {
				printf("%lf ", ANS[i][j]);
			}
			printf("\n");
		}
		*/
		printf("Case #%lld: ", t);
		for(i = 0; i < Q; i++) {
			printf("%lf ", ANS[U[i]-1][V[i]-1]);
		}
		printf("\n");
	}
	return 0;
}
