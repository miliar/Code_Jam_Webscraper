#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

int t, n, c, m;
int p[1010], b[1010];
int cnt[1010][1010];
int cnt2[1010];
int cnt3[1010];

int main(void) {
	FILE *fin = fopen("B-large.in", "r");
	FILE *fout = fopen("output.txt", "w");
	fscanf(fin, "%d", &t);
	for (int iter = 1; iter <= t; iter++) {
		fprintf(fout, "Case #%d: ", iter);
		memset(cnt, 0, sizeof(cnt));
		memset(cnt2, 0, sizeof(cnt2));
		memset(cnt3, 0, sizeof(cnt3));

		fscanf(fin, "%d%d%d", &n, &c, &m);
		for (int i = 0; i < m; i++) {
			fscanf(fin, "%d%d", p + i, b + i);
			cnt[b[i]][p[i]]++;
			cnt2[b[i]]++;
			cnt3[p[i]]++;
		}

		int ans = 0;
		for (int i = 1; i <= c; i++)
			ans = max(ans, cnt2[i]);
		int cntbuf = 0;
		for (int i = 1; i <= n; i++) {
			cntbuf += cnt3[i];
			ans = max(ans, (cntbuf + i - 1) / i);
		}
		fprintf(fout, "%d ", ans);

		int move = 0;
		cntbuf = 0;
		for (int i = 1; i <= n; i++) {
			cntbuf += cnt3[i];
			if (cnt3[i] > ans)
				move += cnt3[i] - ans;
		}
		fprintf(fout, "%d\n", move);
	}
	return 0;
}