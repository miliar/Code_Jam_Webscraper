#include<stdio.h>
#include<string>
int main(void) {
	int T, len, begin_nine;
	char input[20];
	FILE *in = fopen("B-large.in","rb");
	FILE *out = fopen("result.txt", "wt");

	//scanf("%d", &T);
	fscanf(in, "%d", &T);

	for(int i = 0; i < T; i++) {
		//scanf("%s", input);
		begin_nine = 20;
		fscanf(in, "%s", &input);
		len = strlen(input);
		for(int j = len-1; j > 0; j--) {
			if(input[j] <= 0 || input[j] < input[j-1]) {
				input[j-1]--;
				begin_nine = j;
			}
		}
		//printf("Case #%d: ", i);
		fprintf(out, "Case #%d: ", i+1);
		for(int j = 0; j < len && j < begin_nine; j++) {
			if(input[j] != '0') {
				//printf("%c", input[j]);
				fprintf(out, "%c", input[j]);
			}
		}
		for(int j = begin_nine; j < len; j++) {
			//printf("9");
			fprintf(out, "9");
		}
		//printf("\n");
		fprintf(out, "\n");
	}

	return 0;
}