#include<stdio.h>
#include<stdlib.h>
#include<queue>

using namespace std;

int main(void) {
	int T, CC, idx;
	int i;
	FILE *in = fopen("C-small-1-attempt0.in","rb");
	FILE *out = fopen("C-small-1-result.txt", "wt");	
	priority_queue<int> pq;
	
	fscanf(in, "%d", &T);
	for(i = 0; i < T; i++) {
		fscanf(in, "%d %d", &CC, &idx);

		pq.push(CC);

		while(idx--) {
			CC = pq.top();
			pq.pop();
			if(CC > 0) {
				pq.push(CC/2);
				pq.push((CC-1)/2);
			}
		}

		printf("Case #%d: ", i+1);
		fprintf(out, "Case #%d: ", i+1);
		printf("%d %d\n", CC/2, (CC-1)/2);
		fprintf(out, "%d %d\n", CC/2, (CC-1)/2);

		while(!pq.empty()) {
			pq.pop();
		}
	}

	return 0;
}