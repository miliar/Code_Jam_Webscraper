// 0408.A.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"
#include<string>
#include<iostream>
using namespace std;

#define maxn 1001

int cas;
int input[maxn];

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		string s;
		cin >> s;
		for (int i = 0; i < s.length(); i++)
			if (s[i] == '-') input[i] = -1;
			else input[i] = 1;
		int k,ans=0;
		cin >> k;
		for (int i = 0; i <= s.length()-k; i++)
		{
			if (input[i] == -1)
			{
				ans++;
				for (int j = 0; j < k; j++)
				{
					if (input[j + i] == 1) input[j + i] = -1;
					else input[j + i] = 1;
				}
			}
		}
		int i = s.length() - k;
		for (; i < s.length(); i++)
		{
			if (input[i] == -1) break;
		}
		if (i == s.length()) cout << "Case #" << ++cas << ": " << ans << endl;
		else cout << "Case #" << ++cas << ": impossible" << endl;
	}
	return 0;
}

