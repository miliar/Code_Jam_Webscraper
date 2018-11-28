#include <stdio.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

int n;
long long limit[101], speed[101], dist[101][101];
double D[101];
bool check[101];

int main(){
	int testt;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testt);
	for (int test = 1; test <= testt; test++){
		int q;
		scanf("%d %d", &n,&q);
		for (int i = 0; i < n; i++){
			scanf("%lld %lld", &limit[i], &speed[i]);
		}
		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++){
				scanf("%lld", &dist[i][j]);
				if (dist[i][j] == -1 && i != j)
					dist[i][j] = 1LL << 60;
				if (i == j)
					dist[i][j] = 0;
			}
		}

		for (int k = 0; k < n; k++){
			for (int i = 0; i < n; i++){
				for (int j = 0; j < n; j++){
					if (dist[i][j]>dist[i][k] + dist[k][j])
						dist[i][j] = dist[i][k] + dist[k][j];
				}
			}
		}

		printf("Case #%d: ", test);
		while (q--){
			for (int i = 0; i < n; i++){
				check[i] = false;
				D[i] = 1e15;
			}

			int s, e;
			scanf("%d %d", &s, &e);
			s--; e--;

			D[s] = 0;
			while (1){
				int t;
				double min = 1e15;
				for (int i = 0; i < n; i++){
					if (!check[i] && min>D[i]){
						min = D[i];
						t = i;
					}
				}
				check[t] = 1;
				if (t == e) break;

				for (int i = 0; i < n; i++){
					if (dist[t][i] <= limit[t] && D[i] > min + 1.0*dist[t][i]/speed[t])
						D[i] = min + 1.0*dist[t][i]/speed[t];
				}
			}
			printf("%.7lf ", D[e]);
		}
		printf("\n");
	}
	return 0;
}
