#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

char a[35][35], b[35][35];

int main() {
	int Test;
	scanf("%d", &Test);
	for (int test = 1; test <= Test; test++) {
		int M, N;
		scanf("%d%d", &M, &N);
		for (int i = 0; i < M; i++) {
			scanf("%s", &a[i]);
			memcpy(b, a, sizeof(a));
		}
		for (int i = 0; i < M; i++)
			for (int j = 0; j < N; j++) {
				if (a[i][j] == '?') continue;
				int l = j, r = j;
				while (l > 0 && b[i][l - 1] == '?') l--;
				while (r < N - 1 && b[i][r + 1] == '?') r++;
				int u = i, d = i;
				while (u > 0) {
					bool flag = true;
					for (int k = l; k <= r && flag; k++) flag &= b[u - 1][k] == '?';
					if (!flag) break;
					u--;
				}
				while (d < M - 1) {
					bool flag = true;
					for (int k = l; k <= r && flag; k++) flag &= b[d + 1][k] == '?';
					if (!flag) break;
					d++;
				}
				for (int k = u; k <= d; k++)
					for (int p = l; p <= r; p++)
						b[k][p] = a[i][j];
			}
		printf("Case #%d:\n", test);
		for (int i = 0; i < M; i++) printf("%s\n", b[i]);
	}
}