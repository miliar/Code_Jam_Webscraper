#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAX 1000000

struct Activity {
	int start, end;
};
int T;
int NC, NJ;
Activity AC[101], AJ[101];

bool order(const Activity &x, const Activity &y) {
	if (x.start < y.start) return true;
	else return false;
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	int i, j, k;

	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		scanf("%d %d", &NC, &NJ);
		for (i = 1; i <= NC; i++)
			scanf("%d %d", &AC[i].start, &AC[i].end);
		for (i = 1; i <= NJ; i++)
			scanf("%d %d", &AJ[i].start, &AJ[i].end);

		sort(AC + 1, AC + NC + 1, order);
		sort(AJ + 1, AJ + NJ + 1, order);

		printf("Case #%d: ", t);
		if (NC == 2 && NJ == 0) {
			if (AC[2].end - AC[1].start <= 720) printf("2");
			else if (AC[2].start - AC[1].end >= 720) printf("2");
			else printf("4");
		}
		else if (NC == 1 && NJ == 1) {
			printf("2");
		}
		else if (NC == 1 && NJ == 0) printf("2");
		else if (NC == 0 && NJ == 2) {
			if (AJ[2].end - AJ[1].start <= 720) printf("2");
			else if (AJ[2].start - AJ[1].end >= 720) printf("2");
			else printf("4");
		}
		else if (NC == 0 && NJ == 1) printf("2");
		
		printf("\n");

		/*
		for (i = 0; i <= 24 * 60; i++) {
			for (j = 0; j <= 720; j++) {
				for (k = 0; k <= 720; k++)
					d[i][j][k] = 0;
			}
		}
		for (i = 1; i <= 24 * 60; i++) {
			bool errC = false, errJ = false;
			for (j = 1; j <= NC; j++) {
				if (i > AC[j].start && i <= AC[j].end) { errC = true; break; }
			}
			for (j = 1; j <= NJ; j++) {
				if (i > AJ[j].start && i <= AJ[j].end) { errJ = true; break; }
			}

			for (j = 0; j <= 720; j++) {
				for (k = 0; k <= 720; k++)
					d[i][j][k] = MAX;
			}

			if (errC && !errJ) {
				for (j = 1; j <= 720; j++) {
					for (k = 1; k <= 720; k++) {
						if (d[i][j][k] > d[i - 1][j][k - 1]) d[i][j][k] = d[i - 1][j][k - 1];
						if(d[i][j][k]>d[i-1][])
					}
				}
				for (j = 0; j <= 720; j++) {
					if (d[i][j][0] > d[i - 1][j][0]) d[i][j][0] = d[i - 1][j][0];
				}
				for (j = 1; j <= 720; j++) {
					if (d[i][j][1] > d[i - 1][j - 1][1]) d[i][j][1] = d[i - 1][j - 1][1];
					if(d[i][j][1]>d[i-1][j])
				}
			}
			else if (!errC && errJ) {
				for (j = 0; j <= 720; j++) {
					if (d[i][j][1] > d[i - 1][j][1]) d[i][j][1] = d[i - 1][j][1];
				}
			}
			else if (errC && errJ) {

			}
		}
		*/
	}
	return 0;
}