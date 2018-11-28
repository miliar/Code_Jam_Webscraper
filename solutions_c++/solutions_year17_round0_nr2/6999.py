#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define MAX 30

FILE *in = fopen("input.txt", "r");
FILE *out = fopen("output.txt", "w");

int main()
{
	int T, t =1; fscanf(in,"%d", &T);
	while (T--) {
		char S[MAX] = { 0, };
		int len =0, i, j;
		fscanf(in,"%s", S);
		len = strlen(S);

		for (i = len -1; i>=0; i--) {
			for (j = i - 1; j >= 0; j--) {
				if (S[j] > S[i]) break;
			}
			if (j != -1) {
				S[i-1]--;
				for (j = i; j < len; j++)
					S[j] = '9';
			}
		}
		if (S[0] == '0') {
			for (i = 0; i < len - 1; i++) {
				S[i] = S[i + 1];
			}
			S[len - 1] = 0;
		}
		
		fprintf(out,"Case #%d: %s\n",t,S);
		

		t++;
	}
	return 0;
}