#include<stdio.h>
#include<string.h>
#include<memory.h>
int n;
FILE *fo, *fp;
int main() {
	fopen_s(&fo, "input.txt", "r");
	fopen_s(&fp, "output.txt", "w");
	int T,s,t,i,j;
	char len[30];
	int find[30];
	fscanf_s(fo, "%d", &T);
	for (t = 1; t <= T; t++) {
		memset(len, 0, sizeof(len));
		memset(find, 0, sizeof(find));
		fscanf_s(fo, "%s", len, 30);
		s = strlen(len);
		for (i = 0; i < s; i++) {
			len[i] -= '0';
		}
		bool same = true;
		for (i = 0; i < s; i++) {
			if (same) {
				find[i] = len[i];
				while (i != 0) {
					if (find[i] >= find[i - 1])
						break;

					find[i - 1] --;
					same = false;
					i --;
				}
			}
			else {
				find[i] = 9;
			}
		}
		fprintf_s(fp, "Case #%d: ", t);
		if (find[0] != 0)
			fprintf_s(fp, "%d", find[0]);
		for (i = 1; i < s; i++) {
			fprintf_s(fp, "%d", find[i]);
		}
		fprintf_s(fp, "\n");
	}
	return 0;
}