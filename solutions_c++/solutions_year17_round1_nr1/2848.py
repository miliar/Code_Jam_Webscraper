#include<stdio.h>
#include<vector>

int map[26][26];
char S[26][26];
bool used[26];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test = 1, t;
	scanf("%d", &t);
	while (test <= t) {
		printf("Case #%d:\n", test++);
		int n, m;
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; i++) {
			scanf("%s", S[i]);
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (S[i][j] == '?') {
					map[i][j] = 0;
				}
				else {
					map[i][j] = S[i][j] - 'A' + 1;
				}
			}
		}
		for (int i = 0; i < 26; i++)
			used[i] = false;
		for (int i = 0; i < n; i++) { // 위 아래 채우기
			for (int j = 0; j < m; j++) {
				if (map[i][j] && !used[map[i][j]]) {
					used[map[i][j]] = true;
					for (int k = 1; i + k < n && map[i + k][j] == 0; k++) {
						map[i + k][j] = map[i][j];
					}
					for (int k = 1; 0 <= i - k && map[i - k][j] == 0; k++) {
						map[i - k][j] = map[i][j];
					}
				}
			}
		}
		for (int i = 0; i < 26; i++)
			used[i] = false;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] && !used[map[i][j]]) {
					used[map[i][j]] = true;
					int len = 1;
					while (i + len < n && map[i][j] == map[i+len][j]) len++;
					bool avail = true;
					for (int k = 1; j + k < m; k++) {
						for (int l = 0; l < len; l++) {
							if (map[i+l][j + k] != 0) {
								avail = false;
								break;
							}
						}
						if (!avail) {
							break;
						}
						for (int l = 0; l < len; l++) {
							map[i+l][j + k] = map[i][j];
						}
					}
					avail = true;
					for (int k = 1; 0 <= j - k ; k++) {
						for (int l = 0; l < len; l++) {
							if (map[i+l][j - k] != 0) {
								avail = false;
								break;
							}
						}
						if (!avail) {
							break;
						}
						for (int l = 0; l < len; l++) {
							map[i+l][j - k] = map[i][j];
						}
					}
				}
			}
		}
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++) {
				printf("%c", map[i][j] + 'A'-1);
			}
			printf("\n");
		}
	}
}