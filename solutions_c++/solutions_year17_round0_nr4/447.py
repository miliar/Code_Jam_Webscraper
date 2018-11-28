#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	int count = 1;
	int N, M;
	while(scanf("%d%d", &N, &M) != EOF) {
		vector<vector<char>> v(N + 1, vector<char>(N + 1, '.'));
		for (int i = 0; i < M; i++) {
			char c[2];
			int m, n;
			scanf("%s%d%d", c, &m, &n);
			v[m][n] = c[0];
		}
		int point = 0;
		int sub = 0;
		int unsub = 0;
		int x, y;
		for (int i = 1; i <= N; i++) {
			if(v[1][i] != '.')
				point++;
			if(v[1][i] == 'x') {
				x = 1;
				y = i;
				sub = 1;
			}
			if(v[1][i] == 'o') {
				x = 1;
				y = i;
				unsub = 1;
			}
		}
		if (!unsub && !sub && point == N) {
			sub = 1;
			x = 1;
			y = 1;
		}
		int score = N + 1 + max(0, N - 2) + max(0, N - 1);
		printf("Case #%d: %d %d\n", count++, score, score - 1 - point + sub);
		if (sub) {
			printf("o %d %d\n", x, y);
		}
		else if (!unsub){
			for (int i = 1; i <= N; i++) {
				if (v[1][i] == '.') {
					v[1][i] = 'o';
					printf("o %d %d\n", 1, i);
					x = 1;
					y = i;
					break;
				}
			}
		}
		for (int i = 1; i <= N; i++) {
			if (v[1][i] == '.') {
				printf("+ %d %d\n", 1, i);
			}
		}
		int r = 2;
		for (int i = y - 1; i >= 1; i--) {
			printf("x %d %d\n", r++, i);
		}
		for (int i = y + 1; i <= N; i++) {
			printf("x %d %d\n", r++, i);
		}
		for (int i = 2; i <= N - 1; i++) {
			printf("+ %d %d\n", N, i);
		}
	}
}