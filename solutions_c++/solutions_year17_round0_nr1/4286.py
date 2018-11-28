#include <cstdio>
#include <cstring>
const int maxn = 1000 + 5;

void re(char &a) {
	if(a == '+') a = '-';
	else a = '+';
}

void solve() {
	char str[maxn] = {};
	int K;
	int len;
	int cnt = 0;
	scanf("%s %d", str, &K);
	len = strlen(str);
	for(int i = 0; i <= len-K; i++) if(str[i] == '-') {
		for(int j = 0; j < K; j++) re(str[i+j]);
		cnt++;
	}
	bool ok = 1;
	for(int i = 0; i < len; i++) if(str[i] == '-') ok = 0;
	if(ok == 1) printf("%d\n", cnt);
	else printf("IMPOSSIBLE\n");
}


int main() {
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++) {
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}
