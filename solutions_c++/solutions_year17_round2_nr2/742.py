#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

char ans[1005];
int r0, b0, y0;

bool check(int n)
{
	if (ans[n-1] == ans[0]) return false;
	for (int i = 1; i < n; i++)
		if (ans[i-1] == ans[i])
			return false;
	return true;
}

int main()
{
	int tt;
	cin >> tt;
	for (int t = 1; t <= tt; t++)
	{
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        r0 = r, y0 = y, b0 = b;
        cout << "Case #" << t << ": ";
        char f = 'R';
        bool ok = true;
        if (r)
		{
			r--;
			ans[0] = f;
			for (int i = 1; i < n; i++)
			{

				if (ans[i-1] == 'R')
				{
					if (b <= 0 and y <= 0) ok = false;
					else if (b <= 0)
						ans[i] = 'Y', y--;
					else if (y <= 0)
						ans[i] = 'B', b--;
					else if (b > y)
						ans[i] = 'B', b--;
					else if (y > b)
						ans[i] = 'Y', y--;
					else if (f == 'B')
						ans[i] = 'B', b--;
					else ans[i] = 'Y', y--;

				}
				if (ans[i-1] == 'Y')
				{
					if (b<=0 and r<=0) ok = false;
					else if (b <=0)
						ans[i] = 'R', r--;
					else if (r<=0)
						ans[i] = 'B', b--;
					else if (b > r)
						ans[i] = 'B', b--;
					else if (r > b)
						ans[i] = 'R', r--;
					else if (f == 'B')
						ans[i] = 'B', b--;
					else ans[i] = 'R', r--;
				}
				if (ans[i-1] == 'B')
				{
					if (r<=0 and y<=0) ok = false;
					else if (r<=0)
						ans[i] = 'Y', y--;
					else if (r<=0)
						ans[i] = 'R', r--;
					else if (r > y)
						ans[i] = 'R', r--;
					else if (y > r)
						ans[i] = 'Y', y--;
					else if (f == 'R')
						ans[i] = 'R', r--;
					else ans[i] = 'Y', y--;
				}
			}
			if(check(n) and ok)
			{
				for (int i = 0; i < n; i++)
					cout << ans[i];
				cout << "\n";
				continue;
			}
		}
		r = r0, y = y0, b = b0;
		ok = true;
		f = 'Y';
		if (y)
		{
			y--;
			ans[0] = f;
			for (int i = 1; i < n; i++)
			{
				if (ans[i-1] == 'R')
				{
					if (b <= 0 and y <= 0) ok = false;
					else if (b <= 0)
						ans[i] = 'Y', y--;
					else if (y <= 0)
						ans[i] = 'B', b--;
					else if (b > y)
						ans[i] = 'B', b--;
					else if (y > b)
						ans[i] = 'Y', y--;
					else if (f == 'B')
						ans[i] = 'B', b--;
					else ans[i] = 'Y', y--;

				}
				if (ans[i-1] == 'Y')
				{
					if (b<=0 and r<=0) ok = false;
					else if (b <=0)
						ans[i] = 'R', r--;
					else if (r<=0)
						ans[i] = 'B', b--;
					else if (b > r)
						ans[i] = 'B', b--;
					else if (r > b)
						ans[i] = 'R', r--;
					else if (f == 'B')
						ans[i] = 'B', b--;
					else ans[i] = 'R', r--;
				}
				if (ans[i-1] == 'B')
				{
					if (r<=0 and y<=0) ok = false;
					else if (r<=0)
						ans[i] = 'Y', y--;
					else if (r<=0)
						ans[i] = 'R', r--;
					else if (r > y)
						ans[i] = 'R', r--;
					else if (y > r)
						ans[i] = 'Y', y--;
					else if (f == 'R')
						ans[i] = 'R', r--;
					else ans[i] = 'Y', y--;
				}
			}
			if(check(n) and ok)
			{
				for (int i = 0; i < n; i++)
					cout << ans[i];
				cout << "\n";
				continue;
			}
		}
		r = r0, y = y0, b = b0;
		ok = true;
		if (b)
		{
			f = 'B';
			b--;
			ans[0] = f;
			for (int i = 1; i < n; i++)
			{
				//cout << r << " " << b << " " << y << "\n";
				if (ans[i-1] == 'R')
				{
					if (b <= 0 and y <= 0) ok = false;
					else if (b <= 0)
						ans[i] = 'Y', y--;
					else if (y <= 0)
						ans[i] = 'B', b--;
					else if (b > y)
						ans[i] = 'B', b--;
					else if (y > b)
						ans[i] = 'Y', y--;
					else if (f == 'B')
						ans[i] = 'B', b--;
					else ans[i] = 'Y', y--;

				}
				if (ans[i-1] == 'Y')
				{
					if (b<=0 and r<=0) ok = false;
					else if (b <=0)
						ans[i] = 'R', r--;
					else if (r<=0)
						ans[i] = 'B', b--;
					else if (b > r)
						ans[i] = 'B', b--;
					else if (r > b)
						ans[i] = 'R', r--;
					else if (f == 'B')
						ans[i] = 'B', b--;
					else ans[i] = 'R', r--;
				}
				if (ans[i-1] == 'B')
				{
					if (r<=0 and y<=0) ok = false;
					else if (r<=0)
						ans[i] = 'Y', y--;
					else if (r<=0)
						ans[i] = 'R', r--;
					else if (r > y)
						ans[i] = 'R', r--;
					else if (y > r)
						ans[i] = 'Y', y--;
					else if (f == 'R')
						ans[i] = 'R', r--;
					else ans[i] = 'Y', y--;
				}
			}
			if(check(n) and ok)
			{
				for (int i = 0; i < n; i++)
					cout << ans[i];
				cout << "\n";
				continue;
			}
		}
		cout << "IMPOSSIBLE\n";

	}
	return 0;
}
