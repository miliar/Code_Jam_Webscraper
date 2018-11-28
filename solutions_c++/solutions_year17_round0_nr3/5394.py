#include <stdio.h>
#include <bits/stdc++.h>
#define ll long long
#define ull unsigned long long
using namespace std;
const int N = 1005;

tuple<int,int> f(int n, int k)
{
	if (n == k || n==1)
		return{ 0,0 };
	int ma=-1, mi=-1;
	vector<bool> x(n+3, false);
	x[1] = true; x[n + 2] = true; // work 1-based
	while (k--)
	{
		vector<int> le(n + 3, -1);
		vector<int> ri(n + 3, -1);
		int prev = 1; // x[1]=true
		for (auto i = 2; i <= n + 1; i++) // iter over all posibilities for Left
		{
			if (!x[i]) // free cell
			{
				le[i] = i - prev;
			}
			else
			{
				prev = i;
			}
		}
		prev = n + 2; // x[n+2] for sure true
		for (auto i = n+1; i >= 2; i--) // iter over all posibilities for Right
		{
			if (!x[i]) // free cell
			{
				ri[i] = prev- i;
			}
			else
			{
				prev = i;
			}
		}
		using pipii = pair<int, pair<int, int>>;
		//vector<pair<int, pair<int,int>>> y; // min , max, idx
		vector<pipii> y;

		for (auto i = 2; i <= n + 1; i++)
			y.push_back(make_pair(min(le[i], ri[i]), make_pair(max(le[i], ri[i]), i)));
		sort(y.begin(), y.end());
		if (y[n - 1].first == y[n - 2].first) // conflict
		{
			vector<pipii> z;
			for (auto j = n - 1; j >= 0; j--)
			{
				if (y[j].first == y[n - 1].first) // same min value
					z.push_back(y[j]);
				else
					break;
			}

			sort(z.begin(), z.end(), [](pipii &a, pipii &b)->bool {return a.second.first < b.second.first; }); // sort based on max
			int len = z.size();
			if (z[len - 1].second.first == z[len - 2].second.first)
			{
				// conflict
				auto curIdx = N;
				auto tmpIdx = -1;
				for (auto j = len - 1; j >= 0; j--)
				{
					if (z[j].second.first == z[len - 1].second.first) // same max value
					{
						if (z[j].second.second < curIdx)
						{
							curIdx = z[j].second.second;
							tmpIdx = j;
						}
					}
					else
						break;
				}
				ma = z[tmpIdx].second.first;
				mi = z[tmpIdx].first;
				x[z[tmpIdx].second.second] = true;
			}
			else
			{
				ma = z[len - 1].second.first;
				mi = z[len - 1].first;
				x[z[len - 1].second.second] = true;
			}
		}
		else
		{
			ma = y[n - 1].second.first;
			mi = y[n - 1].first;
			x[y[n - 1].second.second] = true;
		}
	}
	return { ma-1,mi-1 };
}
int main()
{
	int i, n, t,k;
	vector<ll> x;
	scanf("%d", &t);
	for (i = 0; i < t; i++)
	{
		scanf("%d %d", &n,&k);
		int tmpMa, tmpMi;
		tie(tmpMa, tmpMi) = f(n, k);
		printf("Case #%d: %d %d\n", i+1, tmpMa, tmpMi);
	}
	return 0;
}