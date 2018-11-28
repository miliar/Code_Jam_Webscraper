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

void solve(int t){	string s;	cin >> s;	int k;	cin >> k;	int n = s.length();	int res = 0;	for (int i = 0; i <= n - k; ++i)	{		if (s[i] == '-')		{			for (int j = 0; j < k; ++j)			{				if (s[i + j] == '-')					s[i + j] = '+';				else					s[i + j] = '-';			}			++res;		}	}	for (int i = n - k; i < n; ++i)	{		if (s[i] == '-')		{			cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;			return;		}	}	cout << "Case #" << t + 1 << ": " << res << endl;}int main(int argc, char* argv[]){	int t;	cin >> t;	for (int i = 0; i < t; ++i)	{		solve(i);	}	return 0;}