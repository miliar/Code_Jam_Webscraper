#include <stdio.h>
#include <string.h>
char pan[2001];
int T, K, len, cnt;
bool isHappy(){
	for (int i = 0; i < len; i++){
		if (pan[i] == '-') return false;
	}
	return true;
}
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int i = 0; i < T; i++){
		scanf("%s %d", &pan, &K);
		len = strlen(pan);
		cnt = 0;
		for (int j = 0; j < len - K + 1;j++){
			if (pan[j] == '-'){
				cnt++;
				for (int k = j; k < j + K; k++){
					pan[k] = pan[k] == '-' ? '+' : '-';
				}
			}
		}
		if (!isHappy())
			printf("Case #%d: IMPOSSIBLE\n", i + 1);
		else
			printf("Case #%d: %d\n", i + 1, cnt);
	}
	return 0;
}