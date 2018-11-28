#include <stdio.h>
#include <map>
#include <algorithm>

using namespace std;

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

		long long en, ek;
		map<long long, long long> cnt;
		scanf("%lld%lld", &en, &ek);
		cnt[en] = 1;
		ek--;
		while (ek > 0) {
			auto it = prev(cnt.end());
			long long take = min(it->second, ek);
			long long a = (it->first - 1) / 2;
			long long b = a + (it->first - 1) % 2;
			cnt[a] += take;
			cnt[b] += take;
			cnt[it->first] -= take;
			if (cnt[it->first] == 0)
				cnt.erase(it);
			ek -= take;
		}

		auto it = prev(cnt.end());
		long long a = (it->first - 1) / 2;
		long long b = a + (it->first - 1) % 2;
		printf("Case #%d: %lld %lld\n", ecount, b, a);
		

		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d END\n", ecount);
	}

	return 0;
}
