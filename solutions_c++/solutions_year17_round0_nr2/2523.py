#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int MAXN = 100500;

bool check(string &s)
{
	for (int i = 0; i < (int)s.size() - 1; i++)
		if (s[i] > s[i + 1])
			return false;
	return true;
}

void sol()
{
	string s;
	cin >> s;
	if (check(s))
	{
		cout << s << '\n';
		return;
	}

	for (int i = (int)s.size() - 1; i >= 1; i--)
	{
		s[i] = '9';
		s[i - 1]--;
		if (check(s) && s[0] != '0')
		{
			cout << s << '\n';
			return;
		}
	}

	for (int i = 0; i < (int)s.size() - 1; i++)
		cout << '9';
	cout << '\n';
	return;
}

int main()
{                                                     

	int t;
	scanf("%d", &t);

	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		sol();
	}
	
	return 0;
}

