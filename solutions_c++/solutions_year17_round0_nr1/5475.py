#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstring>
#include<string>

using namespace std;

string s;
int k;
int res = -1;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cin >> s >> k;
		res = 0;
		for (int j = 0; j < s.size(); j++)
		{
			if (s[j] == '-')
			{
				if (s.size() - j < k)
				{
					break;
				}
				else
				{ 
					res++;
					for (int z = j; z < j + k; z++)
					{
						if (s[z] == '+')
							s[z] = '-';
						else
							s[z] = '+';
					}
				}
			}
		}
		cout << "Case #" << i << ": ";
		if (s.find('-') != string::npos)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << res << endl;
	}
	return 0;
}
