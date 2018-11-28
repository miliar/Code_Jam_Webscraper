#include <bits/stdc++.h>
int k;
char s[1111];
void Main(){
	scanf("%s%d", s, &k);
	int n = strlen(s);
	int ans = 0;
	for (int i = 0; i < n; i ++ ){
		if (i + k > n) break;
		if (s[i] == '-'){
			ans ++ ;
			for (int j = 0; j < k; j ++ )
				s[i + j] = '+' + '-' - s[i + j];
		}
	}
	for (int i = 0; i < n; i ++ )
		if (s[i] == '-'){
			printf("IMPOSSIBLE\n");
			return;
		}
	printf("%d\n", ans);
}
int main(){
	int _;
	freopen("t.out", "w", stdout);
	scanf("%d", &_);
	for (int i = 1; i <= _; i ++ ){
		printf("CASE #%d: ", i);
		Main();
	}
}
