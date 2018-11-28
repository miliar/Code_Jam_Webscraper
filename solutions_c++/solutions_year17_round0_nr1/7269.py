#include <stdio.h>
#include <string.h>
int main() {
	FILE *ifs = fopen("A-large.in", "r");
	FILE *ofs = fopen("output.txt", "w");
	int T; fscanf(ifs, "%d\n", &T);
	for (int tc = 1; tc <= T; tc++) {
		char in[1001]; fscanf(ifs, "%s", in);
		int len = strlen(in), K, cnt = 0;
		fscanf(ifs, "%d", &K);
		for (int i = 0; i <= len - K; i++)
			if (in[i] == '-') {
				cnt++;
				for (int j = 0; j < K; j++) in[i + j] = '+' + '-' - in[i + j];
			}
		for (int i = len - K + 1; i < len; i++)
			if (in[i] == '-') { fprintf(ofs, "Case #%d: IMPOSSIBLE\n", tc); goto ex; }
		fprintf(ofs, "Case #%d: %d\n", tc, cnt);
	ex:;
	}
	return 0;
}