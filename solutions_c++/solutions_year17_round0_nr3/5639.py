#include<stdio.h>
#include<stdlib.h>
#include<queue>

using namespace std;

int main(void) {
	int T, N, K;
	int i, j;
	FILE *in = fopen("C-small-1-attempt3.in","rb");
	FILE *out = fopen("result.txt", "wt");
	
	priority_queue<int, vector<int>, less<int>> pq;
	
	//scanf("%d", &T);
	fscanf(in, "%d", &T);

	for(i = 0; i < T; i++) {

		//scanf("%d %d", &N, &K);
		fscanf(in, "%d %d", &N, &K);

		pq.push(N);

		while(K--) {
			N = pq.top();
			pq.pop();
			if(N > 0) {
				pq.push(N/2);
				pq.push((N-1)/2);
			}
		}

		//printf("Case #%d: ", i+1);
		fprintf(out, "Case #%d: ", i+1);
		//printf("%d %d\n", N/2, (N-1)/2);
		fprintf(out, "%d %d\n", N/2, (N-1)/2);

		while(!pq.empty()) {
			pq.pop();
		}
	}

	return 0;
}