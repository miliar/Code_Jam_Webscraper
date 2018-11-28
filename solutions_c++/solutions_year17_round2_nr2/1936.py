#include<stdio.h>
#include<queue>
using namespace std;
#define Max(a,b) (a > b ? a : b)
int S[1001], arr[7], N;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, test = 1;
	scanf("%d", &t);
	while (test <= t) {
		printf("Case #%d: ", test++);
		int tmp[7] = { 0, }; // R, O, Y, G, B, V
		scanf("%d", &N);
		for (int i = 0; i < 6; i++) {
			scanf("%d", &arr[i]);
			tmp[i] = arr[i];
		}
		if (tmp[1]) {
			if (tmp[1] > tmp[4]) {
				printf("IMPOSSIBLE\n");
				continue;
			}
			else if (tmp[1] == tmp[4]) {
				if (tmp[1] * 2 == N) {
					for (int i = 0; i < N / 2; i++)
						printf("OB");
					printf("\n");
					continue;
				}
				else {
					printf("IMPOSSIBLE\n");
					continue;
				}
			}
			tmp[4] -= tmp[1];
		}
		else if (tmp[3]) {
			if (tmp[3]  > tmp[0]) {
				printf("IMPOSSIBLE\n");
				continue;
			}
			else if (tmp[3] == tmp[0]) {
				if (tmp[3] * 2 == N) {
					for (int i = 0; i < N / 2; i++)
						printf("GR");
					printf("\n");
					continue;
				}
				else {
					printf("IMPOSSIBLE\n");
					continue;
				}
			}
			tmp[0] -= tmp[3];
		}
		else if (tmp[5]) {
			if (tmp[5] > tmp[2]) {
				printf("IMPOSSIBLE\n");
				continue;
			}
			else if (tmp[5] == tmp[2]) {
				if (tmp[2] * 2 == N) {
					for (int i = 0; i < N / 2; i++)
						printf("VY");
					printf("\n");
					continue;
				}
				else {
					printf("IMPOSSIBLE\n");
					continue;
				}
			}
			tmp[2] -= tmp[5];
		}
		int max = 0, sum = 0;
		sum = tmp[0] + tmp[2] + tmp[4];
		max = Max(Max(tmp[0], tmp[2]), tmp[4]);
		if (max > sum - max) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		int order[3];
		if (tmp[0] >= tmp[2] && tmp[0] >= tmp[4]) {
			order[0] = 0;
			order[1] = 2;
			order[2] = 4;
		}
		else if (tmp[2] >= tmp[0] && tmp[2] >= tmp[4]) {
			order[0] = 2;
			order[1] = 0;
			order[2] = 4;
		}
		else {
			order[0] = 4;
			order[1] = 0;
			order[2] = 2;
		}
		while (1) {
			if (tmp[order[0]] == tmp[order[1]] + tmp[order[2]]) {
				for (int j = 0; j < tmp[order[1]]; j++) {
					if (tmp[(order[0] + 3) % 6]) {
						if (order[0] == 0) {
							printf("R");
						}
						else if (order[0] == 2) {
							printf("Y");
						}
						else {
							printf("B");
						}
						for (int k = 0; k < tmp[(order[0] + 3) % 6]; k++) {
							if (order[0] == 0) {
								printf("GR");
							}
							else if (order[0] == 2) {
								printf("VY");
							}
							else {
								printf("OB");
							}
						}
						tmp[(order[0] + 3) % 6] = 0;
					}
					else {
						if (order[0] == 0) {
							printf("R");
						}
						else if (order[0] == 2) {
							printf("Y");
						}
						else {
							printf("B");
						}
					}
					if (tmp[(order[1] + 3) % 6]) {
						if (order[1] == 0) {
							printf("R");
						}
						else if (order[1] == 2) {
							printf("Y");
						}
						else {
							printf("B");
						}
						for (int k = 0; k < tmp[(order[1] + 3) % 6]; k++) {
							if (order[1] == 0) {
								printf("GR");
							}
							else if (order[1] == 2) {
								printf("VY");
							}
							else {
								printf("OB");
							}
						}
						tmp[(order[1] + 3) % 6] = 0;
					}
					else {
						if (order[1] == 0) {
							printf("R");
						}
						else if (order[1] == 2) {
							printf("Y");
						}
						else {
							printf("B");
						}
					}
				}
				for (int j = 0; j < tmp[order[2]]; j++) {
					if (tmp[(order[0] + 3) % 6]) {
						if (order[0] == 0) {
							printf("R");
						}
						else if (order[0] == 2) {
							printf("Y");
						}
						else {
							printf("B");
						}
						for (int k = 0; k < tmp[(order[0] + 3) % 6]; k++) {
							if (order[0] == 0) {
								printf("GR");
							}
							else if (order[0] == 2) {
								printf("VY");
							}
							else {
								printf("OB");
							}
						}
						tmp[(order[0] + 3) % 6] = 0;
					}
					else {
						if (order[0] == 0) {
							printf("R");
						}
						else if (order[0] == 2) {
							printf("Y");
						}
						else {
							printf("B");
						}
					}
					if (tmp[(order[2] + 3) % 6]) {
						if (order[2] == 0) {
							printf("R");
						}
						else if (order[2] == 2) {
							printf("Y");
						}
						else {
							printf("B");
						}
						for (int k = 0; k < tmp[(order[2] + 3) % 6]; k++) {
							if (order[2] == 0) {
								printf("GR");
							}
							else if (order[2] == 2) {
								printf("VY");
							}
							else {
								printf("OB");
							}
						}
						tmp[(order[2] + 3) % 6] = 0;
					}
					else {
						if (order[2] == 0) {
							printf("R");
						}
						else if (order[2] == 2) {
							printf("Y");
						}
						else {
							printf("B");
						}
					}
				}
				break;
			}
			else {
				for (int i = 0; i < 3; i++) {
					if (tmp[(order[i] + 3) % 6]) {
						if (order[i] == 0) {
							printf("R");
						}
						else if (order[i] == 2) {
							printf("Y");
						}
						else {
							printf("B");
						}
						for (int j = 0; j < tmp[(order[i] + 3) % 6]; j++) {
							if (order[i] == 0) {
								printf("GR");
							}
							else if (order[i] == 2) {
								printf("VY");
							}
							else {
								printf("OB");
							}
						}
						tmp[(order[i] + 3) % 6] = 0;
					}
					else {
						if (order[i] == 0) {
							printf("R");
						}
						else if (order[i] == 2) {
							printf("Y");
						}
						else {
							printf("B");
						}
					}
				}
				tmp[order[0]]--;
				tmp[order[1]]--;
				tmp[order[2]]--;
			}
		}
		printf("\n");
	}
}