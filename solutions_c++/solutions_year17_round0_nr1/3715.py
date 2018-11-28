#define _CRT_SECURE_NO_DEPRECATE 1
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
using namespace std;

void solve(int tn)
{
	string s;
	int k;
	cin >> s >> k;
	int ans = 0;
	for (int i = 0; i < s.length(); i++)
		if (s[i] == '-')
		{
			if (i + k - 1 >= s.length())
			{
				cout << "Case #" << tn << ": IMPOSSIBLE" << endl;
				return;
			}
			ans++;
			for (int j = i; j < i + k; j++)
				if (s[j] == '-')
					s[j] = '+';
				else
					s[j] = '-';
		}
	cout << "Case #" << tn << ": " << ans << endl;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf_s("%d", &t);
	for (int it = 0; it < t; it++)
		solve(it + 1);
	return 0;
}
