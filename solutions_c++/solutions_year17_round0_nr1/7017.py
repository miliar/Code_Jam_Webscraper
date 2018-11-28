#include<stdio.h>
#include<string.h>
#define MAX 1010
FILE *in = fopen("input.txt", "r");
FILE *out = fopen("output.txt", "w");

int main()
{
	int T, t =1; fscanf(in,"%d", &T);
	while (T--) {
		char S[MAX] = { 0, };
		int len =0, i,k,N,cnt = 0;
		fscanf(in,"%s%d", S,&N);
		len = strlen(S);

		for (i = 0; i < len - N +1; i++) {
			if (S[i] != '-') continue;
			cnt++;
			for (k = 0; k < N; k++) {
				if (S[i+k] == '-') S[i+k] = '+';
				else S[i+k] = '-';
			}
		}

		for(; i < len; i++) {
			if (S[i] == '-') break;
		}
		if (len == i) fprintf(out,"Case #%d: %d\n",t,cnt);
		else fprintf(out, "Case #%d: IMPOSSIBLE\n",t);

		t++;
	}
	return 0;
}