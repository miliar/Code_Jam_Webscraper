#include<stdio.h>
#include<memory.h>
FILE *fo, *fp;
int min(int a, int b) {
	if (a < b) return a;
	return b;
}
int main() {
	fopen_s(&fo, "input.txt", "r");
	fopen_s(&fp, "output.txt", "w");
	int T, t;
	fscanf_s(fo, "%d", &T);
	int N, G[110], P, i, last = 0;
	int cnt[4] = { 0 };
	for (t = 1; t <= T; t++) {
		memset(G, 0, sizeof(G));
		memset(cnt, 0, sizeof(cnt));
		fscanf_s(fo, "%d %d", &N, &P);
		for (i = 0; i < N; i++) {
			fscanf_s(fo, "%d", &G[i]);
			G[i] %= P;
			cnt[G[i]] ++;
		}
		last = N;
		int ans = cnt[0] + 1;
		last -= cnt[0];

		if (P == 2) {
			ans += (cnt[1]) / 2;
			last -= (cnt[1] / 2) * 2;
		}
		else if (P == 3) {
			int m = min(cnt[1], cnt[2]);
			ans += m;
			last -= m * 2;
			cnt[1] -= m;
			cnt[2] -= m;
			ans += (cnt[1]) / 3;
			last -= (cnt[1] / 3) * 3;
			ans += (cnt[2]) / 3;
			last -= (cnt[2] / 3) * 3;
		}
		else if (P == 4) {
			// cnt = 2; 
			// 1 + 3
			int m = min(cnt[1], cnt[3]);
			ans += m;
			last -= m * 2;
			cnt[1] -= m;
			cnt[3] -= m;
			// 2 + 2;
			ans += (cnt[2] / 2);
			last -= (cnt[2] / 2) * 2;
			cnt[2] %= 2;
			// cnt = 3;
			if (cnt[2] == 1) {
				if (cnt[3] >= 2) {
					cnt[3] -= 2;
					cnt[2] -= 1;
					ans++;
					last -= 3;
				}
				if (cnt[1] >= 2) {
					cnt[1] -= 2;
					cnt[2] -= 1;
					ans++;
					last -= 3;
				}
			}
			// cnt = 4;
			for (i = 1; i <= 3; i++) {
				ans += (cnt[i]) / 4;
				last -= (cnt[i] / 4) * 4;
			}
		}

		if (last == 0) ans--;
		fprintf_s(fp, "Case #%d: %d\n", t, ans);
	}
	return 0;
}