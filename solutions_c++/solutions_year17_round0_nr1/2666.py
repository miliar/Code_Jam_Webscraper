#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
	int ecase, ecount;
	int caseStart = -1, caseEnd = 9999999;
	scanf("%d", &ecase);

	char convert[100];
	convert['+'] = '-';
	convert['-'] = '+';

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

		char input[1010];
		int ek;
		scanf("%s%d", input, &ek);
		int slen = strlen(input);

		int ans = 0;
		for (int i = 0; i + ek <= slen; i++)
			if (input[i] == '-') {
				ans++;
				for (int j = 0; j < ek; j++)
					input[i + j] = convert[input[i + j]];
			}
		
		bool hasMinus = false;
		for (int i = 0; i < slen; i++)
			hasMinus |= (input[i] == '-');

		if (hasMinus)
			printf("Case #%d: IMPOSSIBLE\n", ecount);
		else
			printf("Case #%d: %d\n", ecount, ans);
		

		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d END\n", ecount);
	}

	return 0;
}
