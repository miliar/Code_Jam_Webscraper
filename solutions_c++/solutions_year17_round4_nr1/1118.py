#include <stdio.h>
#include <algorithm>

using namespace std;

int c(int arr[], int a, int b, int c, int d) {
	int bb[4];
	bb[0] = a;
	bb[1] = b;
	bb[2] = c;
	bb[3] = d;
	int ret = 100000;
	for (int i = 0; i < 4; i++) {
		if (bb[i] > 0) {
			int t = arr[i] / bb[i];
			if (t < ret)
				ret = t;
		}
	}
	for (int i = 0; i < 4; i++)
		arr[i] -= bb[i] * ret;
	return ret;
}

int main(int argc, char *argv[]) {
	int ecase, ecount;
	int caseStart = -1, caseEnd = 9999999;
	scanf("%d", &ecase);

	if (argc > 1) {
		if (sscanf(argv[1], "%d", &caseStart) == 1) {
			if (argc > 2)
				sscanf(argv[2], "%d", &caseEnd);
		}
		if (caseEnd < caseStart)
			caseEnd = caseStart;
		if (caseEnd != 9999999 && caseEnd >= 1 && caseStart <= 0)
			caseStart = 1;
		if (caseStart > 0)
			fprintf(stderr, "....................DEBUG MODE ENABLED (FROM CASE %d to %d)\n", caseStart, caseEnd);
	}

	for (ecount = 1; ecount <= ecase; ecount++) {
		if (ecount < caseStart || ecount > caseEnd)
			continue;
	
		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d START\n", ecount);

		int en, ep;
		scanf("%d%d", &en, &ep);
		int cnt[4] = {0};
		for (int i = 0; i < en; i++) {
			int t;
			scanf("%d", &t);
			cnt[t % ep]++;
		}

		int ans = 0;
		ans += c(cnt, 1, 0, 0, 0);
		if (ep == 2) {
			ans += c(cnt, 0, 2, 0, 0);
		}
		else if (ep == 3) {
			ans += c(cnt, 0, 1, 1, 0);
			ans += c(cnt, 0, 3, 0, 0);
			ans += c(cnt, 0, 0, 3, 0);
		}
		else if (ep == 4) {
			ans += c(cnt, 0, 1, 0, 1);
			ans += c(cnt, 0, 0, 2, 0);
			ans += c(cnt, 0, 2, 1, 0);
			ans += c(cnt, 0, 0, 1, 2);
			ans += c(cnt, 0, 4, 0, 0);
			ans += c(cnt, 0, 0, 0, 4);
		}

		int r = cnt[1] + cnt[2] + cnt[3];
		if (r > 0)
			ans++;

		printf("Case #%d: %d\n", ecount, ans);
		

		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d END\n", ecount);
	}

	return 0;
}
