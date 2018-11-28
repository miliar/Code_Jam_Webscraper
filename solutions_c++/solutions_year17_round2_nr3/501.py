#include<stdio.h>
#include<memory.h>
FILE *fo, *fp;
int l[110][2];
int D[110][110];
long long int Move[110][110];
double d[110];
bool check[110];
int main() {
	fopen_s(&fo, "input.txt", "r");
	fopen_s(&fp, "output.txt", "w");
	int T, t;
	fscanf_s(fo, "%d", &T);
	for (t = 1; t <= T; t++) {
		int N, Q;
		double ans;
		int k, i, j;
		fprintf_s(fp, "Case #%d:", t);
		memset(l, 0, sizeof(l));
		memset(D, 0, sizeof(D));
		memset(Move, 0, sizeof(Move));
		fscanf_s(fo, "%d %d", &N, &Q);
		for (i = 0; i < N; i++) {
			fscanf_s(fo, "%d %d", &l[i][0], &l[i][1]);
		}
		for (i = 0; i < N; i++) {
			for (j = 0; j < N; j++) {
				fscanf_s(fo, "%d", &D[i][j]);
				Move[i][j] = D[i][j];
			}
			//Move[i][i] = 0;
		}
		for (k = 0; k < N; k++) {
			for (i = 0; i < N; i++) {
				for (j = 0; j < N; j++) {
					if ((Move[i][j] == -1 || Move[i][j] > Move[i][k] + Move[k][j]) &&
						Move[i][k] != -1 && Move[k][j] != -1) {
						Move[i][j] = Move[i][k] + Move[k][j];
					}
				}
			}
		}

		// Dijkstra
		int start, end;
		for (k = 0; k < Q; k++) {
			fscanf_s(fo, "%d %d", &start, &end);
			start--;
			end--;
			for (i = 0; i < N; i++) {
				d[i] = -1;
			}
			memset(check, 0, sizeof(check));
			int now = start;
			d[start] = 0;
			double min;
			for (i = 0; i < N; i++) {
				check[now] = true;
				for (j = 0; j < N; j++) {
					if (Move[now][j] != -1 && Move[now][j] <= l[now][0] &&
						(d[j] == -1 || d[j] > d[now] + Move[now][j]/ ((double) l[now][1]) )) {
						d[j] = d[now] + Move[now][j] / ((double)l[now][1]);
					}
				}
				min = -1;
				for (j = 0; j < N; j++) {
					if (!check[j] && d[j] != -1) {
						if (min == -1 || min > d[j]) {
							min = d[j];
							now = j;
						}
					}
				}
			}
			fprintf_s(fp, " %.8lf", d[end]);
		}
		fprintf_s(fp, "\n");
	}
	return 0;
}