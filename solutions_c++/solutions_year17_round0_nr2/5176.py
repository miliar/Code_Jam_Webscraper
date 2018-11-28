#include <stdio.h>
#include <bits/stdc++.h>
#define ll long long
#define ull unsigned long long
using namespace std;
const int N = 100005;
char s[25];
string f()
{
	int len = strlen(s);
	for (auto i = len-1; i > 0; i--)
	{
		if (s[i] < s[i - 1])
		{
			for (auto j = i; j <= len-1; j++)
				s[j] = '9';
			s[i - 1]--;
		}
	}
	string ans = "";
	bool flag = false;
	for (auto c = 0; c < len; c++)
	{
		if (s[c] != '0')
			flag = true;
		if (flag)
			ans.push_back(s[c]);
	}
	return ans;
}
int main()
{
	int i, n, t;
	vector<ll> x;
	scanf("%d", &t);
	for (i = 0; i < t; i++)
	{
		ll ans = 0;
		scanf("%s", s);		
		printf("Case #%d: %s\n", i+1, f().c_str());
	}
	return 0;
}