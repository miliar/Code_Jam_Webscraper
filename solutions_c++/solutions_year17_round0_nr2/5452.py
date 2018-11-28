#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstring>
#include<string>

using namespace std;

string s;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cin >> s;
		bool finished = 0;
		while (!finished)
		{
			finished = 1;
			for(int j = 0; j < s.size() - 1; j++)
			{
				if(s[j] > s[j + 1])
				{
					s[j]--;
					for (int k = j + 1; k < s.size(); k++)
						s[k] = '9';
					finished = 0;
					break;
				}
			}
		}
		while (s[0] == '0')
		{
			s = s.substr(1);
		}
		cout << "Case #" << i << ": " << s << endl;

	}
	return 0;
}
