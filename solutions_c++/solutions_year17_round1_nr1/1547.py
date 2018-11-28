#include <bits/stdc++.h>

using namespace std;

int t, r, c;
char ch, arr[30][30];

int main() {
	freopen("inn", "r", stdin);
	freopen("myfile.txt", "w", stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%d%d", &r, &c);
		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				scanf(" %c", &arr[j][k]);
				if (arr[j][k] != '?') {
					ch = arr[j][k];
				}
			}
		}
		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				if (arr[j][k] != '?') {
					int countt = k;
					countt++;
					ch = arr[j][k];
					while (arr[j][countt] == '?') {
						arr[j][countt] = ch;
						countt++;
					}
					countt = k - 1;
					while (countt >= 0 && arr[j][countt] == '?') {
						arr[j][countt] = ch;
						countt--;
					}
				}
			}
		}
		for (int j = 1; j < r; j++) {
			for (int k = 0; k < c; k++) {
				if (arr[j][k] == '?') {
					arr[j][k] = arr[j - 1][k];
				}
			}
		}
		for (int j = r - 2; j >= 0; j--) {
			for (int k = 0; k < c; k++) {
				if (arr[j][k] == '?') {
					arr[j][k] = arr[j + 1][k];
				}
			}
		}
		printf("Case #%d:\n", i);
		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				printf("%c", arr[j][k]);
			}
			printf("\n");
		}
	}
	return 0;
}
