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


void solve()
{
	int n, p;
	cin >> n >> p;
	vi v(p, 0);
	for (int i = 0; i < n; i++)
	{
		int t;
		cin >> t;
		v[t%p]++;
	}
	int ans = v[0];
	if (p == 2) ans += (v[1]+1) / 2;
	else
	{
		if (p == 3)
		{
			if (v[1] + v[2] > 0)
			{
				int t = min(v[1], v[2]);
				ans += t;
				v[1] -= t;
				v[2] -= t;
				ans += (v[1] + 2) / 3 + (v[2] + 2) / 3;
			}
		}
		else
		{
			// p == 4
			int t = min(v[1], v[3]);
			ans += t;
			v[1] -= t;
			v[3] -= t;
			ans += (v[2]) / 2;
			v[2] %= 2;
			t = max(v[1], v[3]);
			if (v[2] == 1)
			{
				ans++;
				if (t > 2) ans += (t - 2 + 3) / 4;
			}
			else ans += (t + 3) / 4;

			//cout << ans << endl;
		}
	}

	cout << ans << endl;
}


int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	// LL a[110];
	// memset(a,0,sizeof(a));

	freopen("A-large.in", "r", stdin);
	//freopen("A-small-attempt0.in", "r", stdin);
	freopen("output_A_large.txt","w",stdout);
	//cout<<fixed;
	//cout<<setprecision(9);

	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
	}

	return 0;
}