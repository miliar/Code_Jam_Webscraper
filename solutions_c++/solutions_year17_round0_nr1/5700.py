#include<stdio.h>
#include<string>
int main(void) {
	int T, KKK, len, flag, count;
	char pancake[1001];
	int i,j; 
	FILE *in = fopen("A-large.in","rb");
	FILE *out = fopen("A-large-result.txt", "wt");

	fscanf(in, "%d", &T);
	for(i = 0; i < T; i++) {
		fscanf(in, "%s", pancake);
		fscanf(in, "%d", &KKK);
		len = strlen(pancake);
		count = 0;

		for(int j = 0; j <= len-KKK ; j++){
			if(pancake[j] == '-') {
				for(int k = 0; k < KKK; k++){
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
		for(j = len-KKK; j < len; j++) {
			if(pancake[j] == '-') {
				flag = 1;
			}
		}

		printf("Case #%d: ", i);
		fprintf(out, "Case #%d: ", i+1);

		if(flag == 0){
			printf("%d\n", count);
			fprintf(out, "%d\n", count);
		}
		else{
			printf("IMPOSSIBLE\n");
			fprintf(out, "IMPOSSIBLE\n");
		}
	}

	return 0;
}