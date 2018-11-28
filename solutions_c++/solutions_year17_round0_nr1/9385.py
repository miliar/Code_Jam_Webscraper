#include <stdio.h>
#include <string.h>
#define MAX 1001

char str[MAX];

void flip(char* a) {
	*a = (*a == '+') ? '-' : '+';
}

int main() {
	int t, k;
	FILE* fpi = fopen("A-large.in", "r");
	FILE *fpo = fopen("A-large.out", "w");

	fscanf(fpi, "%d", &t);
	for (int i = 0; i < t; i++) {
		fscanf(fpi, "%s", str);
		fscanf(fpi, "%d", &k);
		fprintf(fpo, "Case #%d: ", i + 1);
		int cnt = 0;
		int iflag = 0;
		for (int j = 0; str[j]; j++) {
			if (str[j] == '-') {
				if (j + k > strlen(str)) {
					iflag = 1;
					break;
				}
				cnt++;
				for (int l = j; l < j + k; l++)
					flip(str + l);					
			}
		}
		if (iflag)
			fprintf(fpo, "IMPOSSIBLE\n");
		else
			fprintf(fpo, "%d\n", cnt);
	}
	fclose(fpi);
	fclose(fpo);

	return 0;
}