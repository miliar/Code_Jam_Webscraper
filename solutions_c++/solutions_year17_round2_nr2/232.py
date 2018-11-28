#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int a[3], ind[3];
string c[3];

bool cmp(int i, int j)
{
	return a[i] > a[j];
}

string solve(int r, int y, int b)
{
	a[0] = r;
	a[1] = y;
	a[2] = b;
	c[0] = "R";
	c[1] = "Y";
	c[2] = "B";
	for (int i = 0; i < 3; ++i)
	{
		ind[i] = i;
	}
	sort(ind, ind + 3, cmp);
	if (a[ind[0]] > a[ind[1]] + a[ind[2]])
	{
		return "IMPOSSIBLE";
	}
	string ans = "";
	while (a[ind[0]] > 0)
	{
		ans += c[ind[0]];
		if (a[ind[1]] + a[ind[2]] > a[ind[0]])
		{
			ans += c[ind[1]] + c[ind[2]];
			--a[ind[1]];
			--a[ind[2]];
		}
		else if (a[ind[1]] > a[ind[2]])
		{
			ans += c[ind[1]];
			--a[ind[1]];
		}
		else
		{
			ans += c[ind[2]];
			--a[ind[2]];
		}
		--a[ind[0]];
	}
	return ans;
}

string make_alternate(int n, string c1, string c2)
{
	string ans = "";
	for (int i = 0; i < n; ++i)
	{
		ans += c1 + c2;
	}
	return ans;
}

string insert_mixed(string ans, string base_color, string mixed_color, int mixed_color_count)
{
	for (int i = 0; i < ans.size(); ++i)
	{
		if (ans.substr(i, 1) == base_color)
		{
			ans = ans.insert(i + 1, make_alternate(mixed_color_count, mixed_color, base_color));
			return ans;
		}
	}
	return ans;
}

void solve()
{
	int n, r, o, y, g, b, v;
	scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
	string ans = "";
	if (o == b && o + b == n)
	{
		ans = make_alternate(o, "O", "B");
	}
	if (g == r && g + r == n)
	{
		ans = make_alternate(g, "G", "R");
	}
	if (v == y && v + y == n)
	{
		ans = make_alternate(v, "V", "Y");
	}
	if (ans == "" && ((o > 0 && o >= b) || (g > 0 && g >= r) || (v > 0 && v >= y)))
	{
		ans = "IMPOSSIBLE";
	}
	else if (ans == "")
	{
		ans = solve(r - g, y - v, b - o);
		if (ans != "IMPOSSIBLE")
		{
			ans = insert_mixed(ans, "R", "G", g);
			ans = insert_mixed(ans, "Y", "V", v);
			ans = insert_mixed(ans, "B", "O", o);
		}
	}
	cout << ans;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
