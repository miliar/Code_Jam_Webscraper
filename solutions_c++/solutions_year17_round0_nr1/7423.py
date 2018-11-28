#include <iostream>
#include <algorithm>
#include <fstream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <iomanip>
#include <cassert>
#include <set>
#include <map>
#include <stdlib.h>
#include <string.h>
#include <bitset>

#define show(x) cerr << "# " << #x << " = " << (x) << endl

#define fast_IO() ios_base::sync_with_stdio(false)
#define FOR(i, a, b) for(__typeof(a) i = a; i != b; i++)
#define FR(i, a) FOR(i, 0, a)
#define FOREACH(i, t) FOR(i, t.begin(), t.end())
#define ALL(x) (x).begin(), (x).end()
#define SZ(a) int(a.size())
#define PB push_back
#define MP make_pair
#define F first
#define S second


#define _USE_MATH_DEFINES
using namespace std;

inline bool ascending(int i, int j) { return (i < j); }
inline bool descending(int i, int j) { return (i > j); }

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

#define MOD 1000000007
const int MN = 100000+51;



int main(){
	fast_IO();	
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		string s;
		int t;
		cin >> s >> t;
		int res = 0;
		for (int j = 0; j < SZ(s) - t+1; ++j)
		{
			if (s[j] == '-')
			{
				res++;
				for (int k = 0; k < t; ++k)
				{
					if (s[j+k] == '-') s[j+k] = '+';
					else s[j+k] = '-';
				}
			}
		}
		bool flag = true;
		for (int j = 0; j < SZ(s); ++j)
		{
			if (s[j] == '-') flag = false;
		}
		cout << "Case #" << i+1 << ": ";
		if (flag)
			cout << res << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
