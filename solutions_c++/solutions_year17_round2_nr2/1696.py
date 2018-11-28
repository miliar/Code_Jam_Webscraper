#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, i, n, r, o, y, g, b, v, temp, j, m1, m2, m3;
	char c1, c2, c3;
	cin >> t;
	for (i = 1; i <= t; i++)
	{
		cin >> n >> r >> o >> y >> g >> b >> v;
		temp = n >> 1;
		cout << "Case #" << i << ": ";
		if (r > temp || y > temp || b > temp)
			cout << "IMPOSSIBLE";
		else
		{
			if (r >= y && r >= b)
			{
				c1 = 'R';
				m1 = r;
				if (y > b)
				{
					c2 = 'Y';
					m2 = y;
					c3 = 'B';
					m3 = b;
				}
				else
				{
					c2 = 'B';
					m2 = b;
					c3 = 'Y';
					m3 = y;
				}
			}
			else if (y >= r && y >= b)
			{
				c1 = 'Y';
				m1 = y;
				if (r > b)
				{
					c2 = 'R';
					m2 = r;
					c3 = 'B';
					m3 = b;
				}
				else
				{
					c2 = 'B';
					m2 = b;
					c3 = 'R';
					m3 = r;
				}
			}
			else
			{
				c1 = 'B';
				m1 = b;
				if (r > y)
				{
					c2 = 'R';
					m2 = r;
					c3 = 'Y';
					m3 = y;
				}
				else
				{
					c2 = 'Y';
					m2 = y;
					c3 = 'R';
					m3 = r;
				}
			}
			while (m2 > m3)
			{
				cout << c1 << c2;
				m1--;
				m2--;
			}
			while (m1 > m2)
			{
				cout << c1;
				m1--;
				if (m2 > 0)
				{
					cout << c2;
					m2--;
				}
				if (m1 > 0)
				{
					cout << c1;
					m1--;
				}
				if (m3 > 0)
				{
					cout << c3;
					m3--;
				}
			}
			while (m1 > 0)
			{
				cout << c1;
				m1--;
				if (m2 > 0)
				{
					cout << c2;
					m2--;
				}
				if (m3 > 0)
				{
					cout << c3;
					m3--;
				}
			}
		}
		cout << endl;
	}
	return 0;
}