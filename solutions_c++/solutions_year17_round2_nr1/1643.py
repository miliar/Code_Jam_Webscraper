#include <algorithm>
#include <bitset>
#include <cassert>
#include <deque>
#include <queue>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <float.h>
#include <limits>
#include <list>
#include <map>
#include <math.h>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pi;
typedef pair<ll, ll> pl;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<unsigned> vu;
typedef vector<ll> vl;
typedef vector<pi> vp;
typedef vector<string> vs;
typedef set<int> si;
typedef map<int, int> mi;

void solve(int t)
{
	int d, n;
	cin >> d >> n;

	vp ks(n);
	double tm = 0;
	for (int i = 0; i < n; ++i)
	{
		cin >> ks[i].first >> ks[i].second;
		tm = max(tm, ((double)d - (double)ks[i].first) / (double)ks[i].second);
	}

	double res = (double)d / tm;

	cout << "Case #" << t + 1 << ": " << setprecision(17) << res << endl;
}

int main(int argc, char* argv[])
{
	int t;
	cin >> t;

	for (int i = 0; i < t; ++i)
	{
		solve(i);
	}
	return 0;
}
