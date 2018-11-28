#include <iostream>
#include <string>
using namespace std;
typedef unsigned long long ull;

ull strToNum(string s)
{
	ull factor = 1;
	ull res = 0;
	for (int i = s.size()-1; i >= 0; --i)
	{
		res += factor * (s[i] - '0');
		factor *= 10;
	}
	return res;
}

int fstDecPos(const string s)
{
	for (int i = 0; i < s.size()-1; ++i)
	{
		if (s[i] > s[i+1])
			return i+1;
	}
	return -1;
}

int findBlockStart(const string s, int x)
{
	for (int i = x; i > 0; --i)
		if (s[i] != s[i-1])
			return i;
	return 0;
}

int main()
{
	int numTests;
	cin >> numTests;
	for (int t = 1; t <= numTests; ++t)
	{
		string s;
		cin >> s;
		int decPos = fstDecPos(s);
		if (decPos == -1)
		{
			cout << "Case #" << t << ": " << strToNum(s) << endl;
			continue;
		}
		int blockStart = findBlockStart(s,decPos-1);
		s[blockStart]--;
		for (int i = blockStart+1; i < s.size(); ++i)
			s[i] = '9';
		cout << "Case #" << t << ": " << strToNum(s) << endl;
	}
}