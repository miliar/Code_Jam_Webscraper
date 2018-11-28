#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

string ans;
string s;
int flag = 0;
int n;

int rec(int ost, int r, int y, int b, int pred)
{
	if (flag == 1)
		return 1;
	if (ost == 0)
	{
		if ((int)s.length() == n && s[0] != s[n - 1])
		{
			ans = s;
			flag = 1;
			return 1;
		}
		else
			return 0;
	}
	int mx = max(r, max(y, b));
	if (mx > 0)
	{
		if (r == mx && y == mx && b == mx)
		{
			if (pred != 0)
			{
				s += 'R';
				rec(ost - 1, r - 1, y, b, 0);
				s.pop_back();
			}
			if (pred != 1)
			{
				s += 'Y';
				rec(ost - 1, r, y - 1, b, 1);
				s.pop_back();
			}
			if (pred != 2)
			{
				s += 'B';
				rec(ost - 1, r, y, b - 1, 2);
				s.pop_back();
			}
		}
		else if (r == mx && y == mx)
		{
			if (pred != 0)
			{
				s += 'R';
				rec(ost - 1, r - 1, y, b, 0);
				s.pop_back();
			}
			if (pred != 1)
			{
				s += 'Y';
				rec(ost - 1, r, y - 1, b, 1);
				s.pop_back();
			}
		}
		else if (r == mx && b == mx)
		{
			if (pred != 0)
			{
				s += 'R';
				rec(ost - 1, r - 1, y, b, 0);
				s.pop_back();
			}
			if (pred != 2)
			{
				s += 'B';
				rec(ost - 1, r, y, b - 1, 2);
				s.pop_back();
			}
		}
		else if (y == mx && b == mx)
		{
			if (pred != 1)
			{
				s += 'Y';
				rec(ost - 1, r, y - 1, b, 1);
				s.pop_back();
			}
			if (pred != 2)
			{
				s += 'B';
				rec(ost - 1, r, y, b - 1, 2);
				s.pop_back();
			}
		}
		else if (r == mx)
		{
			if (pred != 0 && r>0)
			{
				s += 'R';
				rec(ost - 1, r - 1, y, b, 0);
				s.pop_back();
			}
			if (pred != 1 && y>0)
			{
				s += 'Y';
				rec(ost - 1, r, y - 1, b, 1);
				s.pop_back();
			}
			if (pred != 2 && b>0)
			{
				s += 'B';
				rec(ost - 1, r, y, b - 1, 2);
				s.pop_back();
			}
		}
		else if (y == mx)
		{
			if (pred != 1 && y>0)
			{
				s += 'Y';
				rec(ost - 1, r, y - 1, b, 1);
				s.pop_back();
			}
			if (pred != 0 && r>0)
			{
				s += 'R';
				rec(ost - 1, r - 1, y, b, 0);
				s.pop_back();
			}
			if (pred != 2 && b>0)
			{
				s += 'B';
				rec(ost - 1, r, y, b - 1, 2);
				s.pop_back();
			}
		}
		else if (b == mx)
		{
			if (pred != 2 && b>0)
			{
				s += 'B';
				rec(ost - 1, r, y, b - 1, 2);
				s.pop_back();
			}
			if (pred != 0 && r>0)
			{
				s += 'R';
				rec(ost - 1, r - 1, y, b, 0);
				s.pop_back();
			}
			if (pred != 1 && y>0)
			{
				s += 'Y';
				rec(ost - 1, r, y - 1, b, 1);
				s.pop_back();
			}
			if (pred != 2 && b>0)
			{
				s += 'B';
				rec(ost - 1, r, y, b - 1, 2);
				s.pop_back();
			}
		}
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int q = 0; q < t; q++)
	{
		cin >> n;
		int x1, x2, x3, r, y, b;
		cin >> r >> x1 >> y >> x2 >> b >> x3;
		ans = "";
		s = "";
		flag = 0; 
		int d = n;
		if (r>y+b||b>r+y||y>r+b)
			ans = "IMPOSSIBLE";
		else
			rec(d, r, y, b, -1);
		if (flag==0)
			ans = "IMPOSSIBLE";
		cout << "Case #" << (q + 1) << ": " << ans << "\n";
	}
	return 0;
}