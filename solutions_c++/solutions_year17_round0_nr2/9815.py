#include <iostream>
#include <string>

using namespace std;
typedef long long LL;

LL solve(LL n)
{
	string s = to_string(n);

	int index = 1;
	bool tidy = true;
	for (int i = 1; i < s.length(); ++i)
	{
		if (s[i] < s[i - 1])
		{
			index = i;
			tidy = false;
			break;
		}
	}

	if (tidy)
	{
		return n;
	}

	bool allSame = false;
	bool allOnes = true;

	for (int i = 0; i < index; ++i)
	{
		if (s[i] != '1')
		{
			allOnes = false;
			break;
		}
	}

	if (index > 1 && !allOnes)
	{
		allSame = true;
	}

	for (int i = 1; i < index && !allOnes; ++i)
	{
		if (s[i] != s[i - 1])
		{
			allSame = false;
			break;
		}
	}

	for (int i = index - 1; i >= 0; --i)
	{
		if (s[i] > s[i + 1])
		{
			s[i]--;
		}
	}

	if (allOnes)
	{
		s[0] = '0';
		for (int i = 1; i < s.length(); ++i)
		{
			s[i] = '9';
		}
	}
	else if (allSame)
	{
		for (int i = index - 1; i < s.length(); ++i)
		{
			s[i] = '9';
		}
	}
	else
	{
		for (int i = index; i < s.length(); ++i)
		{
			s[i] = '9';
		}
	}

	return stoll(s);
}

int main()
{
	int t;
	LL n;
	string s;

	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cin >> n;
		LL answer = solve(n);

		cout << "Case #" << i << ": ";
		cout << answer << endl;
	}

	return 0;
}