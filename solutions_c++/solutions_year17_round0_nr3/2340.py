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
#include <fstream>
#include <stack>
#include <queue>
#define PI acos(-1.0)
#define VI vector<int>
#define PII pair<int,int>
#define MP make_pair
#define INF 10000
#define eps 1e-12
#define ll long long
#define f0(i , n) for (int i = 0; i < n; i++)
#define NMAX 5000

using namespace std;

ll test, i, j , t;

ll n , k;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	cin >> test;
	for (t = 1; t <= test; t++)
	{
		cin >> n>>k;

		map<ll, ll> cnt;
		set<ll> q;
		q.insert(n);
		cnt[n] = 1;

		while (1)
		{
			ll val = *q.rbegin();
			if (val <= 1)
				break;

			q.erase(val);

			cnt[val / 2] += cnt[val];
			cnt[(val - 1) / 2] += cnt[val];

			q.insert(val / 2);
			q.insert((val - 1) / 2);
		}
		
		vector< pair<ll, ll> > v;
		for (auto i : cnt)
		{
			v.push_back(i);
		}

		sort(v.rbegin(), v.rend());

		ll sum = 0;
		for (i = 0; i < v.size(); i++)
		{
			sum += v[i].second;
			if (sum >= k)
				break;
		}

		cout << "Case #" << t << ": " << v[i].first / 2 <<" "<<(v[i].first - 1) / 2<< endl;
	}
	return 0;
}