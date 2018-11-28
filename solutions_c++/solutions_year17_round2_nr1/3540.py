#include<stdio.h>

int main(void) {
	int T;
	long long D, N, K, S;
	long long head, body, nhead, nbody;
	FILE *in = fopen("A-large.in","rb");
	FILE *out = fopen("result.txt", "wt");

	//scanf("%d", &T);
	fscanf(in, "%d", &T);

	for(int t = 0; t < T; t++) {
		//scanf("%lld", &D);
		fscanf(in, "%lld", &D);
		//scanf("%lld", &N);
		fscanf(in, "%lld", &N);

		N--;
		//scanf("%lld%lld", &K, &S);
		fscanf(in, "%lld%lld", &K, &S);
		head = D-K;
		body = S;
		while(N--) {
			//scanf("%lld%lld", &K, &S);
			fscanf(in, "%lld%lld", &K, &S);
			nhead = head*S;	
			nbody = body*(D-K);
			if(nhead < nbody) {
				head = D-K;
				body = S;
			}
		}

		printf("Case #%d: ", t+1);
		fprintf(out, "Case #%d: ", t+1);
		body*=D;
		printf("%lld", body/head);
		fprintf(out, "%lld", body/head);
		body %= head;
		body *= 10;
		printf(".");
		fprintf(out, ".");
		for(int i = 0; i < 6; i++) {
			printf("%lld", body/head);
			fprintf(out, "%lld", body/head);
			body %= head;
			body *= 10;
		}
		printf("\n");
		fprintf(out, "\n");
	}

	return 0;
}