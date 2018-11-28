#include <stdio.h>
#include <bits/stdc++.h>
#define ll long long
#define ull unsigned long long
using namespace std;
const int N = 1500;
const int seconds = 24 * 60;
int main()
{
	int i, j, t, k;
	scanf("%d", &t);
	for (i = 0; i < t; i++)
	{
		int numc, numj;
		int c = 0, j = 1;
		int ans = 0;
		int cntc = 0, cntj = 0;
		scanf("%d %d", &numc, &numj);
		vector< pair<pair<int, int>, int>> x;
		vector<pair<int, int>> cc;
		vector<pair<int, int>> jj;
		int le, ri;
		for (auto idx = 0; idx < numc; idx++)
		{
			scanf("%d %d", &le, &ri);
			x.push_back({ { le,ri }, c });
			cc.push_back({ le,ri });
			cntc += (ri - le);
		}
		for (auto idx = 0; idx < numj; idx++)
		{
			scanf("%d %d", &le, &ri);
			x.push_back({ { le,ri }, j });
			jj.push_back({ le,ri });
			cntj += (ri - le);
		}
		sort(x.begin(), x.end());
		sort(cc.begin(), cc.end());
		sort(jj.begin(), jj.end());
		int cur = c;
		vector<int> cgap;
		vector<int> jgap;
		vector<int> ggap;
		for (auto idx = 0; idx < x.size()-1; idx++)
			if (x[idx].second == x[idx + 1].second)
			{
				if (x[idx].second==c)
					cgap.push_back(x[idx + 1].first.first - x[idx].first.second);
				else
					jgap.push_back(x[idx + 1].first.first - x[idx].first.second);
			}
			else
			{
				ans++;
				ggap.push_back(x[idx + 1].first.first - x[idx].first.second);
			}
		if (x[0].second == x[x.size() - 1].second)
		{
			if (x[0].first.first - x[x.size() - 1].first.second + seconds > 0)
			{
				if (x[0].second == c)
					cgap.push_back(x[0].first.first - x[x.size() - 1].first.second + seconds);
				else
					jgap.push_back(x[0].first.first - x[x.size() - 1].first.second + seconds);
			}
		}
		else
		{
			ans++;
			ggap.push_back(x[0].first.first - x[x.size() - 1].first.second + seconds);
		}
		sort(cgap.rbegin(), cgap.rend());
		sort(jgap.rbegin(), jgap.rend());
		sort(ggap.rbegin(), ggap.rend());
		while(!cgap.empty())
		{
			auto tmp = cgap.back();
			if (tmp + cntc <= 720)
			{
				cntc += tmp;
				cgap.pop_back();
			}
			else
			{
				cgap.back() -= 720 - cntc;
				cntc = 720;
				break;
			}
		}
		while (!jgap.empty())
		{
			auto tmp = jgap.back();
			if (tmp + cntj <= 720)
			{
				cntj += tmp;
				jgap.pop_back();
			}
			else
			{
				jgap.back() -= 720 - cntj;
				cntj = 720;
				break;
			}
		}
		sort(cgap.begin(), cgap.end());
		sort(jgap.begin(), jgap.end());
		sort(ggap.begin(), ggap.end());
		while (!ggap.empty())
		{
			auto tmp = ggap.back();
			if (cntj + tmp <= 720)
			{
				cntj += tmp;
				ggap.pop_back();
			}
			else
			{
				cntj = 720;
				ggap.back() -= 720 - cntj;
				break;
			}
		}
		while (!ggap.empty())
		{
			auto tmp = ggap.back();
			if (cntc + tmp <= 720)
			{
				cntc += tmp;
				ggap.pop_back();
			}
			else
			{
				cntc = 720;
				ggap.back() -= 720 - cntc;
				break;
			}
		}
		if (cntc < 720) {
			ans += 2*jgap.size();
		}
		else
			ans += 2*cgap.size();
		printf("Case #%d: %d\n", i + 1,ans);
	}
	return 0;
}