#include <stdio.h>
#include <string.h>

struct SH{
	long long sta;
	double speed;
};

double dp[110]; 
bool vis[110];

long long admat[110][110];
int N, Q;
SH horses[110];

int main(){
	int jcase;
	
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	scanf("%d", &jcase);
	for(int icase=0; icase<jcase; icase++){
		scanf("%d %d", &N, &Q);
		for(int i=0; i<N; i++){
			scanf("%lld %lf", &horses[i].sta, &horses[i].speed);
		}
		for(int i=0; i<N; i++){
			for(int j=0; j<N; j++){
				scanf("%lld", &admat[i][j]);
			}
		}
		
		//floyd warshall
		for(int k=0; k<N; k++){
			for(int i=0; i<N; i++){
				for(int j=0; j<N; j++){
					if(admat[i][k]==-1 || admat[k][j]==-1) continue;
					long long newDist = admat[i][k] + admat[k][j];
					if(admat[i][j] == -1 || admat[i][j] > newDist) admat[i][j] = newDist;
				}
			}
		}
		
		printf("Case #%d:", icase+1);
		
		for(int q=0; q<Q; q++){
			int from, to;
			scanf("%d %d", &from, &to);
			from--; to--;
			memset(vis, false, sizeof(vis));
			
			for(int i=0; i<N; i++) dp[i] = 1e20;
			dp[from] = 0;
			
			for(int i=0; i<N; i++){
				double leastTime = 1e19;
				int chosenCity=-1;
				
				for(int j=0; j<N; j++){
					if(vis[j]) continue;
					if(dp[j] < leastTime){
						leastTime = dp[j];
						chosenCity = j;
					}
				}
				if(chosenCity == -1) break;
				
				vis[chosenCity] = true;
				
				for(int j=0; j<N; j++){
					if(vis[j]) continue;
					if(admat[chosenCity][j] == -1) continue;
					if(admat[chosenCity][j] > horses[chosenCity].sta) continue;
					double time = admat[chosenCity][j] / horses[chosenCity].speed;
					if(dp[j] > dp[chosenCity] + time) dp[j] = dp[chosenCity] + time;
				}
			}
			
			printf(" %.7lf", dp[to]);
		}
		printf("\n");
	}
	return 0;
}

/*
2
4 1
13 10
1 1000
10 8
5 5
-1 1 -1 -1
-1 -1 1 -1
-1 -1 -1 10
-1 -1 -1 -1
*/
