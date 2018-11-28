#include <stdio.h>
#include <bits/stdc++.h>
#define ll long long
#define ull unsigned long long
using namespace std;
const int N = 1500;
int f(char st[], int w)
{
	int len = strlen(st);
	int cnt = 0;
	for (auto i = 0; i <= len - w; i++)
	{
		if (st[i] == '-')
		{
			cnt++;
			for (auto j = i; j < i + w; j++)
				st[j] = (st[j] == '+') ? '-' : '+';
		}
	}
	for (auto i = 0; i < len; i++)
		if (st[i] == '-')
			return -1;
	return cnt;
}

int main()
{
	int i, n, t, k;
	char s[N];
	vector<ll> x;
	scanf("%d", &t);
	for (i = 0; i < t; i++)
	{
		scanf("%s %d", s, &k);
		auto ans = f(s, k);
		if(ans==-1)
			printf("Case #%d: IMPOSSIBLE\n", i+1);
		else
			printf("Case #%d: %d\n", i+1, ans);
	}
	return 0;
}