#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<queue>
#include<map>
#include<math.h>
#include<functional>
#include<vector>
#include<algorithm>

#define PI (2 * acos(0))

using namespace std;

vector<pair<int, int> > pc;

double get_ans(int rad, int n, int k)
{
	double ret = PI * rad * rad;
	vector<double> vals;
	int i;
	int mxh = 0;
	int mxi = -1;
	for (i = 0; i < n; i++)
	{
		if (pc[i].first == rad)
		{
			if (pc[i].second > mxh)
			{
				mxh = pc[i].second;
				mxi = i;
			}
		}
	}
	ret += (2.0 * PI * rad * mxh);
	for (i = 0; i < n; i++)
	{
		if (i == mxi)
			continue;
		if (pc[i].first <= rad)
		{
			vals.push_back(2.0 * PI * pc[i].first * pc[i].second);
		}
	}
	if (vals.size() < k - 1)
		return 0.0;
	sort(vals.begin(), vals.end());
	reverse(vals.begin(), vals.end());
	for (i = 0; i < k - 1; i++)
	{
		ret += vals[i];
	}
	return ret;
}

int main()
{
	//freopen("a-small-attempt1.in", "rt", stdin);
	//freopen("a-small_1.out", "wt", stdout);
	freopen("a-large.in", "rt", stdin);
	freopen("a-large.out", "wt", stdout);
	int i, j, kase, inp, n, k, l, r;
	scanf("%d", &inp);
	for (kase = 1; kase <= inp; kase++)
	{
		scanf("%d %d", &n, &k);
		pc.clear();
		for (i = 0; i < n; i++)
		{
			scanf("%d %d", &r, &l);
			pc.push_back(make_pair(r, l));
		}
		sort(pc.begin(), pc.end());
		double res = get_ans(pc[0].first, n, k);
		for (i = 1; i < n; i++)
		{
			//if (pc[i].first != pc[i - 1].first)
			//{
				double tres = get_ans(pc[i].first, n, k);
				if (tres > res)
					res = tres;
			//}
		}
		printf("Case #%d: %.9lf\n", kase, res);
	}
	return 0;
}
