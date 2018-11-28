#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

const int MaxN = 100;
string s;
int T, K;
int a[MaxN + 5], b[MaxN + 5];

bool Check(int s, int a[], int len)
{
	for (int i = 0; i < len; i++)
		if (s & (1 << i)) {
			if (i + K - 1 >= len) return false;
			for (int j = i; j <= i + K - 1; j++)
				a[j] = 1 - a[j];
		}
	for (int i = 0; i < len; i++) 
		if (a[i] == 0) return false;
	return true;
}

int Count(int s)
{
	int cnt = 0;
	while (s != 0) {
		cnt = cnt + (s & 1);	
		s >>= 1;
	}
	return cnt;
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		cin >> s; scanf("%d", &K);
		for (int i = 0; i < s.length(); i++)
			a[i] = s[i] == '-' ? 0 : 1;
		int ans = 1 << 30;
		for (int St = 0; St < (1 << s.length()); St++) {
			for (int i = 0; i < s.length(); i++) b[i] = a[i];
			if (Check(St, b, s.length())) ans = min(ans, Count(St));
		}
		if (ans == (1 << 30)) printf("Case #%d: IMPOSSIBLE\n", cas);
		else printf("Case #%d: %d\n", cas, ans);
	}
	fclose(stdin);
	fclose(stdout);
}
