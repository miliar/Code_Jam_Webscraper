#include <cstdio>
char s[26][26];
int T, R, C, cnt;
int main (){
	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; i++){
		scanf("%d %d", &R, &C);
		for (int j = 0; j < R; j++)
			scanf("%s", s[j]);
		for (int j = 0; j < R; j++){
			for (int k = 0; k < C - 1; k++){
				if (s[j][k] != '?' && s[j][k + 1] == '?')
					s[j][k + 1] = s[j][k];
			}
			for (int k = C - 1; k >= 1; k--){
				if (s[j][k] != '?' && s[j][k - 1] == '?')
					s[j][k - 1] = s[j][k];
			}
		}
		for (int j = 1; j < R; j++){
			cnt = 0;
			for (int k = 0; k < C; k++)
				if (s[j][k] == '?')
					cnt++;
			if (cnt == C){
				for (int k = 0; k < C; k++)
					s[j][k] = s[j - 1][k];
			}
		}
		for (int j = R - 2; j >= 0; j--){
			cnt = 0;
			for (int k = 0; k < C; k++)
				if (s[j][k] == '?')
					cnt++;
			if (cnt == C){
				for (int k = 0; k < C; k++)
					s[j][k] = s[j + 1][k];
			}
		}
		printf("Case #%d:\n", i);
		for (int j = 0; j < R; j++)
			printf("%s\n", s[j]);
	}
	fclose (stdin);
	fclose (stdout);
	return 0;
}
