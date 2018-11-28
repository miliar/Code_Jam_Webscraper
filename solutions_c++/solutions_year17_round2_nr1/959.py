#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <bitset>
#include <numeric>
#include <cassert>
#include <time.h>
#include <ctime>
#include <memory.h>
#include <complex>
#include <utility>
#include <climits>
#include <cctype>


using namespace std;
#pragma comment(linker, "/STACK:1024000000,1024000000")


typedef long long LL;
typedef unsigned long long uLL;
typedef double dbl;
typedef vector<int> vi;
typedef vector<LL> vL;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef pair<LL, LL> pLL;

#define mp(x,y)  make_pair((x),(y))
#define pb(x)  push_back(x)
#define sqr(x) ((x)*(x))

const int MaxN = 1000;
const dbl inf = 1000 * 1000 * 1000 * 2;
const dbl eps = 1e-7;
pair<dbl, dbl> h[MaxN + 10];
pLL h2[MaxN + 10];
dbl ctch[MaxN + 10];
//dbl dist[MaxN + 10];
//dbl delta[MaxN + 10];

void solve()
{
	LL d;
	int n;
	cin >> d >> n;
	for (int i = 0; i < n; i++)
	{
		LL k, v;
		cin >> k >> v;
		h[i] = { k, v };
		h2[i] = { k, v };
	}
	sort(h2, h2 + n);

	dbl minDelta = inf;
	for (int i = 1; i < n; i++)
	{
		if (h2[i].second >= h2[i - 1].second)
		{
			n = i;
			break;
		}
		else
		{
			dbl tmp = ((dbl)(h2[i].first - h2[i - 1].first)) / ((dbl(h2[i - 1].second - h2[i].second)));
			if (tmp < minDelta)
				minDelta = tmp;
		}
	}
	for (int i = 0; i < n; i++)
		h[i] = h2[i];

	dbl curTime = 0;
	for (int i = 0; i < n; i++)
	{
		dbl newH = h[0].first + h[0].second*minDelta;
		if (newH > d || abs(newH - d) < eps)
		{
			break;
		}
		for (int j = n - 1; j >= 0; j--)
			h[j].first += h[j].second*minDelta;

		curTime += minDelta;
		minDelta = inf;
		for (int j = n - 2; j >= 0; j--)
			if (abs(h[j + 1].first - h[j].first) < eps)
			{
				h[j].second = h[j + 1].second;
				ctch[j] = curTime;
			}
			else
			{
				dbl tmp = (h[j + 1].first - h[j].first);
				tmp /= (h[j].second - h[j + 1].second);
				minDelta = min(minDelta, tmp);
			}
	}

	curTime += (d - h[0].first) / h[0].second;
	dbl speed = d / curTime;
	cout << speed << endl;

}


int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	// LL a[110];
	// memset(a,0,sizeof(a));

	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);

	cout<<fixed;
	cout<<setprecision(9);

	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
	}

	return 0;
}