#include<stdio.h>
#include<string>
int main(void) {
	int T, K, len, flag, count;
	char pancake[1001];
	FILE *in = fopen("A-small-attempt1.in","rb");
	FILE *out = fopen("result.txt", "wt");

	//scanf("%d", &T);
	fscanf(in, "%d", &T);

	for(int i = 0; i < T; i++) {
		//scanf("%s", pancake);
		fscanf(in, "%s", pancake);
		//scanf("%d", &K);
		fscanf(in, "%d", &K);
		len = strlen(pancake);
		count = 0;
		for(int j = 0; j <= len-K ; j++) {
			if(pancake[j] == '-') {
				for(int k = 0; k < K; k++) {
					if(pancake[j+k] == '-') {
						pancake[j+k] = '+';
					}
					else {
						pancake[j+k] = '-';
					}
				}
				count++;
			}
		}
		flag = 0;
		for(int j = len-K; j < len; j++) {
			if(pancake[j] == '-') {
				flag = 1;
			}
		}
		printf("Case #%d: ", i);
		fprintf(out, "Case #%d: ", i+1);
		if(flag == 0) {
			printf("%d\n", count);
			fprintf(out, "%d\n", count);
		}
		else {
			printf("IMPOSSIBLE\n");
			fprintf(out, "IMPOSSIBLE\n");
		}
	}

	return 0;
}