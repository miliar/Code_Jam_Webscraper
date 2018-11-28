#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
#include <map>
#include <iterator>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define TASK ""
#define X first
#define Y second
#define inb push_back
#define utp pop_back
#define INF 2e9
#define LING 9e18

map<ll, ll> z;

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen(TASK".in", "r", stdin);
	freopen(TASK".out", "w", stdout);
#endif
	int t;
	cin >> t;
	int p = 0;
	while (t--)
	{
		cout << "Case #" << p + 1 << ": ";
		ll n, k;
		cin >> n >> k;
		ll i = 0;
		z.clear();
		set<pair<ll, ll> > s;
		s.insert({ n, 1 });
		while (i < k)
		{
			auto j = *s.rbegin();
			if (j.Y + i >= k)
			{
				cout << j.X / 2 << ' ' << (j.X - 1) / 2 << '\n';
				break;
			}
			else
				i += j.Y;
			if (j.X / 2)
			{
				s.erase({ j.X / 2, z[j.X / 2] });
				z[j.X / 2] += j.Y;
				s.insert({ j.X / 2, z[j.X / 2] });
			}
			--j.X;
			if (j.X / 2)
			{
				s.erase({ j.X / 2, z[j.X / 2] });
				z[j.X / 2] += j.Y;
				s.insert({ j.X / 2, z[j.X / 2] });
			}
			s.erase({ j.X + 1, j.Y });
		}
		++p;
	}
}