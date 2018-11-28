#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stack>
#include <functional>
#include <set>
#include <queue>
#include <string>
#include <map>
#include <iomanip>
#include <sstream>

using namespace std;


int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		cout << "Case #" << t + 1 << ": ";
		string s;
		cin >> s;
		int i;
		bool fl = false;
		for (i = 0; i < s.length() - 1; i++)
			if (s[i + 1] < s[i])
			{
				fl = true;
				break;
			}
		if (!fl)
			cout << s << endl;
		else
		{
			for (int j = i; j >= 0; j--)
			{
				if (j == 0)
				{
					if (s[j] == '1')
					{
						for (int z = 0; z < s.length() - 1; z++)
							cout << '9';
						cout << endl;
						break;
					}
					else
					{
						s[j] = char(s[j] - 1);
						for (int z = j + 1; z < s.length(); z++)
							s[z] = '9';
						cout << s << endl;
						break;
					}
				}
				else
				{
					if (s[j] > s[j - 1])
					{
						s[j] = char(s[j] - 1);
						for (int z = j + 1; z < s.length(); z++)
							s[z] = '9';
						cout << s << endl;
						break;
					}
				}
			}
		}

	}
}