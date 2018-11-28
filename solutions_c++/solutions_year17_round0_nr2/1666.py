#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

char s[1000];

string solve(string s)
{
	for (int i = 1; i < s.size(); ++i)
	{
		if (s[i - 1] > s[i])
		{
			s[i - 1]--;
			for (int j = i; j < s.size(); ++j)
				s[j] = '9';
			return solve(s);
		}
	}

	if (s[0] == '0')
	{
		return s.substr(1);
	}
	return s;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int cn = 1; cn <= T; ++cn)
	{
		scanf("%s", s);
		printf("Case #%d: %s\n", cn, solve(s).c_str());
	}
}