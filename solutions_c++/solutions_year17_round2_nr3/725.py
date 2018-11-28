#include<stdio.h>
#include<string.h>
#include <algorithm>
#include<queue>
#include<string>
#include<math.h>
#include<vector>
#include <map>
#include <stack>
#include<set>

using namespace std;
int d[111][111];
double time[111][111];
int dist[111];
int speed[111];
double I = 111111111111111;
int main() {

	int tc, t, i, j,k,INF=1011111111;
	FILE *fp1,*fp2;
	fp1= fopen("1.in", "r");
	fp2 = fopen("2.out","w");
	fscanf(fp1, "%d", &tc);
	for (t = 1; t <= tc; t++) {
		memset(time, 0, sizeof(time));
		fprintf(fp2, "Case #%d: ", t);
		int n, q; fscanf(fp1, "%d%d", &n, &q);
		for (i = 0; i < n; i++) {
			fscanf(fp1, "%d%d", &dist[i], &speed[i]);
		}
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				fscanf(fp1, "%d", &d[i][j]);
				if (d[i][j] == -1)
					d[i][j] = INF;
			}
		}
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				for (k = 0; k < n; k++) {
					if (d[j][k]>d[j][i] + d[i][k])
						d[j][k]=d[j][i] + d[i][k];
				}
			}
		}
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++)
				time[i][j] = I;
		}
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				if (d[i][j] != INF&&d[i][j] <= dist[i])
					time[i][j] = (double)d[i][j] / speed[i];
			}
		}
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				for (k = 0; k < n; k++) {
					if (time[j][k]>time[j][i] + time[i][k])
						time[j][k] = time[j][i] + time[i][k];
				}
			}
		}
		while (q--) {
			int x, y; fscanf(fp1, "%d%d", &x, &y);
			fprintf(fp2, "%.7f ", time[x-1][y-1]);
		}
		fprintf(fp2, "\n");
	}
	fclose(fp1);
	fclose(fp2);
}


