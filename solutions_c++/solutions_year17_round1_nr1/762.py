#include <cstdio>
char map[30][30];
int width[36];
int skip[36];
void work(){
	int R,C;
	scanf("%d%d", &R, &C);
	for (int i = 0; i < R; i++){
		scanf("%s", map[i]);
	}

	for (int i = 0; i < 26; i++) {
		width[i] = 1;
		skip[i] = false;
	}

	for (int i = 0; i < R; i++)
		for (int j = 0; j < C; j++){
			if (map[i][j] != '?'){
				for (int k = j - 1; k >= 0; k--){
					if (map[i][k] == '?'){
						map[i][k] = map[i][j];
						width[map[i][j] - 'A']++;
					} else break;
				}
				for (int k = j + 1; k < C; k++){
					if (map[i][k] == '?'){
						map[i][k] = map[i][j];
						width[map[i][j] - 'A']++;
					} else break;
				}
			}
		}
	for (int i = 0; i < R; i++)
		for (int j = 0; j < C; j++){
			if (map[i][j] != '?' && skip[map[i][j] - 'A'] == false){
				skip[map[i][j] - 'A'] = true;
				for (int k = i - 1; k >= 0; k--){
					if (map[k][j] == '?'){
						bool can_go = true;
						for (int l = j; l < j + width[map[i][j] - 'A']; l++)
							if (map[k][l] != '?') {
								can_go = false;
								break;
							}
						if (can_go) 
							for (int l = j; l < j + width[map[i][j] - 'A']; l++)
								map[k][l] = map[i][j];
						else break;
					} else break;
				}
				for (int k = i + 1; k < R; k++){
					if (map[k][j] == '?'){
						bool can_go = true;
						for (int l = j; l < j + width[map[i][j] - 'A']; l++)
							if (map[k][l] != '?') {
								can_go = false;
								break;
							}
						if (can_go) 
							for (int l = j; l < j + width[map[i][j] - 'A']; l++)
								map[k][l] = map[i][j];
						else break;
					} else break;
				}
			}
		}
	puts("");
	for (int i = 0; i < R; i++)
		printf("%s\n", map[i]);
}

int main(){
	freopen("A.in", "r", stdin);
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; i++){
		printf("Case #%d:", i);
		work();
	}
}