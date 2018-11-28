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
pLL cackes[MaxN + 10];

void solve()
{
	int n, k;
	cin >> n >> k;
	LL r, h;
	for (int i = 0; i < n; i++)
	{
		cin >> r >> h;
		cackes[i] = { r, h };
	}

	sort(cackes, cackes + n);
	LL curHeight = 0;
	LL ans = 0;
	set<LL> heighes;
	for (int i = 0; i < k-1; i++)
	{
		LL t =  cackes[i].second * 2LL * cackes[i].first;
		curHeight += t;
		heighes.insert(t);
	}

	for (int i = k-1; i < n; i++)
	{
		LL t = cackes[i].second * 2LL * cackes[i].first;
		curHeight += t;
		LL tAns = curHeight + sqr(cackes[i].first);
		if (tAns > ans)
			ans = tAns;

		heighes.insert(t);
		t = *heighes.begin();
		curHeight -= t;
		heighes.erase(heighes.begin());
	}

	dbl ansDbl = ans;
	ansDbl *= 3.14159265359;
	cout << ansDbl << endl;
}


int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	// LL a[110];
	// memset(a,0,sizeof(a));

	freopen("A-large.in","r",stdin);
	freopen("output_A_large.txt","w",stdout);
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