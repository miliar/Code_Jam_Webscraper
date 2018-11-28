#include<bits/stdc++.h>
using namespace std;
long long num, ret;
int len;
int digits[20];
bool dfs(int now, bool flag, int pre, long long ans) {
	if (now == -1) {
		ret = ans;
		return true;
	}
	if (flag) {
		return dfs(now - 1, flag, 9, ans * 10 + 9);
	}
	if (digits[now]<pre) {
		return false;
	}
	if (dfs(now - 1, flag, digits[now], ans * 10 + digits[now]))
		return true;
	else if (digits[now] - 1<pre) {
		return false;
	}
	else {
		return dfs(now - 1, true, digits[now] - 1, ans * 10 + digits[now] - 1);
	}
}
int main() {
	#ifndef ONLINE_JUDGE
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	#endif
	int T, cas = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%lld", &num);
		len = 0;
		while (num) {
			digits[len++] = num % 10;
			num /= 10;
		}
		dfs(len - 1, false, 0, 0);
		printf("Case #%d: %lld\n",++cas,ret);
	}
	return 0;
}
