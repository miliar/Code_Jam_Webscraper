#include<stdio.h>
#include<memory.h>
FILE *fo, *fp;
char map[26][26];
char check[26][26];
int gap[700][3], gc, ans = 0;
int x, y;
void find(int now) {
	if (now == gc) {
		int i, j;
		for (i = 0; i < x; i++) {
			for (j = 0; j < y; j++) {
				if (check[i][j] == 0) {
					return;
				}
			}
		}


		for (i = 0; i < x; i++) {
			for (j = 0; j < y; j++) {
				fprintf_s(fp, "%c", check[i][j]);
			}
			fprintf_s(fp, "\n");
		}
		ans = 1;
	}
	else {
		int left,right,up,down,i,j;
		bool ches = 0;
		for (left = gap[now][1]; left >= 0; left--) {
			for (right = gap[now][1]; right < y; right++) {
				for (up = gap[now][0]; up >= 0; up--) {
					ches = false;
					for (i = left; i <= right; i++) 
						if (check[up][i] != 0 && check[up][i] != gap[now][2]) {
							ches = true;
							break;
						}
					if (ches)
						break;
					for (down = gap[now][0]; down < x; down++) {
						ches = false;
						for (i = left; i <= right; i++)
							if (check[down][i] != 0 && check[down][i] != gap[now][2]) {
								ches = true;
								break;
							}

						if (ches)
							break;
						// complete
						for (i = up; i <= down; i++)
							for (j = left; j <= right; j++)
								check[i][j] = gap[now][2];
						
						find(now + 1);
						if (ans == 1)
							return;

						for (i = up; i <= down; i++)
							for (j = left; j <= right; j++)
								if (gap[now][0] == i && gap[now][1] == j) {
									check[i][j] = gap[now][2];
								}
								else {
									check[i][j] = 0;
								}

					}
				}
			}
		}
	}
}
int main() {
	fopen_s(&fo, "input.txt", "r");
	fopen_s(&fp, "output.txt", "w");
	int T, t;
	fscanf_s(fo, "%d", &T);
	long long int N, S;
	for (t = 1; t <= T; t++) {
		int i,j;
		memset(map, 0, sizeof(map));
		memset(check, 0, sizeof(check));
		memset(gap, 0, sizeof(gap));
		gc = 0;

		fscanf_s(fo, "%d %d", &x, &y);
		for (i = 0; i < x; i++) {
			fscanf_s(fo, "%s", map[i], 100);
			for (j = 0; j < y; j++) {
				if (map[i][j] != '?') {
					gap[gc][0] = i;
					gap[gc][1] = j;
					gap[gc][2] = map[i][j];

					check[i][j] = map[i][j];
					gc++;
				}
			}
		}
		fprintf_s(fp, "Case #%d:\n", t);
		ans = 0;
		find(0);
	}
	return 0;
}