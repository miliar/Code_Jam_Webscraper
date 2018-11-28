#include <bits/stdc++.h>

using namespace std;

int Test ,R, C;
char s[30][30];

int main(){
//	freopen("A-large.in", "r", stdin);
//	freopen("A-large.out", "w", stdout);
	scanf("%d", &Test);
	for (int tt = 1; tt <= Test; tt++){
		scanf("%d%d", &R, &C);
		for (int i = 1; i <= R; i++)
			scanf("%s", s[i] + 1);
		for (int i = 1; i <= R; i++)
			for (int j = 2; j <= C; j++)
				if (s[i][j - 1] != '?' && s[i][j] == '?')
					s[i][j] = s[i][j - 1];
		for (int i = 1; i <= R; i++)
			for (int j = C - 1; j > 0; j--)
				if (s[i][j + 1] != '?' && s[i][j] == '?')
					s[i][j] = s[i][j + 1];
		for (int i = 2; i <= R; i++)
			for (int j = 1; j <= C; j++)
				if (s[i - 1][j] != '?' && s[i][j] == '?')
					s[i][j] = s[i - 1][j];
		for (int i = R - 1; i > 0; i--)
			for (int j = 1; j <= C; j++)
				if (s[i + 1][j] != '?' && s[i][j] == '?')
					s[i][j] = s[i + 1][j];
		printf("Case #%d: \n", tt);
		for (int i = 1; i <= R; i++)
			printf("%s\n", s[i] + 1);
	}
}