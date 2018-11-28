#define _CRT_SECURE_NO_DEPRECATE 1
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <complex>
using namespace std;

void solve(int tn)
{
	string s;
	string t;
	cin >> s;
	t = s;
	for (int i = 0; i < s.length(); i++)
	{
		for (int j = i; j < s.length(); j++)
			t[j] = s[i];
		if (t > s)
		{
			t[i] = s[i] - 1;
			for (int j = i + 1; j < s.length(); j++)
				t[j] = '9';
			while (t[0] == '0')
				t = t.substr(1);
			cout << "Case #" << tn << ": " << t << endl;
			return;
		}
	}
	cout << "Case #" << tn << ": " << s << endl;
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

