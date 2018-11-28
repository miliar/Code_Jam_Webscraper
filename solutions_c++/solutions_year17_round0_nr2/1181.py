#include <stdio.h>
#include <string.h>

FILE *in = fopen("input.txt", "r");
FILE *out = fopen("output.txt", "w");

int T;
char d[30];

int main(void) {
	int i, j;
	int len;
	bool flag;
	fscanf(in, "%d", &T);
	for (i = 1;i <= T;i ++) {
		fscanf(in, "%s", &d[1]);
		len = strlen(&d[1]);
		flag = 1;
		while (flag) {
			flag = 0;
			for(j = 1;j < len;j ++) {
				if (d[j+1] < d[j]) {
					d[j] --; 
					for (j = j+1;j <= len;j ++) d[j] = '9';
					flag = 1;
					break;
				}
			}
		}

		fprintf(out, "Case #%d: ", i);
		for (j = 1;j <= len;j ++) {
			if (d[j] != '0') break;
		}

		for (;j <= len;j ++) fprintf(out, "%c", d[j]);
		fprintf(out, "\n");
	}

	return 0;
}