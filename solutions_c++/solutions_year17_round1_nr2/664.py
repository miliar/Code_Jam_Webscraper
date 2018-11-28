#define _CRT_SECURE_NO_DEPRECATE 1
#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

struct item
{
	int l, r, c;

	item(int _l = 0, int _r = 0, int _c = 0)
	{
		l = _l;
		r = _r;
		c = _c;
	}

	int operator <(const item& b) const
	{
		if (l != b.l)
			return l < b.l;
		if (r != b.r)
			return r < b.r;
		return c < b.c;
	}
};

void solve(int tn)
{
	int r[100];
	int cur[100];
	vector<item> lists[100];
	int n, p;
	cin >> n >> p;
	for (int i = 0; i < n; i++)
		cin >> r[i];

	set<item> s;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < p; j++)
		{
			int x;
			cin >> x;
			int L = ceil(x / 1.1 / r[i] - 1.e-8);
			int R = floor(x / 0.9 / r[i] + 1.e-8);
			lists[i].push_back(item(L, R, i));
		}
		sort(lists[i].begin(), lists[i].end());
		cur[i] = 0;
		s.insert(lists[i][0]);
	}

	int ans = 0;
	bool finish = false;
	while (!finish)
	{
		auto min = *s.begin();
		auto max = *s.rbegin();
		if (min.r >= max.l)
		{
			ans++;
			s.clear();
			for (int i = 0; i < n; i++)
			{
				cur[i]++;
				if (cur[i] >= p)
				{
					finish = true;
					break;
				}
				s.insert(lists[i][cur[i]]);
			}
		}
		else
		{
			s.erase(min);
			cur[min.c]++;
			if (cur[min.c] >= p)
				finish = true;
			else
				s.insert(lists[min.c][cur[min.c]]);
		}
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
