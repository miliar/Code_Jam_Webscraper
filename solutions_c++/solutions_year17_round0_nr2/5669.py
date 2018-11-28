#include<stdio.h>
#include<string>
int main(void) {
	int T, len, start_idx;
	char input[20];
	int i,j;
	FILE *in = fopen("B-large.in","rb");
	FILE *out = fopen("B-large-result.txt", "wt");

	fscanf(in, "%d", &T);

	for( i = 0; i < T; i++) {
		start_idx = 20;
		fscanf(in, "%s", &input);
		len = strlen(input);
		for(j= len-1; j>0;j--) {
			if(input[j] < input[j-1]||input[j] <=0 ) {
				input[j-1]--;
				start_idx = j;
			}
		}
		fprintf(out, "Case #%d: ", i+1);

		for(j = 0; j < len && j < start_idx; j++) {
			if(input[j] != '0') {
				fprintf(out, "%c", input[j]);
			}
		}
		for(j = start_idx; j < len; j++) {
			fprintf(out, "9");
		}
		fprintf(out, "\n");
	}

	return 0;
}