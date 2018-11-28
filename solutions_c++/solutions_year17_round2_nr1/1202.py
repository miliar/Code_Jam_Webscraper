#include <stdio.h>
#include <algorithm>
#define MAX_N 1005
using namespace std;
int S[MAX_N];
int K[MAX_N];

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T; scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		int D, N; scanf("%d %d", &D, &N);
		for(int i = 0; i < N; i++){
			scanf("%d %d", &K[i], &S[i]);
		}
		double maxTime = 0.;
		for(int i = 0; i < N; i++){
			double curTime = ((double)D - K[i]) / S[i];
			maxTime = max(maxTime, curTime);
		}
		printf("Case #%d: %f\n", t, D / maxTime);	
	}
	return 0;
}