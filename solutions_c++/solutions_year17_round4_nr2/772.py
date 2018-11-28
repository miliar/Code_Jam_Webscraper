#include<stdio.h>
#include<memory.h>
#include<algorithm>
#include<stdlib.h>
FILE *fo, *fp;
int f[1010], fc;
int s[1010], sc;
int main() {
	fopen_s(&fo, "input.txt", "r");
	fopen_s(&fp, "output.txt", "w");
	int T, t;
	fscanf_s(fo, "%d", &T);
	for (t = 1; t <= T; t++) {
		int N, C, M, i,j;
		fscanf_s(fo, "%d %d %d", &N, &C, &M);
		int P, B;
		memset(f, 0, sizeof(f));
		memset(s, 0, sizeof(s));
		for (i = 0; i < M; i++) {
			fscanf_s(fo, "%d %d", &P, &B);
			if (B == 1) f[P]++;
			else s[P] ++ ;
		}
		int ride = 0, promo = 0;
		for (i = 1; i <= N; i++) {
			while (f[i] != 0) {
				bool check = 0;
				for (j = 1; j <= N; j++) {
					if (i != j && s[j] != 0 && f[j] != 0) {
						check = true;
						s[j] --;
						f[i] --;
						ride++;
						break;
					}
				}
				if (!check) {
					for (j = 1; j <= N; j++) {
						if (i != j && s[j] != 0) {
							check = true;
							s[j] --;
							f[i] --;
							ride++;
							break;
						}
					}
					if (!check) {
						if (s[i] != 0 && i != 1) {
							s[i] --;
							f[i] --;
							ride++;
							promo++;
						}
						else {
							f[i] --;
							ride++;
						}
					}
				}
			}
		}
		for (i = 1; i <= N; i++) {
			while (s[i] != 0) {
				s[i] --;
				ride++;
			}
		}
		fprintf_s(fp, "Case #%d: %d %d\n", t,ride,promo);
	}
	return 0;
}