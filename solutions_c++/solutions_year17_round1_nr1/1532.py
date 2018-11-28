#include <stdio.h>
#include <string.h>
const int R = 25;
const int C = 25;
int main() {
	char cake[R+1][C+1];
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int r, c;
		scanf("%d %d", &r, &c);
		printf("Case #%d:\n", t);
		for (int i = 0; i < r; ++i)
			scanf("%s", cake[i]);
		for (int i = 0; i < r; ++i) {
			for (int j = c -1; j >= 0; --j) {
				if (cake[i][j] != '?') {
					for (int a = j +1; a < c; ++a)
						if (cake[i][a] == '?')
							cake[i][a] = cake[i][j];
						else
							break;
				}
			}
			for (int j = 0; j < c; ++j) {
				if (cake[i][j] != '?')
					for (int a = 0; a < j; ++a)
						if (cake[i][a] == '?')
							cake[i][a] = cake[i][j];
			}
		}

		for (int i = 0; i < r; ++i)
			if (cake[i][0] != '?')
				for (int a = i -1; a >= 0; --a)
					if (cake[a][0] == '?')
						for (int j = 0; j < c; ++j)
							cake[a][j] = cake[i][j];
		
		for (int i = r -1; i >= 0; --i)
			if (cake[i][0] != '?')
				for (int a = i +1; a < r; ++a)
					if (cake[a][0] == '?')
						for (int j = 0; j < c; ++j)
							cake[a][j] = cake[i][j];


		for (int i = 0; i < r; ++i)
			printf("%s\n", cake[i]);
	}
	return 0;
}
