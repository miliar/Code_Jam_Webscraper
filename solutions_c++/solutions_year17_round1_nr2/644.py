// I WISH I COULD WRITE SOMETHING COOL HERE BUT I'M TRYING TO HURRY!!!
// SAMUEL MAS LENTO PLZ.
#include <iostream>
#include <algorithm>
#include <vector>
#include <functional>
#include <set>

using namespace std;

struct range
{
	int a, b, i, j;
	
	bool bad()
	{
		return (b < a || b < 1);
	}
	
	bool operator<(const range& rhs) const
	{
		if (a != rhs.a) return a < rhs.a;
		if (b != rhs.b) return b < rhs.b;
		if (i != rhs.i) return i < rhs.i;
		return j < rhs.j;
	}
	
	range merge(const range& rhs) const
	{
		return {max(a, rhs.a), min(b, rhs.b), -1, -1};
	}
};

typedef set<range> setr;

int solve()
{
	int n, p, i, j, q;
	cin >> n >> p;
	vector<int> rs(n);
	vector<setr> packs(n);
	setr ordering;
	
	for (i = 0; i < n; i++)
		cin >> rs[i];
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < p; j++)
		{
			cin >> q;
			int s110 = (10 * q + (11 * rs[i] - 1)) / (11 * rs[i]);
			int s90 = (10 * q) / (9 * rs[i]);
			if (s110 <= s90)
			{
				range ing = {s110, s90, i, j};
				ordering.insert(ing);
				packs[i].insert(ing);
			}
		}
	}
	
	int kits = 0;
	bool done = false;
	for (i = 0; i < n; i++)
		done |= packs[i].empty();
	while (!done)
	{
		range next = *ordering.begin();
		range combo = next;
		ordering.erase(ordering.begin());
		for (i = 0; i < n && !combo.bad(); i++)
			combo = packs[i].begin()->merge(combo);
		if (combo.bad())
		{
			packs[next.i].erase(next);
			done = packs[next.i].empty();
		}
		else
		{
			kits++;
			for (i = 0; i < n; i++)
			{
				packs[i].erase(packs[i].begin());
				done |= packs[i].empty();
			}
		}
	}
	return kits;
}

int main()
{
	int t;
	cin >> t;
	for (int c = 1; c <= t; c++)
	{
		printf("Case #%d: %d\n", c, solve());
	}
}
