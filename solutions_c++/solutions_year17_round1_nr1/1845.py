#include<cstdio>
const int maxc = 25 + 5;

int R, C, kase;
char maps[maxc][maxc];

void solve()
{
	for(int i = 0; i < R; i++) {
		for(int j = 0; j < C-1; j++) {
			if(maps[i][j] != '?' && maps[i][j+1] == '?') maps[i][j+1] = maps[i][j];
		}
	}
	for(int i = 0; i < R; i++) {
		for(int j = C-1; j > 0; j--) {
			if(maps[i][j] != '?' && maps[i][j-1] == '?') maps[i][j-1] = maps[i][j];
		}
	}
	for(int j = 0; j < C; j++) {
		for(int i = 0; i < R-1; i++) {
			if(maps[i][j] != '?' && maps[i+1][j] == '?') maps[i+1][j] = maps[i][j];
		}
	}

	for(int j = 0; j < C; j++) {
		for(int i = R-1; i > 0; i--) {
			if(maps[i][j] != '?' && maps[i-1][j] == '?') maps[i-1][j] = maps[i][j];
		}
	}

	printf("Case #%d:\n", ++kase);
	for(int i = 0; i < R; i++) {
		for(int j = 0; j < C; j++) {
			printf("%c", maps[i][j]);
		}
		putchar('\n');
	}
}

int main()
{
	kase = 0;
	int T;
	scanf("%d", &T);

	while(T--) {
		scanf("%d%d", &R, &C);
		for(int i = 0; i < R; i++) {
			getchar();
			for(int j = 0; j < C; j++) scanf("%c", &maps[i][j]);
		}

		solve();
	}

	return 0;
}
