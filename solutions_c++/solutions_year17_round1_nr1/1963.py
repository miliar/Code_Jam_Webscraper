#include <cstdio>
#include <vector>
#include <algorithm>
int main(){
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++){
		char s[30][30] = { 0 };
		int c[30][4] = { 0 };
		printf("Case #%d:\n", tc);
		int R, C;

		scanf("%d%d", &R, &C);
		for (int i = 1; i <= R; i++) {
			scanf("%s", s[i] + 1);
			int pv = '?';
			for (int j = 1; j <= C; j++){
				if (s[i][j] != '?' && pv == '?') pv = s[i][j];
			}
			if (pv != '?'){
				for (int j = 1; j <= C; j++){
					if (s[i][j] != '?') pv = s[i][j];
                    s[i][j] = pv;
					for (int k = i-1; k >= 1; k--){
						if (s[k][j] == '?') s[k][j] = pv;
						else break;
					}
				}
			}
			else {
				for (int j = 1; j <= C; j++)
				if (s[i-1][j] != 0 && s[i-1][j] != '?') {
					s[i][j] = s[i - 1][j];
				}
			}
		}
		for (int i = 1; i <= R; i++){
			printf("%s\n", s[i]+1);
		}
	}

}
