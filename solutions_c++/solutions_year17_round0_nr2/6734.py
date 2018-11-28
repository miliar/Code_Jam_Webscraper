#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>

#pragma warning(disable:4996)

using namespace std;

int TI, T;


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> T;
	for (TI = 0; TI < T; TI++)
	{
		string s;
		cin >> s;
		char minFrom[100];
		if (s.length() == 1)
		{
			cout << "Case #" << TI + 1 << ": " << s << endl;
			continue;
		}
		int i, j, l = s.length();
		//cout << "string=" << s;
		for (int I = 0; I < l+5; I++)
		{
			for (i = 0; i < l - 1; i++)
			{
				if (s[i] > s[i + 1])
				{
					while (s[i] == '1' && i > 0)
						i--;

					s[i]--;

					for (j = i + 1; j < l; j++)
					{
						s[j] = '9';
					}
					break;
				}
			}
		}
		//cout << " to " << s << endl;
		char curMin = '9';
		for (i = l - 1; i >= 0; i--)
		{
			if (s[i] < curMin)
				curMin = s[i];
			minFrom[i] = curMin;
		}
		cout << "Case #" << TI + 1 << ": ";
		/*
		for (i = 0; i < l; i++)
		{
			if (minFrom[i] == '0')
				continue;
			cout << minFrom[i];
		}
		*/
		for (i = 0; i < l; i++)
		{
			if (i == 0 && s[i] == '0' && s.length() > 1)
				continue;
			cout << s[i];
		}
		cout << endl;
	}
	return 0;
}