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

pair<uLL, uLL> solve(uLL n, uLL k)
{
	if (n == k)
		return{ 0, 0 };

	uLL mid = (n + 1) / 2;
	uLL mn = mid - 1;
	uLL mx = n - mid;
	//cout << n << " " << k << "\t" << mid << "\t" << mn << " " << mx << endl;
	if (k == 1)
		return{ mx, mn };

	k--;
	if (k % 2 == 0)
		return solve(mn, k / 2);
	else
		return solve(mx, (k + 1) / 2);
}

void solve()
{
	LL n, k;
	cin >> n >> k;
	pair<uLL, uLL> ans = solve(n, k);
	//if (ans.first < ans.second) swap(ans.first, ans.second);
	cout << ans.first << " " << ans.second << endl;
}


int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	// LL a[110];
	// memset(a,0,sizeof(a));

	freopen("C-large.in","r",stdin);
	freopen("output-large.out","w",stdout);
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