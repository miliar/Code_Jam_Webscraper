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

void solve(int t){	string s;	cin >> s;	int n = s.length();	string res;	for (int i = 0; i < n; ++i)	{		if (i == n - 1 || s[i] <= s[i + 1])			res += s[i];		else		{			if (s[i] == '1')			{				res = string(n - 1, '9');			}			else			{				int j = i - 1;				while (j >= 0 && s[j] == s[i])					--j;				res = res.substr(0, j + 1);				res += s[i] - 1;				res += string(n - j - 2, '9');			}			break;		}	}	cout << "Case #" << t + 1 << ": " << res << endl;}int main(int argc, char* argv[]){	int t;	cin >> t;	for (int i = 0; i < t; ++i)	{		solve(i);	}	return 0;}