#include <cstring>
#include <iostream>
using namespace std;
const int nmax = 25 + 18;

int T, R, C;
char a[nmax][nmax];
bool exist[nmax];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int cases = 1; cases <= T; ++cases) {
		scanf("%d%d", &R, &C);
		for (int i = 1; i <= R; ++i) {
			scanf("%s", a[i] + 1);
			exist[i] = 0;
			for (int j = 1; j <= C; ++j)
				if (a[i][j] != '?') {
					exist[i] = 1;
					break;
				}
		}
		int cur_c = -1;
		for (int i = 1; i <= R; ++i) {
			if (exist[i]) {
				int cur_d = -1;
				for (int j = 1; j <= C; ++j)
					if (a[i][j] != '?') {
						if (cur_d == -1) {
							for (int k = 1; k < j; ++k)
								a[i][k] = a[i][j];
						}
						cur_d = a[i][j];
					}
					else if (a[i][j] == '?') {
						if (cur_d != -1)
							a[i][j] = cur_d;
					}
				if (cur_c == -1)
					for (int k = 1; k < i; ++k)
						for (int j = 1; j <= C; ++j)
							a[k][j] = a[i][j];
				cur_c = i;
			}
			else {
				if (cur_c != -1)
					for (int j = 1; j <= C; ++j)
						a[i][j] = a[cur_c][j];
			}
		}
		printf("Case #%d:\n", cases);
		for (int i = 1; i <= R; ++i)
			printf("%s\n", a[i] + 1);
	}
	return 0;
}
