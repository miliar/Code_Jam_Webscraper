#include <iostream>
#include <string>
using namespace std;

void flip(string &s, int k, int pos)
{
	for (int i = pos; i < pos+k; ++i)
	{
		if (s[i] == '+')
			s[i] = '-';
		else
			s[i] = '+';
	}
}

int main()
{
	int numTests;
	cin >> numTests;
	for (int t = 1; t <= numTests; ++t)
	{
		string s;
		int k;
		cin >> s >> k;
		int cnt = 0;
		for (int i = 0; i < s.size()-k+1; ++i)
		{
			if (s[i] == '-')
			{
				flip(s,k,i);
				cnt++;
			}
		}
		bool imp = false;
		for (int i = s.size()-k+1; i < s.size(); ++i)
		{
			if (s[i] == '-')
			{
				imp = true;
				break;
			}
		}
		cout << "Case #" << t << ": ";
		if (imp)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << cnt << endl;
	}
}