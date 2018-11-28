/*
Hanit Banga
*/

#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define pb push_back
#define fast_cin() ios_base::sync_with_stdio(false)

typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

const int N = 1e5 + 5;

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		int n, r, o, y, g, b, v;
		int b2 = 0, r2 = 0, y2 = 0;
		cin >> n >> r >> o >> y >> g >> b >> v;
		// bool possible = true;
		while (o)
		{
			if (b < 2)
				break;

			int temp = min(o, b / 2);
			o -= temp;
			b2 += temp;
			b += temp;
			b -= 2 * temp;
		}

		while (g)
		{
			if (r < 2)
				break;

			int temp = min(g, r / 2);
			g -= temp;
			r2 += temp;
			r += temp;
			r -= 2 * temp;
		}

		while (v)
		{
			if (y < 2)
				break;

			int temp = min(v, y / 2);
			v -= temp;
			y2 += temp;
			y += temp;
			y -= 2 * temp;
		}

		// cout << ' ' << r << ' ' << o << ' ' << y << ' ' << g << ' ' << b << ' ' << v << endl;

		if (o + v + g > 1)
		{
			cout << "IMPOSSIBLE\n";
			continue;
		}

		if (o + v + g == 1 and r + b + y > 1)
		{
			cout << "IMPOSSIBLE\n";
			continue;
		}

		if (o + v + g == 1 and r + b + y == 1)
		{
			if (o and b)
			{
				cout << "OB";
				if (b2)
					cout << "OB";
			}

			else if (g and r)
			{
				cout << "GR";
				if (r2)
					cout << "GR";
			}

			else if (v and y)
			{
				cout << "VY";
				if (y2)
					cout << "VY";
			}

			else
				cout << "IMPOSSIBLE";

			cout << endl;
			continue;
		}

		if (o + v + g == 1)
		{
			if (o)
				cout << "O";

			else if (v)
				cout << "G";

			else
				cout << "V";

			cout << endl;
			continue;
		}

		pair <int, char> p[3] = {{r, 'R'}, {b, 'B'}, {y, 'Y'}};
		sort(p, p + 3);
		int c1 = p[0].first, c2 = p[1].first, c3 = p[2].first;
		char p1 = p[0].second, p2 = p[1].second, p3 = p[2].second;

		if (c1 + c2 < c3)
		{
			cout << "IMPOSSIBLE\n";
			continue;
		}

		string ans = "";
		for (int i = 0; i < c1 - c3 + c2; ++i)
		{
			ans += p3;
			ans += p1;
			ans += p2;
		}

		for (int i = 0; i < c3 - c1; ++i)
		{
			ans += p3;
			ans += p2;
		}

		for (int i = 0; i < c3 - c2; ++i)
		{
			ans += p3;
			ans += p1;
		}

		for (auto &i : ans)
		{
			if (i == 'B' and b2)
			{
				cout << "BOB";
				--b2;
			}

			else if (i == 'R' and r2)
			{
				cout << "RGR";
				--r2;
			}

			else if (i == 'Y' and y2)
			{
				cout << "YVY";
				--y2;
			}

			else
				cout << i;
		}

		cout << endl;
	}	
}