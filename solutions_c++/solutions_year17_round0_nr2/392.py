#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

string s;

void minusone(int x)
{
	--s[x];
	if (s[x] < '0' || (x>0 && s[x] < s[x-1]))
	{
		minusone(x-1);
		while (x<s.size())
			s[x++] = '9';
	}
}

void check(int x)
{
	if (s[x] >= s[x-1]) return;
	minusone(x-1);
	while (x < s.size())
		s[x++] = '9';
}

void solve()
{
	cin >> s;
	for (int i = 1; i < s.size(); ++i)
		check(i);
	for (int i = 0; i < s.size(); ++i)
		if (s[i] != '0')
		{
			cout << s.substr(i,s.size()-i) << endl;
			return;
		}
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int times;
	scanf("%d", &times);
	for (int i = 1; i <= times; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}