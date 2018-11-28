#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

bool is(string& s, int t, int k)
{
	if (s[t] == '+')
		return false;

	for (int i = t; i < t + k; ++i)
	{
		if (s[i] == '-')
			return true;
	}

	return false;
}

bool is2(string& s, int t, int k) 
{
	for (int i = t; i < t + k; ++i)
	{
		if (s[i] == '-')
			return true;
	}

	return false;
}

bool flip(string& s, int t, int k)
{
	for (int i = t; i < t + k; ++i)
	{
		s[i] = s[i] == '-' ? '+' : '-';
	}

	return false;
}

int do_case(string& s, int k)
{
	int n = 0;
	for (int i = 0; i < s.length() - k + 1; ++i) 
	{
		if (is(s, i, k))
		{
			flip(s, i, k);
			++n;
		}
	}

	return is2(s, 0, s.length()) ? -1 : n;
}

int main() 
{
	int T, K;
	cin >> T;
	string S;
	
	for (int i = 0; i < T; ++i) 
	{
		cin >> S;
		cin >> K;
		int s = do_case(S, K);
		//printf("%s %d\n", S.c_str(), s);
		if (s == -1)
			printf("Case #%d: IMPOSSIBLE\n", i + 1, s);
		else
			printf("Case #%d: %d\n", i + 1, s);
	}

	return 0;
}