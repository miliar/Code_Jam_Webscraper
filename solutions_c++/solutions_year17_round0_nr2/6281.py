#include<stdio.h>
#include<string.h>

#define MAX_SIZE 20

char str[MAX_SIZE + 5];

int main()
{
	int t;
	int i, j;
	int tc;
	int len, cnt, k, key;
	FILE *infp = fopen("input.txt", "r");
	FILE *outfp = fopen("output.txt", "w");
	fscanf(infp, "%d", &tc);
	for (t = 0; t < tc; t++) {
		fscanf(infp, "%s", str);
		len = strlen(str);
		k = 0; key = 1;
		for (i = 1; i < len; i++) {
			if (str[i - 1] <= str[i]) k++;
			else break;
		}
		// 0 ~ k 까지는 소팅이 만족하고있다.
		if( k + 1 < len ) {
			for (i = k; i >= 0; i--) {
				str[i]--;
				if (i == 0) break;
				if (str[i - 1] <= str[i]) break;
				else k--;
			}
			k++;
			for (i = k; i < len; i++)
				str[i] = '9';
		}
		fprintf(outfp,"Case #%d: ",t+1);
		for (i = 0; i < len; i++) {
			if (str[i] == '0' && key == 1) continue;
			else {
				key = 0;  fprintf(outfp, "%c", str[i]);
			}
		}
		fprintf(outfp,"\n");
	}
	return 0;
}