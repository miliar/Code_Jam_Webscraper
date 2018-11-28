#include <bits/stdc++.h>
void Main(){
	char s[111];
	scanf("%s", s);
	int len = strlen(s);
	long long ans = 0, now = 0;
	for (int i = 0; i <= len; i ++ ){
		if (i == len){
			ans = now;
			break;
		}
		now = now * 10 + s[i] - '0';
		if (now % 10 == (now % 100) / 10) continue;
		if (now % 10 < (now % 100) / 10) break;
		long long tmp = now - 1;
		for (int j = 1; j < len - i; j ++ )
			tmp = tmp * 10 + 9;
		if (tmp > ans) ans = tmp;
	}
	printf("%lld\n", ans);
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
