#include <cstdio>
#include <cstring>
bool flip[1001] = {0}, valid;
char S[1001];
int T, K, len, num, ans;
int main (){
	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; i++){
		scanf("%s %d", S, &K);
		len = strlen(S);
		num = 0;
		ans = 0;
		for (int j = 0; j <= len - K; j++){
			if (j >= K)
				if (flip[j - K])
					num--;
			if ((S[j] == '-' && num % 2 == 0) || (S[j] == '+' && num % 2 == 1)){
				num++;
				ans++;
				flip[j] = true;
			} else 
				flip[j] = false;
		}
		valid = true;
		for (int j = len - K + 1; j < len; j++){
			if (j >= K){
				if (flip[j - K])
					num--;
			}
			if ((S[j] == '-' && num % 2 == 0) || (S[j] == '+' && num % 2 == 1))
				valid = false;
		}
		if (valid)
			printf("Case #%d: %d\n", i, ans);
		else 
			printf("Case #%d: IMPOSSIBLE\n", i);
	}
	fclose (stdin);
	fclose (stdout);
	return 0;
}
