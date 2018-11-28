#include <stdio.h>
typedef long long lld;
int main() {
	FILE *ifs = fopen("B-large.in", "r");
	FILE *ofs = fopen("output.txt", "w");
	int T; fscanf(ifs, "%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		lld N; int in[19] = { 0, };
		fscanf(ifs, "%lld", &N);
		for (int i = 0; N; i++) { in[i] = N % 10; N /= 10; }
		bool chk = true;
		while (chk) {
			chk = false;
			for (int i = 18; i >= 1; i--) {
				if (in[i] > in[i - 1]) {
					chk = true;
					in[i--]--;
					for (; i >= 0; i--) in[i] = 9;
					break;
				}
			}
		}
		N = 0;
		for (int i = 18; i >= 0; i--) {
			N *= 10;
			N += in[i];
		}
		fprintf(ofs, "Case #%d: %lld\n", tc, N);
	}
	return 0;
}