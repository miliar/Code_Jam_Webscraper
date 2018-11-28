#include <stdio.h>
#include <algorithm>

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

		long long en;
		scanf("%lld", &en);
		if (en < 10)
			printf("Case #%d: %lld\n", ecount, en);
		else {
			int digits[20];
			int len = 0;
			while (en > 0) {
				digits[len++] = en % 10;
				en /= 10;
			}

			bool check = true;
			while (check) {
				check = false;
				for (int i = len - 1; i > 0; i--)
					if (digits[i] > digits[i-1]) {
						digits[i]--;
						for (int j = i - 1; j >= 0; j--)
							digits[j] = 9;
						check = true;
						break;
					}
			}
			if (digits[len - 1] == 0)
				len--;
			printf("Case #%d: ", ecount);
			for (int i = len - 1; i >= 0; i--)
				printf("%d", digits[i]);
			printf("\n");
		}
		

		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d END\n", ecount);
	}

	return 0;
}
