#include <cstdio>
#include <vector>
#include <cassert>
#include <algorithm>

int solve2(int A, int B) {
	const int p = 2;
	assert(0 <= A && A <= 100);
	assert(0 <= B && B <= 100);
	static int max[101][101];
	for (int a = 0; a <= A; a++) {
		for (int b = 0; b <= B; b++) {
			max[a][b] = 0;
			if (a > 0) {
				if (((a - 1) * 0 + b * 1) % p == 0) {
					max[a][b] = std::max(max[a][b], max[a - 1][b] + 1);
				} else {
					max[a][b] = std::max(max[a][b], max[a - 1][b]);
				}
			}
			if (b > 0) {
				if ((a * 0 + (b - 1) * 1) % p == 0) {
					max[a][b] = std::max(max[a][b], max[a][b - 1] + 1);
				} else {
					max[a][b] = std::max(max[a][b], max[a][b - 1]);
				}
			}
		}
	}
	return max[A][B];
}

int solve3(int A, int B, int C) {
	const int p = 3;
	assert(0 <= A && A <= 100);
	assert(0 <= B && B <= 100);
	assert(0 <= C && C <= 100);
	static int max[101][101][101];
	for (int a = 0; a <= A; a++) {
		for (int b = 0; b <= B; b++) {
			for (int c = 0; c <= C; c++) {
				max[a][b][c] = 0;
				if (a > 0) {
					if (((a - 1) * 0 + b * 1 + c * 2) % p == 0) {
						max[a][b][c] = std::max(max[a][b][c], max[a - 1][b][c] + 1);
					} else {
						max[a][b][c] = std::max(max[a][b][c], max[a - 1][b][c]);
					}
				}
				if (b > 0) {
					if ((a * 0 + (b - 1) * 1 + c * 2) % p == 0) {
						max[a][b][c] = std::max(max[a][b][c], max[a][b - 1][c] + 1);
					} else {
						max[a][b][c] = std::max(max[a][b][c], max[a][b - 1][c]);
					}
				}
				if (c > 0) {
					if ((a * 0 + b * 1 + (c - 1) * 2) % p == 0) {
						max[a][b][c] = std::max(max[a][b][c], max[a][b][c - 1] + 1);
					} else {
						max[a][b][c] = std::max(max[a][b][c], max[a][b][c - 1]);
					}
				}
			}
		}
	}
	return max[A][B][C];
}

int solve4(int A, int B, int C, int D) {
	const int p = 4;
	assert(0 <= A && A <= 100);
	assert(0 <= B && B <= 100);
	assert(0 <= C && C <= 100);
	assert(0 <= D && D <= 100);
	static int max[101][101][101][101];
	for (int a = 0; a <= A; a++) {
		for (int b = 0; b <= B; b++) {
			for (int c = 0; c <= C; c++) {
				for (int d = 0; d <= D; d++) {
					max[a][b][c][d] = 0;
					if (a > 0) {
						if (((a - 1) * 0 + b * 1 + c * 2 + d * 3) % p == 0) {
							max[a][b][c][d] = std::max(max[a][b][c][d], max[a - 1][b][c][d] + 1);
						} else {
							max[a][b][c][d] = std::max(max[a][b][c][d], max[a - 1][b][c][d]);
						}
					}
					if (b > 0) {
						if ((a * 0 + (b - 1) * 1 + c * 2 + d * 3) % p == 0) {
							max[a][b][c][d] = std::max(max[a][b][c][d], max[a][b - 1][c][d] + 1);
						} else {
							max[a][b][c][d] = std::max(max[a][b][c][d], max[a][b - 1][c][d]);
						}
					}
					if (c > 0) {
						if ((a * 0 + b * 1 + (c - 1) * 2 + d * 3) % p == 0) {
							max[a][b][c][d] = std::max(max[a][b][c][d], max[a][b][c - 1][d] + 1);
						} else {
							max[a][b][c][d] = std::max(max[a][b][c][d], max[a][b][c - 1][d]);
						}
					}
					if (d > 0) {
						if ((a * 0 + b * 1 + c * 2 + (d - 1) * 3) % p == 0) {
							max[a][b][c][d] = std::max(max[a][b][c][d], max[a][b][c][d - 1] + 1);
						} else {
							max[a][b][c][d] = std::max(max[a][b][c][d], max[a][b][c][d - 1]);
						}
					}
				}
			}
		}
	}
	return max[A][B][C][D];
}

int solveOne() {
	int nG, perPack;
	scanf("%d %d", &nG, &perPack);
	std::vector<int> count(perPack, 0);
	for (int i = 0; i < nG; i++) {
		int v;
		scanf("%d", &v);
		count[v % perPack]++;
	}
	if (perPack == 2) {
		return solve2(count[0], count[1]);
	} else if (perPack == 3) {
		return solve3(count[0], count[1], count[2]);
	} else {
		assert(perPack == 4);
		return solve4(count[0], count[1], count[2], count[3]);
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: %d\n", i, solveOne());
	}
	return 0;
}
