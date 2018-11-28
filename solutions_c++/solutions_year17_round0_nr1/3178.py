#include<stdio.h>
#include<string.h>
#include<memory.h>
FILE *fo;
FILE *fp; 
int main() {
	int T;

	errno_t error = fopen_s(&fo, "input.txt", "r");
	error = fopen_s(&fp, "output.txt", "w");
	fscanf_s(fo, "%d", &T);

	int t, i, j;
	char len[1010] = { 0 };
	int l[1010] = { 0 }, n;
	for (t = 1; t <= T; t++) {
		memset(len, 0, sizeof(len));
		memset(l, 0, sizeof(l));

		fscanf_s(fo, "%s %d", len, 1010, &n);
		int s = strlen(len);

		for (i = 0; i < s; i++) {
			l[i] = (len[i] == '-') ? 0 : 1;
		}

		int cnt = 0;
		for(i=0;i<s-n+1;i++){
			if (l[i] == 0) {
				cnt++;
				for (j = 0; j < n; j++) {
					l[i + j] = 1 - l[i + j];
				}
			}
		}
		fprintf_s(fp, "Case #%d: ", t);
		bool check = true;
		for (i = s-n+1; i < s; i++) {
			if (l[i] == 0) {
				check = false;
			}
		}
		if (check) {
			fprintf_s(fp, "%d\n", cnt);
		}
		else {
			fprintf_s(fp, "IMPOSSIBLE\n");
		}
	}
	return 0;
}