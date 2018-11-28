#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;

string str;

string solve(string s)
{
	for (int i = 0; i < (int)s.length() - 1; i++)
	{
		if (s[i] > s[i + 1])
		{
			s[i]--;
			for (int a = i + 1; a < (int)s.length(); a++)
				s[a] = '9';
			return solve(s);
		}
	}
	while (s[0] == '0')
		s = s.substr(1);
	return s;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		cin >> str;
		printf("Case #%d: ", i + 1);
		cout << solve(str) << endl;
	}
	return 0;
}
