#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:160777216")
#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <cmath>
#include <string>
#include <cstdio>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <sstream>
#define eps 1e-6
#define INF 1000000000
#define VI vector<int>
#define PII pair<int,int>
#define MP make_pair
#define ALL(x) x.begin() , x.end()
#define PB push_back
#define FOR(i , n) for (i = 0; i < n; i++)
#define FAB(i , a , b) for (i = a; i <= b; i++)
#define ll long long
#define NMAX 100001
using namespace std;

int n, m, q, i, j, k , p , c;
set<int> s[2000] , s1[2000];
int u[2000];

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);

	
	int t;
	cin >> t;

	

	for (int test = 1; test <= t; test++)
	{
		
		cin >> n >> c >> m;
		vector<PII> v(m);
		for (i = 0; i < m; i++)
		{
			cin >> v[i].first >> v[i].second;
		}

		sort(v.begin(), v.end());
		
		int l = 1, r = m;
		int ans = 0 , ans1;
		while (l <= r)
		{
			int x = (l + r) / 2;

			for (i = 0; i < x; i++)
				s[i].clear() , s1[i].clear();

			int good = 1;
			int cnt = 0;
			for (i = 0; i < v.size(); i++)
			{
				int found = 0;
				for (j = 0; j < x; j++)
				{
					if (s[j].size() < v[i].first && s[j].find(v[i].second) == s[j].end() && s1[j].find(v[i].first) == s1[j].end())
					{
						found = 1;
						s[j].insert(v[i].second);
						s1[j].insert(v[i].first);
						break;
					}
				}

				if (!found)
				{
					for (j = 0; j < x; j++)
					{
						if (s[j].size() < v[i].first && s[j].find(v[i].second) == s[j].end())
						{
							cnt++;
							found = 1;
							s[j].insert(v[i].second);
							s1[j].insert(v[i].first);
							break;
						}
					}
				}
				if (!found)
				{
					good = 0;
					break;
				}
			}

			if (good)
			{
				ans = x;
				r = x - 1;
			}
			else
				l = x + 1;

		}

		ans1 = 0;
		for (i = 0; i <= n; i++)
			u[i] = 0;

		for (i = 0; i < v.size(); i++)
		{
			u[v[i].first]++;
		}

		for (i = 0; i <= n; i++)
		{
			if (u[i] > ans)
				ans1 += u[i] - ans;
		}

		cout << "Case #" << test << ": ";
		cout << ans << " "<<ans1<<endl;
		
	}
	return 0;
}