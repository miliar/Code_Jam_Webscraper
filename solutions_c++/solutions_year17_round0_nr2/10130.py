#include<stdio.h>
#include<string.h>
#pragma warning(disable:4996)
FILE *in = fopen("B-small-attempt0.in", "r");
FILE *out = fopen("output.txt", "w");
int T, N;
int main()
{
	fscanf(in,"%d", &T);
	for (int a = 1; a <= T; a++){
		fscanf(in,"%d", &N);
		for (int i = N; i >= 0; i--){
			char str[10];
			sprintf(str, "%d", i);
			int len = strlen(str);
			//	printf("%s %d\n",str,len);
			int j;

			for (j = 1; j<len; j++){
				//	printf("%d %s %c %c %d %d\n",i,str,str[j-1],str[j],j-1,j);
				if (str[j - 1] - '0'>str[j] - '0') break;
			}
			if (j == len){
				fprintf(out,"Case #%d: %d\n", a, i);
				break;
			}
		}
	}
	return 0;
}