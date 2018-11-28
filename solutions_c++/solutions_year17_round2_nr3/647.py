#include <stdio.h>
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

	double dis[110][110];
	double hour[110][110];
	double inf = 1e18;
	double tinf = 1e15;
	for (ecount = 1; ecount <= ecase; ecount++) {
		if (ecount < caseStart || ecount > caseEnd)
			continue;
	
		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d START\n", ecount);

		int en, eq;
		scanf("%d%d", &en, &eq);

		double ee[110], es[110];
		for (int i = 0; i < en; i++)
			scanf("%lf%lf", &ee[i], &es[i]);

		for (int i = 0; i < en; i++) 
			for (int j = 0; j < en; j++) {
				scanf("%lf", &dis[i][j]);
				if (dis[i][j] == -1)
					dis[i][j] = inf;
			}

		for (int k = 0; k < en; k++)
			for (int i = 0; i < en; i++)
				for (int j = 0; j < en; j++)
					if (i != j && j != k && k != i)
						dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);

		for (int i = 0; i < en; i++)
			for (int j = 0; j < en; j++)
				hour[i][j] = tinf;
		for (int i = 0; i < en; i++)
			for (int j = 0; j < en; j++)
				if (dis[i][j] <= ee[i])
					hour[i][j] = min(hour[i][j], dis[i][j] / es[i]);

		for (int k = 0; k < en; k++)
			for (int i = 0; i < en; i++)
				for (int j = 0; j < en; j++)
					if (i != j && j != k && k != i)
						hour[i][j] = min(hour[i][j], hour[i][k] + hour[k][j]);

		printf("Case #%d:", ecount);
		for (int i = 0; i < eq; i++) {
			int qa, qb;
			scanf("%d%d", &qa, &qb);
			qa--;
			qb--;
			printf(" %lf", hour[qa][qb]);
		}
		printf("\n");
		

		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d END\n", ecount);
	}

	return 0;
}
