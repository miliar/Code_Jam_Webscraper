#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int tc, c = 0;
	scanf("%d", &tc);
	while (tc--) {
		c++;
		int R, C;
		char cake[30][30];
		vector<int> aa;

		scanf("%d %d\n", &R, &C);
		for (int i = 0; i < R; i++) scanf("%s", &cake[i]);

		for (int i = 0; i < R; i++) {
			char ch = '?';
			for (int j = 0; j < C; j++) {
				if (cake[i][j] != '?') ch = cake[i][j];
				cake[i][j] = ch;
			}
			for (int j = C - 1; j >= 0; j--) {
				if (cake[i][j] != '?') ch = cake[i][j];
				cake[i][j] = ch;
			}
		}
		int pivot = -1;
		for (int i = 0; i < R; i++) {
			if (cake[i][0] != '?') pivot = i;
			else if (pivot != -1) strcpy(cake[i], cake[pivot]);
		}
		pivot = -1;
		for (int i = R-1; i >= 0; i--) {
			if (cake[i][0] != '?') pivot = i;
			else if (pivot != -1) strcpy(cake[i], cake[pivot]);
		}

		printf("Case #%d: \n", c); 
		for (int i = 0; i < R; i++) printf("%s\n", cake[i]);
	}
}