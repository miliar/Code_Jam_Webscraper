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

const int MaxN = 50;
dbl p[MaxN + 10];
dbl pEnd[MaxN + 10];

void solve()
{
	int n, k;
	cin >> n >> k;
	dbl u;
	cin >> u;

	for (int i = 0; i < n; i++)
		cin >> p[i];

	sort(p, p + n);
	p[n] = 1;
	pEnd[n] = 1;
	for (int i = n - 1; i >= 0; i--)
		pEnd[i] = pEnd[i + 1] * p[i];

	dbl ans = 0;
	dbl prev = p[0];
	for (int i = 1; i <= n; i++)
	{
		dbl need = (p[i] - prev)*i;
		if (need <= u)
		{
			u -= need;
			prev = p[i];
		}
		else
		{
			prev += u / i;
			u = 0;
		}
		dbl prob = pow(prev, i);
		prob *= pEnd[i];
		if (prob > ans)
			ans = prob;
	}

	cout << ans << endl;
}


int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	// LL a[110];
	// memset(a,0,sizeof(a));

	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("output_C_small.txt","w",stdout);
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