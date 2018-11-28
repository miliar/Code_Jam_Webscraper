#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
void reverse(char &c)
{
	if (c == '+') c = '-';
	else c = '+';
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n, t;
	string s;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		int ans = 0;
		cin >> s >> n;
		for (int j = 0; j <= s.length()-n; j++)
		{
			if (s[j] == '-')
			{
				ans++;
				for (int k = 0; k < n; k++) reverse(s[j + k]);
			}
		}
		bool flag = false;
		for (int j = s.length() - n + 1; j < s.length(); j++)
		{
			if (s[j] == '-')
			{
				cout << "Case #" << i << ": IMPOSSIBLE" << endl;
				flag = true;
				break;
			}
		}
		if (flag) continue;
		cout << "Case #" << i << ": " << ans<<endl;
	}
	return 0;
}