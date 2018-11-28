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
	int n;
	int r, o, y, g, b, v;
	cin >> n;
	cin >> r >> o >> y >> g >> b >> v;
	// R Y B
	map<char, char> color;
	// r >= y >= b
	color['r'] = 'R';
	color['y'] = 'Y';
	color['b'] = 'B';
	if (b > r)
	{
		swap(b, r);
		swap(color['b'], color['r']);
	}
	// r >= b
	if (y > r)
	{
		swap(y, r);
		swap(color['y'], color['r']);
	}
	// r >= y
	if (b > y)
	{
		swap(b, y);
		swap(color['b'], color['y']);
	}
	// y >= b

	if (r > y + b)
	{
		cout << "IMPOSSIBLE" << endl;
		return;
	}

	// r >= y >= b
	int d = y - b;
	for (int i = d; i > 0; i--)
		cout << color['r'] << color['y'];
	r -= d;
	y -= d;

	while (r > y)
	{
		cout << color['r'] << color['y'];
		r--;
		y--;
		if (r > 0)
		{
			cout << color['r'];
			r--;
		}
		if (b > 0)
		{
			cout << color['b'];
			b--;
		}
	}
	// r = y = b
	for (int i = 0; i < r; i++)
		cout << color['r'] << color['y'] << color['b'];
	cout << endl;
}


int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	// LL a[110];
	// memset(a,0,sizeof(a));

	freopen("B-small-attempt0.in","r",stdin);
	freopen("output_B.txt","w",stdout);
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