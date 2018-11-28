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

const string name = "ROYGBV";

void solve(int t)
{
	int n;
	cin >> n;

	int C = 6;
	vi c(C);
	for (int i = 0; i < C; ++i)
	{
		cin >> c[i];
	}

	vi res;

	while (res.size() != n - 2)
	{
		int max_i = -1;
		int max_n = 0;
		int next_i = -1;
		int next_n = 0;
		for (int i = 0; i < C; ++i)
		{
			if (c[i] > max_n)
			{
				next_i = max_i;
				next_n = max_n;
				max_i = i;
				max_n = c[i];
			}
			else if (c[i] > next_n)
			{
				next_i = i;
				next_n = c[i];
			}
		}
		if (res.empty() || res[res.size() - 1] != max_i)
		{
			res.push_back(max_i);
			--c[max_i];
		}
		else if (next_i != -1)
		{
			res.push_back(next_i);
			--c[next_i];
		}
		else
		{
			cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
			return;
		}
	}

	for (int i = 0; i < C; ++i)
	{
		if (c[i] == 2)
		{
			cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
			return;
		}
	}

	for (int i = 0; i < C; ++i)
	{
		if (c[i] && i == res[0] && i != res[res.size() - 1])
		{
			res.push_back(i);
			--c[i];
			break;
		}
	}

	for (int i = 0; i < C; ++i)
	{
		if (c[i] && i == res[0] && i == res[res.size() - 1])
		{
			cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
			return;
		}
	}

	for (int i = 0; i < C; ++i)
	{
		if (c[i] && i != res[0] && i != res[res.size() - 1])
		{
			res.push_back(i);
			--c[i];
		}
	}

	if (res.size() != n)
	{
		cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
		return;
	}

	cout << "Case #" << t + 1 << ": ";
	for (int i = 0; i < n; ++i)
		cout << name[res[i]];
	cout << endl;
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
