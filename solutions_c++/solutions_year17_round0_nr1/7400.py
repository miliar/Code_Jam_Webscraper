#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>
#include<string>
using namespace std;
const int N = 1000 + 10;

char str[N];
bool flip[N];
int calc(string str, int n,int k) {
	int ans = 0;
	memset(flip, 0, sizeof flip);
	bool f = false;
	for (int i = 0; i < n; ++i) {
		if (flip[i])
			f = !f;
		if (f)
			str[i] = '1' - str[i] + '0';
		if (i<n-k && str[i]=='0') {
			++ans;
			f = !f;
			flip[i + k] = true;
		}
	}
	for (int i = n - k + 1; i < n; ++i)
		if (str[i]!=str[i-1])
			return -1;

	return ans+('1'-str[n-1]);
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for(int cas=1;cas<=t;++cas) {
		printf("Case #%d: ", cas);
		scanf("%s", str);
		int k;
		scanf("%d", &k);
		int n = strlen(str);
		for (int i = 0; i < n; ++i)
			if (str[i] == '+')
				str[i] = '1';
			else str[i] = '0';
		string s = str;
		int ans1 = calc(s, n, k);
		reverse(s.begin(), s.end());
		int ans2 = calc(s, n, k);
		if (ans1 == -1 && ans2 == -1)
			puts("IMPOSSIBLE");
		else if (ans1 == -1)
			printf("%d\n", ans2);
		else if (ans2 == -1)
			printf("%d\n", ans1);
		else
			printf("%d\n", min(ans1, ans2));


	}


	return 0;
}
