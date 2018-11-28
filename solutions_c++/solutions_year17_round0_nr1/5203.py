// GCJ.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

int query;

int main()
{
	ofstream cout("small_output.txt");
	ifstream cin("inp.in");

	cin >> query;
	for (int asd = 0; asd < query; ++asd)
	{
		string s;
		int k, cnt = 0;
		cin >> s >> k;
		for (int i = 0; i < s.size(); ++i)
		{
			if (s[i] == '-' && i + k <= s.size())
			{
				++cnt;
				for (int j = i; j < i + k; ++j)
				{
					if (s[j] == '-')
					{
						s[j] = '+';
					}
					else
					{
						s[j] = '-';
					}
				}
			}
		}
		bool flag = true;
		for (int i = 0; i < s.size(); ++i)
		{
			if (s[i] == '-')
			{
				flag = false;
			}
		}
		cout << "Case #" << (asd + 1) << ": ";
		if (!flag)
		{
			cout << "IMPOSSIBLE";
		}
		else
		{
			cout << cnt;
		}
		cout << endl;
	}
    return 0;
}

