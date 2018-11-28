#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <math.h>
#include <algorithm>
#include <vector>
using namespace std;

void solve(char arr[25][25], int R, int C) {
	for (int r =  0; r < R; r++) {
		char last = '?';
		for (int c =  0; c < C; c++) {
			if (arr[r][c] != '?') {
				last = arr[r][c];
			}
			if (last != '?'){
				for (int cc = 0; cc <= c; cc++) {
					if (arr[r][cc] == '?') {
						arr[r][cc] = last;
					}
				}
			}
		}
	}
	
	//find first letter
	if (arr[0][0] == '?') {
		for (int r = 1; r < R; r++) {
			if (arr[r][0] != '?') {
				for (int cc = 0; cc < C; cc++) {
					arr[0][cc] = arr[r][cc];
				}
				break;
			}
		}
	}

	for (int r = 1; r < R; r++) {
		for (int c = 0; c < C; c++) {
			if (arr[r][c] == '?') {
				arr[r][c] = arr[r - 1][c];
			}
		}
	}
}

int main() {
	//freopen("in.txt", "rt", stdin);
	freopen("A-large.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int T;
	scanf("%d\n", &T);

	for (int i = 1; i <= T; i++) {
		int R, C;
		scanf("%d %d\n", &R, &C);

		char arr[25][25] = { 0 };
		for (int j = 0; j < R; j++) {
			for (int k = 0; k < C; k++) {
				scanf("%c", &arr[j][k]);
			}
			scanf("\n");
		}

		solve(arr, R, C);

		printf("Case #%d: \n", i);
		for (int j = 0; j < R; j++) {
			for (int k = 0; k < C; k++) {
				printf("%c", arr[j][k]);
			}
			if (j != R - 1) {
				printf("\n");
			}
		}
		printf("\n");
	}

	return 0;
}