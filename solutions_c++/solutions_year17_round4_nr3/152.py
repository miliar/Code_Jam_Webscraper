#include <bits/stdc++.h>
#define MAXN 55

using namespace std;

struct node {
	int laser, need;
	char column[7];
};

int main () {
	int T, iT;
	scanf("%d",&T);
	static char data[MAXN][MAXN];
	static char canRotate[MAXN][MAXN];
	static char a[MAXN][35][35];
	static node w[MAXN][35][35];
	for (iT = 0; iT < T; iT++) {
		int N, M;
		scanf("%d %d",&N,&M);
		int i, j;
		for (i = 0; i < N; i++) {
			scanf("\n%s",data[i]);
		}
		memset(canRotate, 0, sizeof(canRotate));
		for (i = 0; i < N; i++) {
			int last = -1;
			for (j = 0; j < M; j++) {
				if (data[i][j] == '#') {
					last = -1;
				} else if ((data[i][j] == '-') || (data[i][j] == '|')) {
					canRotate[i][j] = 1;
					if (last == -1) {
						last = j;
					} else {
						data[i][last] = '|';
						canRotate[i][last] = 0;
						last = j;
						data[i][last] = '|';
						canRotate[i][last] = 0;
					}
				}
			}
		}
		char isFail = 0;
		for (j = 0; j < M; j++) {
			int last = -1;
			for (i = 0; i < N; i++) {
				if (data[i][j] == '#') {
					last = -1;
				} else if ((data[i][j] == '-') || (data[i][j] == '|')) {
					if (last == -1) {
						last = i;
					} else {
						if ((data[last][j] == '|') && (canRotate[last][j] == 0)) {
							isFail = 1;
							break;
						}
						data[last][j] = '-';
						canRotate[last][j] = 0;
						last = i;
						if ((data[last][j] == '|') && (canRotate[last][j] == 0)) {
							isFail = 1;
							break;
						}
						data[last][j] = '-';
						canRotate[last][j] = 0;
					}
				}
			}
			if (isFail) {
				break;
			}
		}

		if (isFail) {
			printf("Case #%d: IMPOSSIBLE\n",iT+1);
			continue;
		}
/*
		for (i = 0; i < N; i++) {
			for (j = 0; j < M; j++) {
				if ((data[i][j] == '-') || (data[i][j] == '|')) {
					if (canRotate[i][j]) printf("?");
					else printf("%c",data[i][j]);
				} else printf("%c",data[i][j]);
			}
			printf("\n");
		}
*/

		memset(a, 0, sizeof(a));
		int totalmask = 1 << N;
		int laser, need, mask;
		a[0][0][0] = 1;
		for (j = 0; j < M; j++) {
			for (laser = 0; laser < totalmask; laser++) {
				for (need = 0; need < totalmask; need++) {
					if (a[j][laser][need]) {
						//printf("%d, %d, %d\n",j,laser,need);
						char column[7];
						int rotateable = 0;
						for (i = 0; i < N; i++) {
							if (((data[i][j] == '-') || (data[i][j] == '|')) && (canRotate[i][j])) {
								rotateable++;
							}
						}
						for (mask = 0; mask < (1 << rotateable); mask++) {

							for (i = 0; i < N; i++) {
								column[i] = data[i][j];
							}

							int laser2 = laser;
							int need2 = need;
							char isOK = 1;

							int mask2 = mask;
							for (i = 0; i < N; i++) {
								if (((data[i][j] == '-') || (data[i][j] == '|')) && (canRotate[i][j])) {
									if (mask2 % 2) {
										column[i] = '|';
									} else {
										column[i] = '-';
									}
									mask2 /= 2;
								}
							}

							char lit[7];
							memset(lit, 0, sizeof(lit));

							char isLaser = 0;
							for (i = 0; i < N; i++) {
								if (column[i] == '#') {
									lit[i] = 1;
									isLaser = 0;
								} else if (column[i] == '-') {
									lit[i] = 1;
								} else if (column[i] == '|') {
									lit[i] = 1;
									isLaser = 1;
								} else {
									if (isLaser) {
										lit[i] = 1;
									}
								}
							}
							isLaser = 0;
							for (i = N-1; i >= 0; i--) {
								if (column[i] == '#') {
									lit[i] = 1;
									isLaser = 0;
								} else if (column[i] == '-') {
									lit[i] = 1;
								} else if (column[i] == '|') {
									lit[i] = 1;
									isLaser = 1;
								} else {
									if (isLaser) {
										lit[i] = 1;
									}
								}
							}
							for (i = 0; i < N; i++) {
								if ((lit[i] == 0) && (laser & (1 << i))) {
									lit[i] = 1;
								}
							}

							for (i = 0; i < N; i++) {
								if (column[i] == '#') {
									laser2 &= ~(1 << i);
								} else if (column[i] == '-') {
									laser2 |= (1 << i);
								}
							}

							for (i = 0; i < N; i++) {
								if (column[i] == '#') {
									if (need & (1 << i)) {
										isOK = 0;
										break;
									}
								} else if (column[i] == '-') {
									need2 &= ~(1 << i);
								} else {
									if (lit[i] == 0) {
										//printf("NOT LIT %d WITH %d (OF %d)\n",i,(laser & (1 << i)),laser);
										need2 |= (1 << i);
									}
								}
							}

							if (isOK) {
								a[j+1][laser2][need2] = 1;
								w[j+1][laser2][need2].laser = laser;
								w[j+1][laser2][need2].need = need;
								for (i = 0; i < N; i++) {
									w[j+1][laser2][need2].column[i] = column[i];
								}
							}

						}
					}
				}
			}
		}

		char isGood = 0;
		for (laser = 0; laser < totalmask; laser++) {
			if (a[M][laser][0]) {
				isGood = 1;
				break;
			}
		}

		if (isGood) {
			printf("Case #%d: POSSIBLE\n",iT+1);
			j = M;
			need = 0;
			while (j) {
				for (i = 0; i < N; i++) {
					data[i][j-1] = w[j][laser][need].column[i];
				}
				int laser2 = w[j][laser][need].laser;
				int need2 = w[j][laser][need].need;
				laser = laser2;
				need = need2;
				j--;
			}
			for (i = 0; i < N; i++) {
				printf("%s\n",data[i]);
			}
		} else {
			printf("Case #%d: IMPOSSIBLE\n",iT+1);
			/*printf("$$$$$\n");
			for (i = 0; i < N; i++) {
				for (j = 0; j < M; j++) {
					if ((data[i][j] == '-') || (data[i][j] == '|')) {
						if (canRotate[i][j]) printf("?");
						else printf("%c",data[i][j]);
					} else printf("%c",data[i][j]);
				}
				printf("\n");
			}
			printf("$$$$$\n");*/
		}

	}
	return 0;
}
