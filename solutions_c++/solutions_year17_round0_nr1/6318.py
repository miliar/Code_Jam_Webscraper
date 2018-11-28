#include<stdio.h>
#include<string.h>

#define MAX_SIZE 1000

char str[MAX_SIZE + 5];

int main()
{
	int t;
	int i, j;
	int tc;
	int k,len,cnt,key;
	FILE *infp = fopen("input.txt", "r");
	FILE *outfp = fopen("output.txt", "w");
	fscanf(infp,"%d", &tc);
	for (t = 0; t < tc; t++) {
		fscanf(infp,"%s %d", str, &k);
		len = strlen(str);
		cnt = 0; key = 1;
		for (i = 0; i <= len - k; i++) {
			if (str[i] == '-') {
				for (j = i; j < i + k; j++) {
					if (str[j] == '-') str[j] = '+';
					else str[j] = '-';
				}
				cnt++;
			}
		}
		for (i = len - k; i < len; i++) {
			if (str[i] == '-') {
				key = 0;
				break;
			}
		}
		if (key == 0) {
			// impossible
			fprintf(outfp,"Case #%d: IMPOSSIBLE\n", t + 1);
		}
		else {
			// cnt Ãâ·Â
			fprintf(outfp,"Case #%d: %d\n",t+1,cnt);
		}
	}
	return 0;
}