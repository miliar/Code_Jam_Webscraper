#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <bitset>
#include <unordered_map>
#include <unordered_set>

using namespace std;
typedef long long ll;



typedef pair<pair<int, int>, pair<int, int> > state;

int dst[101][201][101][101];

void validate(state& cur)
{
	if (cur.first.first <= 0)
		cur.first.first = 0;
	if (cur.second.first <= 0)
		cur.second.first = 0;
	if (cur.first.second > 100)
		cur.first.second = 100;
	if (cur.second.second <= 0)
		cur.second.second == 0;
}

int get(state &cur)
{
	validate(cur);
	return dst[cur.first.first][cur.first.second][cur.second.first][cur.second.second];
}

void Set(state &cur, int val)
{
	validate(cur);
	dst[cur.first.first][cur.first.second][cur.second.first][cur.second.second] = val;
}

int main() {
#ifdef _CONSOLE
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	ll test;
	cin >> test;
	for (ll t = 1; t <= test; ++t)
	{
		int hd, ad, hk, ak, b, d;
		cin >> hd >> ad >> hk >> ak >> b >> d;

		queue<state> q;
		q.push({ {hd,ad}, {hk, ak } });
		//map<state, int> dst;
		//dst[{ {hd, ad}, { hk, ak } }] = 0;
		for (int i = 0; i <= 100; ++i)
		{
			for (int j = 0; j <= 200; ++j)
			{
				for (int k = 0; k <= 100; ++k)
				{
					for (int m = 0; m <= 100; ++m)
					{
						dst[i][j][k][m] = 1e9;
					}
				}
			}
		}
		dst[hd][ad][hk][ak] = 0;
		int answer = -1;
		while (!q.empty())
		{
			state cur = q.front();
			int curlen = get(cur);
			q.pop();
			if (cur.second.first <= 0)
			{
				answer = get(cur);
				break;
			}
			if (cur.first.first <= 0)
			{
				continue;
			}
			state next = cur;
			next.second.first -= next.first.second;
			next.first.first -= next.second.second;
			validate(next);
			if (get(next) == 1e9)
			{
				Set(next, curlen + 1);
				q.push(next);
			}
			next = cur;
			next.first.second += b;
			next.first.first -= next.second.second;
			validate(next);
			if (get(next) == 1e9)
			{
				Set(next, curlen + 1);
				q.push(next);
			}
			next = cur;
			next.first.first = hd;
			next.first.first -= next.second.second;
			validate(next);
			if (get(next) == 1e9)
			{
				Set(next, curlen + 1);
				q.push(next);
			}
			next = cur;
			next.second.second -= d;
			next.second.second = max(0, next.second.second);
			next.first.first -= next.second.second;
			validate(next);
			if (get(next) == 1e9)
			{
				Set(next, curlen + 1);
				q.push(next);
			}
		}

		if (answer == -1)
		{
			//printf("Case #%d: IMPOSSIBLE\n", t);
			cout << "Case #" << t << ": IMPOSSIBLE\n";
		}
		else
		{
//			printf("Case #%d: %d\n", t, d);
			cout << "Case #" << t << ": "<<answer<<"\n";
		}
		
			
	}

	return 0;
}