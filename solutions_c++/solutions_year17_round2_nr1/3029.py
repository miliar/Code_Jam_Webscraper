#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
int D, N;
int K[1005], S[1005];
int main(){
	int i, T,ca=0;
	scanf("%d", &T);
	while(T--){
		scanf("%d%d", &D, &N);
		for(i=0;i<N;i++){
			scanf("%d%d", &K[i], &S[i]);
		}
		double maxt=0;
		for(i=0;i<N;i++){
			maxt=max(maxt, (double)(D-K[i])/S[i]);
		}
		printf("Case #%d: %f\n", ++ca, (double)D/maxt);
	}
	return 0;
}