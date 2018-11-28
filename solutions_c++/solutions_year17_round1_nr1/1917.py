#include <cstdio>

int R, C;
char s[25][26];

void solve() {
    scanf("%d%d", &R, &C);
    for (int i = 0, j = 0; i < R; i++) {
	scanf("%s", s[i]);
	for (j = 0; j < C && s[i][j] == '?'; j++);
	if (j >= C)
	    continue;
	for (int k = j - 1; k >= 0; k--)
	    s[i][k] = s[i][j];
	for (; j < C; j++)
	    if (s[i][j] == '?')
		s[i][j] = s[i][j - 1];
    }
    for (int i = 0, j = 0; i < C; i++) {
	for (j = 0; j < R && s[j][i] == '?'; j++);
	for (int k = j - 1; k >= 0; k--)
	    s[k][i] = s[j][i];
	for (; j < R; j++)
	    if (s[j][i] == '?')
		s[j][i] = s[j - 1][i];
    }
    for (int i = 0; i < R; i++)
	puts(s[i]);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
	printf("Case #%d:\n", i);
	solve();
    }
}
