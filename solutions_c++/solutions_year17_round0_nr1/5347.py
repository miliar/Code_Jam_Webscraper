#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
using namespace std;
inline void flip(char &c)
{
	if (c == '-')
		c = '+';
	else
		c = '-';
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, i, k, l, flip_count, j, m;
	bool possible;
	string s;
	cin >> t;
	for (i = 1; i <= t; i++)
	{
		cin >> s >> k;
		l = s.size();
		flip_count = 0;
		for (j = 0; j <= l - k; j++)
			if (s[j] == '-')
			{
				flip_count++;
				for (m = 0; m < k; m++)
					flip(s[j + m]);
			}
		possible = true;
		for (j = l - k + 1; j < l; j++)
			if (s[j] == '-')
			{
				possible = false;
				break;
			}
		cout << "Case #" << i << ": ";
		if (possible)
			cout << flip_count;
		else
			cout << "IMPOSSIBLE";
		cout << endl;
	}
	return 0;
}
