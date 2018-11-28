#include<stdio.h>
#include<string.h>
FILE *in = fopen("B-large.in", "r");
FILE *out = fopen("output.txt", "w");
char b[30];
int main() {
	int n, i, l, j, k;
	fscanf(in, "%d", &n);
	for (i = 1; i <= n; i++) {
		fscanf(in, "\n%s", b);
		l = strlen(b);
		for (j = 1; j < l; j++) {
			if (b[j] < b[j - 1]) {
				b[j - 1]--;
				for (k = j; k < l; k++) b[k] = '9';
				k = j - 1;
				while (b[k] < b[k - 1]) { b[k] = '9'; k--; b[k]--; }
				break;
			}
		}
		fprintf(out, "Case #%d: ", i);
		if (b[0] == '0') { for (k = 1; k < l; k++) fprintf(out, "9"); fprintf(out, "\n"); }
		else {
			fprintf(out, "%s", b);
			fprintf(out, "\n");
		}
	}
	return 0;
}