#include<stdio.h>
#include<memory.h>
FILE *fo, *fp;
int main() {
	fopen_s(&fo, "input.txt", "r");
	fopen_s(&fp, "output.txt", "w");
	int T, t;
	fscanf_s(fo, "%d", &T);
	for (t = 1; t <= T; t++) {
		double max = 0, ans = 0;
		int D, N;
		fscanf_s(fo, "%d %d", &D, &N);
		int i;
		for (i = 0; i < N; i++) {
			int K, S;
			double gap;
			fscanf_s(fo, "%d %d", &K, &S);
			gap = (D - K) / (double)S;
			if (gap >= max) {
				max = gap;
			}
		}
		ans = D / max;
		fprintf_s(fp, "Case #%d: %.8lf\n", t, ans);
	}
	return 0;
}